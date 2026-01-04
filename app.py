# Streamlit app

import streamlit as st
from openai import OpenAI

from scenarios import get_scenario
from prompts import roleplay_prompt, evaluation_prompt

# Initialize OpenAI client
api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the client
client = OpenAI(api_key=api_key)

## App Header

st.set_page_config(page_title="The Inner Circle Game", layout="centered")

st.title("🎭 The Inner Circle Game")
st.subheader("A 5-minute role-play to practice real-life conversations")

st.write(
    "You will face a realistic situation. "
    "Respond naturally. The goal is practice, not perfection."
)

## Load Scenario

scenario = get_scenario("WORK_BOUNDARY_01")

st.markdown("### Scenario")
st.write(scenario["context"])

## Step 1: User First Response

user_response = st.text_area(
    "How would you respond?",
    placeholder="Type what you would actually say...",
    height=120
)

if user_response.strip() == "":
    st.stop()

## Step 2: AI Pushback

system_prompt, user_prompt = roleplay_prompt(scenario, user_response)

with st.spinner("The teammate responds..."):
    pushback = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

ai_pushback = pushback.choices[0].message.content

st.markdown("### Teammate")
st.write(ai_pushback)

## Step 3: Final User Response

final_response = st.text_area(
    "Your final response:",
    placeholder="Respond to the pushback...",
    height=120
)

if final_response.strip() == "":
    st.stop()

## Step 4: Evaluation

eval_system, eval_user = evaluation_prompt(scenario, final_response)

with st.spinner("Evaluating your response..."):
    evaluation = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": eval_system},
            {"role": "user", "content": eval_user}
        ],
        temperature=0
    )

evaluation_text = evaluation.choices[0].message.content

## Step 5: Display Feedback

st.markdown("## 📊 Feedback")
st.text(evaluation_text)

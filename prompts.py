# Role-play & evaluation prompts

# Prompt A - Role play Pushback
def roleplay_prompt(scenario, user_response):
    system_prompt = (
        "You are role-playing a human in a real-life situation.\n"
        "Stay fully in character.\n"
        "Be realistic, casual, and slightly persistent.\n"
        "Do NOT explain, evaluate, or coach.\n"
        "Only reply as the character would."
    )

    user_prompt = f"""
Context:
{scenario['context']}

Your role:
{scenario['ai_role']}

What the user said:
"{user_response}"

Respond as the character with a short, realistic pushback.
"""

    return system_prompt, user_prompt

# Prompt B - Evaluation Engine
def evaluation_prompt(scenario, final_response):
    system_prompt = (
        "You are an evaluator of professional communication.\n"
        "You assess responses calmly and practically.\n"
        "You do not moralize or judge personality.\n"
        "Focus only on the response quality."
    )

    user_prompt = f"""
Scenario:
{scenario['context']}

User's final response:
"{final_response}"

Evaluate the response on these traits:
- Assertiveness
- Empathy
- Clarity
- Self-Respect
- Emotional Control

Rules:
- Each trait must be scored: +2, +1, 0, -1, or -2
- Give ONE clear strength
- Give ONE clear improvement suggestion

Return the output in EXACTLY this format:

Trait Scores:
Assertiveness: <score>
Empathy: <score>
Clarity: <score>
Self-Respect: <score>
Emotional Control: <score>

Feedback:
Strength: <one sentence>
Improvement: <one sentence>
"""

    return system_prompt, user_prompt

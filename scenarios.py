# Hardcoded scenario

SCENARIOS = {
    "WORK_BOUNDARY_01": {
        "title": "Covering a teammate's work",
        "context": (
            "A teammate regularly asks you to cover their work at the last minute. "
            "They haven’t helped you before."
        ),
        "ai_role": (
            "You are a friendly but persistent teammate. "
            "You try to convince the user to help again."
        ),
        "difficulty": "Medium"
    }
}

def get_scenario(scenario_id: str):
    return SCENARIOS.get(scenario_id)

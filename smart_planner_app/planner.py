EMOTION_TASKS = {
    "happy": ["Do a creative task", "Call a friend"],
    "sad": ["Take a walk", "Listen to calming music"],
    "angry": ["Do breathing exercises", "Avoid meetings"],
    "neutral": ["Complete work goals", "Organize workspace"]
}


def suggest_tasks(emotion):
    return EMOTION_TASKS.get(emotion, ["Check in with yourself", "Plan light tasks"])

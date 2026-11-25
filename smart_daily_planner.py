# smart_planner_app/planner.py
EMOTION_TASKS = {
    "happy": ["Do a creative task", "Call a friend"],
    "sad": ["Take a walk", "Listen to calming music"],
    "angry": ["Do breathing exercises", "Avoid meetings"],
    "neutral": ["Complete work goals", "Organize workspace"]
}

def suggest_tasks(emotion):
    return EMOTION_TASKS.get(emotion, ["Check in with yourself", "Plan light tasks"])

# smart_planner_app/README.md
"""
# Emotion-Based Task Planner

Suggests daily activities based on detected or user-input mood.

## Example:
```python
print(suggest_tasks("happy"))
```
"""
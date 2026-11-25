"""Tests for the emotion-based task planner."""

from smart_planner_app.planner import EMOTION_TASKS, suggest_tasks


def test_known_emotion_returns_tasks():
    assert suggest_tasks("happy") == EMOTION_TASKS["happy"]


def test_unknown_emotion_returns_fallback():
    assert suggest_tasks("confused") == ["Check in with yourself", "Plan light tasks"]


def test_every_mapping_is_a_non_empty_list_of_strings():
    for emotion, tasks in EMOTION_TASKS.items():
        assert isinstance(tasks, list) and tasks
        assert all(isinstance(task, str) and task for task in tasks), emotion

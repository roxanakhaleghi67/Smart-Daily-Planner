# Emotion-Based Task Planner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Suggests daily activities based on a detected or user-provided mood.

## Features

- Maps a mood to a short list of suggested tasks
- Covers `happy`, `sad`, `angry`, and `neutral`
- Falls back to a gentle suggestion for unrecognized moods
- Pure Python — no external dependencies or model downloads
- Works with either a detected emotion or one entered by the user

## Requirements

- Python 3.6 or newer
- Standard library only (no third-party packages)

## Installation

```bash
pip install -r requirements.txt
```

No third-party dependencies are needed, so this step is only required if you add your own to `requirements.txt`.

## Usage

The repository contains a single source module that defines `suggest_tasks`. Import it and call it with a mood:

```python
from planner import suggest_tasks

print(suggest_tasks("happy"))
# ['Do a creative task', 'Call a friend']

print(suggest_tasks("angry"))
# ['Do breathing exercises', 'Avoid meetings']

print(suggest_tasks("unknown"))
# ['Check in with yourself', 'Plan light tasks']
```

> **Note:** Mood keys are matched exactly as written in the `EMOTION_TASKS` table (`"happy"`, `"sad"`, `"angry"`, `"neutral"`). Extend the table to add more moods or tasks.

## Project Structure

```text
Smart-Daily-Planner/
├── Smart Daily Planner.py   # suggest_tasks and EMOTION_TASKS mapping
├── requirements.txt
└── README.md
```

## License

This project is released under the **MIT License**.

## Author

**Roxana Khaleghi**

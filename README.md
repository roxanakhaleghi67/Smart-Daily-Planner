# Emotion-Based Daily Planner

Suggests daily activities that fit a person's current mood, using a small rule table.

## What it does

`smart_daily_planner.py` maps four moods — `happy`, `sad`, `angry`, `neutral` — to short
task suggestions and returns a sensible fallback for any other input.

```python
from smart_daily_planner import suggest_tasks

print(suggest_tasks("happy"))
# -> ["Do a creative task", "Call a friend"]
```

## Requirements

Python 3.9+. The module uses only the standard library, so there is nothing to install.

## Notes and limitations

- The suggestions are static rules authored by hand, not a trained model.
- The mood must be supplied by the caller; no automatic mood detection is included.

## Status

Single-module prototype. Planned work: richer task sets, time-of-day awareness and a small
web form.

## License

No license file is present yet. Until one is added, the default copyright applies.

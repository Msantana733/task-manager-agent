from datetime import date, timedelta
import httpx
from auth import get_auth_headers

TICKTICK_API_BASE = "https://api.ticktick.com/api/v2"


def get_due_tasks() -> dict:
    """Fetch tasks grouped by due date: overdue, today, and this week."""
    response = httpx.get(
        f"{TICKTICK_API_BASE}/batch/check/0",
        headers=get_auth_headers(),
    )
    response.raise_for_status()
    data = response.json()

    today = date.today()
    week_end = today + timedelta(days=7)

    overdue, due_today, due_this_week = [], [], []

    for task in data.get("syncTaskBean", {}).get("update", []):
        due_str = task.get("dueDate", "")
        if not due_str:
            continue
        due = date.fromisoformat(due_str[:10])
        entry = {"title": task.get("title"), "due": str(due), "id": task.get("id")}
        if due < today:
            overdue.append(entry)
        elif due == today:
            due_today.append(entry)
        elif due <= week_end:
            due_this_week.append(entry)

    return {"overdue": overdue, "due_today": due_today, "due_this_week": due_this_week}

#!/usr/bin/env python3
"""PostToolUse hook: run `graphify update .` once each time a user story is fully done.

Trigger: an Edit/Write/MultiEdit to a tasks.md file leaves a "## Phase N: User Story ..."
block with every checkbox ticked. Each completed story is recorded in a state file, so the
graph is rebuilt once per story, not on every edit.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

GRAPHIFY = os.path.expanduser("~/.local/bin/graphify")
STATE_NAME = ".graphify-us-done.json"
PHASE_RE = re.compile(r"^##\s+Phase\s+[^:]*:\s*(User Story[^\n(]*)", re.MULTILINE)
TASK_RE = re.compile(r"^\s*-\s\[( |x|X)\]\s", re.MULTILINE)


def completed_stories(text):
    """Return {story title: True} for every User Story phase whose tasks are all ticked."""
    done = {}
    headers = list(PHASE_RE.finditer(text))
    for i, m in enumerate(headers):
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        # stop at the next top-level "## " heading so later phases are not counted
        nxt = re.search(r"^## ", text[m.end():end], re.MULTILINE)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():end]
        boxes = TASK_RE.findall(body)
        if boxes and all(b.lower() == "x" for b in boxes):
            done[m.group(1).strip()] = True
    return done


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    file_path = (payload.get("tool_input") or {}).get("file_path") or ""
    if not file_path.endswith("tasks.md"):
        return 0
    project = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()
    tasks = Path(file_path)
    if not tasks.is_file():
        return 0

    done_now = completed_stories(tasks.read_text(encoding="utf-8"))
    if not done_now:
        return 0

    state_path = project / "graphify-out" / STATE_NAME
    state = {}
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except Exception:
            state = {}
    seen = set(state.get(str(tasks), []))
    new = [s for s in done_now if s not in seen]
    if not new:
        return 0

    result = subprocess.run([GRAPHIFY, "update", "."], cwd=project,
                            capture_output=True, text=True)
    if result.returncode != 0:
        msg = (result.stderr or result.stdout).strip().splitlines()[-1:] or ["unknown error"]
        print(f"graphify update failed: {msg[0]}", file=sys.stderr)
        return 0  # do not block the edit

    state[str(tasks)] = sorted(seen | set(new))
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"graphify updated after user story done: {', '.join(new)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

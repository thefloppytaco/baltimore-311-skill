# Baltimore 311 — a teachable Muse skill

Teaches Muse how to file Baltimore City 311 service requests and track their
status, so anyone with Muse can do it in one conversation.

## Install

Copy this folder into your Muse workspace at `~/workspace/custom-skills/baltimore-311/`.
Muse picks it up automatically. No API keys, no login, nothing to configure.

## What it teaches

- **Filing** — the city's 311 portal flow (guest, no account), the exact
  questions for 10 common request types (pothole, missed trash, bulk trash,
  graffiti, street light, damaged cart, sidewalk, dirty street/alley, storm
  drain), and the gotchas (contact email is required for every type except
  missed trash; the graffiti flow redirects; bulk trash adds a scheduling step).
- **Tracking** — `scripts/check_status.py` reads the city's public 311 data
  feed and prints a request's live status, agency, due date, and last activity.
  Usage: `python3 scripts/check_status.py 26-00965493`

## Contents

- `skill.yaml` — skill metadata
- `SKILL.md` — the playbook
- `references/request-types.md` — verified per-type questions, portal search
  terms, departments, and resolution estimates (verified against the live
  portal 2026-10-15)
- `scripts/check_status.py` — status lookup via the public ArcGIS 311 layer

Built from a real filing workflow. Baltimore City's 311 data is public;
filing happens on the city's official portal.

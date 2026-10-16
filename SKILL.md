# Baltimore 311

## Purpose
File Baltimore City 311 service requests and track their status. Filing goes through the city's web portal in a browser task. Status checks use the city's public data feed and need no login.

## File a service request

- Operate the portal with `browser.spawn_task` at `https://balt311.baltimorecity.gov/citizen/s/`. The guest flow needs no account and has five screens: photo upload, location, type questions, contact, review.

- Before filing, confirm the request type, the street address, the answers to that type's questions, a contact name and email, and a photo when the user has one. A pasted "filing request for Muse" message already carries all of these.

- On the portal, type the request type in the "Submit a 3-1-1 Service Request" search box, open the result, and click Request This Service. Use the search terms in `references/request-types.md`.

- Skip the photo upload screen unless the user gave you a photo. If they did, pass it to the browser task in `files` so it can attach it.

- On the location screen, type the address and click the suggestion dropdown. The Continue button stays disabled until a suggestion is selected.

- Answer the type's questions from `references/request-types.md`. Some types show conditional follow-ups and one type adds a scheduling step; the reference lists them.

- On the contact screen, enter the user's name and email. Email is required for every type except missed trash pickup. Never click "Register and Submit"; use the guest "Submit Request" button unless the user asked for a portal account.

- Report the SR number back exactly as the portal shows it, for example 26-00965493.

## Track a request's status

- Run `scripts/check_status.py` with one or more SR numbers: `python3 ~/workspace/custom-skills/baltimore-311/scripts/check_status.py 26-00965493`.

- The script reads the city's public ArcGIS 311 layer. No key or login is needed. It prints status, type, agency, address, filed and due dates, last activity, and outcome.

- SR numbers look like 26-00965493. Accept them with or without the dash.

- The feed refreshes daily. A request filed today usually appears tomorrow; say that instead of calling it missing.

- Present the status plainly with the due date. Flag when a request is past due.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [Baltimore 311 portal](https://balt311.baltimorecity.gov/citizen/s/) for filing requests. Carry into the browser task: the request type and its portal search term, the street address, the answers to the type's questions, the contact name and email, and any photo as a file grant. Verify the SR number on the confirmation screen before reporting it.

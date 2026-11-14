# Week 4 — INVEST Check and Planning Poker Record

**Team 7 — FocusPulse** · Study Streak & Pomodoro Tracker · Section: Group 2


Roles in the Planning Poker session: **Product Owner** Bavly Romany Nabih (reads stories, does not vote) · **Scrum Master** Nicole Aziz (runs the room, keeps time, reveals votes — votes are cast by the three Developers) · **Voting Developers** Mina Ehab, David Gerges, David Albert.
Vote order in the tables below: Mina, David G., David A.
Reference story: **S10 "Log out" = 2 points** (every other story is sized relative to it).

---

## 1. Product Backlog (ordered by the Product Owner)

| ID | Jira | Epic | Story (short) | Points | Release | Owner |
|----|------|------|---------------|:-----:|---------|-------|
| S01 | AP-6 | E1 Account & Goals | Register and log in | 3 | MVP | Bavly |
| S02 | AP-7 | E2 Pomodoro Timer | Add my courses | 2 | MVP | Mina |
| S03 | AP-8 | E2 Pomodoro Timer | Start a 25-min focus session for a course | 5 | MVP | Nicole |
| S04 | AP-9 | E2 Pomodoro Timer | Cancel a session — interrupted sessions do not count | 3 | MVP | Mina |
| S05 | AP-10 | E1 Account & Goals | Set a daily goal (number of sessions) | 2 | MVP | Nicole |
| S06 | AP-11 | E3 Focus Log & Streak | See my current streak | 5 | MVP | Mina |
| S07 | AP-12 | E2 Pomodoro Timer | Automatic 5-minute break after a focus session | 3 | MVP | Nicole |
| S08 | AP-13 | E3 Focus Log & Streak | See my daily log of focus minutes per course | 5 | MVP | David A. |
| S09 | AP-14 | E3 Focus Log & Streak | Streak resets to zero after a missed day | 3 | MVP | David A. |
| S10 | AP-15 | E1 Account & Goals | Log out | 2 | MVP | David A. |
| S11 | AP-16 | E4 Study Groups | Create a study group and get an invite code | 5 | MVP | David G. |
| S12 | AP-17 | E4 Study Groups | Join a study group with an invite code | 3 | MVP | Bavly |
| S13 | AP-18 | E4 Study Groups | See my group's weekly total of focus minutes | 5 | MVP | David G. |
| S14 | AP-19 | E4 Study Groups | Set and track a weekly group challenge | 5 | MVP | Bavly |
| S15 | AP-20 | E1 Account & Goals | Reset my password | 3 | Later | Nicole |
| S16 | AP-21 | E3 Focus Log & Streak | Streak uses my local time zone and handles midnight | 5 | Later | Mina |
| S17 | AP-22 | E5 Insights & Motivation | Weekly statistics chart | 5 | Later | David A. |
| S18 | AP-23 | E5 Insights & Motivation | Badges for streak milestones | 5 | Later | David G. |
| S19 | AP-24 | E5 Insights & Motivation | Distraction notes during a session | 3 | Later | Bavly |
| | | | **Total** | **72** | | |

Jira project AP: epics AP-1 to AP-5, stories AP-6 to AP-24. Team: Product Owner Bavly Romany Nabih · Scrum Master Nicole Aziz · Developers Mina Ehab, David Gerges, David Albert. Story owners are the Jira assignees (David Albert appears in Jira as "David Alber") (14 / 13 / 15 / 15 / 15 points for Bavly / Nicole / Mina / David G. / David A.). Full story text ("As a … I want … so that …") is in Jira; the top 6 with acceptance criteria are in `stories.md`.

---

## 2. INVEST check

I = Independent · N = Negotiable · V = Valuable · E = Estimable · S = Small · T = Testable. ✅ = passes, ⚠️ = gap found and fixed. Reviewer (teammate who did not write the epic): E1 Mina · E2 David G. · E3 Bavly · E4 David A. · E5 Nicole (each reviewer did not write stories in that epic)

| Story | I | N | V | E | S | T | Fix needed |
|-------|:-:|:-:|:-:|:-:|:-:|:-:|------------|
| S01 Register and log in | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S02 Add my courses | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S03 Start a focus session | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | Needs S02 (courses). Order S02 before S03 in the backlog. |
| S04 Interrupted session does not count | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | Needs S03 (a running timer). Kept as its own story because it is the key rule; order after S03. |
| S05 Set a daily goal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S06 See my current streak | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | First version was "streak with reset and time zones" — too big. Split with SPIDR (Rules): S06 streak grows, S09 reset after missed day, S16 time zone/midnight. |
| S07 Automatic 5-minute break | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S08 Daily log per course | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | "Log" was vague; fixed to "focus minutes per course per day" so it is testable. |
| S09 Streak resets after a missed day | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | Depends on S06; ordered after it. |
| S10 Log out | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — (reference story = 2) |
| S11 Create a study group | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S12 Join a study group | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | Needs S11 (a group must exist); ordered after it. |
| S13 Group weekly total | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | Needs S11/S12 and focus data; ordered after them. |
| S14 Weekly group challenge | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ | "Motivating challenge" was untestable. Rewritten: one target (focus minutes) per group per week with a progress bar. |
| S15 Reset my password | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S16 Time zone and midnight handling | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | Unsure how the browser reports time zones — add a short spike before the Sprint if it is pulled in. |
| S17 Weekly statistics chart | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| S18 Badges for streak milestones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Milestones fixed to 3, 7 and 30 days. |
| S19 Distraction notes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

---

## 3. Planning Poker record

Rules used: Fibonacci deck · PO does not vote · secret vote, reveal together · all votes within one step → discuss and agree · wide spread → highest and lowest explain, re-vote · max 3 rounds · 13 or more → split.

Votes are listed in the order Mina, David G., David A. Final = value agreed by the team (the same value as in Jira).

| Story | Round 1 votes | Round 2 votes | Round 3 votes | Final | Key discussion point |
|-------|---------------|---------------|---------------|:-----:|----------------------|
| S10 Log out (reference) | 2, 2, 2 | — | — | 2 | Agreed as the reference story: one button that ends the session. |
| S01 Register and log in | 5, 3, 3 | — | — | 3 | Use a standard auth library; only e-mail + password (minimum 8 characters). |
| S02 Add my courses | 1, 2, 2 | — | — | 2 | Add courses only; editing and deleting are left out of the MVP. |
| S03 Start a focus session | 8, 5, 3 | 5, 5, 5 | — | 5 | The timer must keep correct time when the tab is in the background. |
| S04 Interrupted session does not count | 3, 3, 5 | 3, 3, 3 | — | 3 | Detecting a closed tab needs a status check on the next login. |
| S05 Set a daily goal | 2, 1, 2 | — | — | 2 | One number with validation (1–12 sessions). |
| S06 See my current streak | 8, 3, 5 | 5, 5, 5 | — | 5 | Counting consecutive days; midnight and time-zone cases moved to S16. |
| S07 Automatic 5-minute break | 3, 2, 3 | — | — | 3 | Same timer component as S03 with different settings. |
| S08 Daily log per course | 5, 8, 5 | — | — | 5 | Needs a grouped query per course and day, plus a page to show it. |
| S09 Streak resets after a missed day | 3, 5, 3 | — | — | 3 | Small logic, but needs many edge-case unit tests. |
| S11 Create a study group | 5, 3, 5 | — | — | 5 | Group table, owner, unique invite code. |
| S12 Join a study group with a code | 2, 3, 3 | — | — | 3 | Validate the code and block joining the same group twice. |
| S13 Group weekly total | 5, 8, 5 | — | — | 5 | Weekly aggregation across members; week starts on Saturday (PO decision). |
| S14 Weekly group challenge | 5, 5, 13 | 5, 8, 5 | 5, 5, 5 | 5 | PO decision: one focus-minutes target per group per week, set by the group owner, with a progress bar. |
| S15 Reset my password | 3, 2, 3 | — | — | 3 | Use a fake mail service for test data. |
| S16 Time zone and midnight | 5, 13, 5 | 5, 8, 5 | 5, 5, 5 | 5 | Short spike first on how the browser reports the time zone. |
| S17 Weekly statistics chart | 5, 5, 8 | — | — | 5 | Use a ready-made chart library. |
| S18 Badges for streak milestones | 3, 8, 5 | 5, 5, 5 | — | 5 | Three badges (3, 7 and 30 days) and a place to show them. |
| S19 Distraction notes | 2, 3, 3 | — | — | 3 | One text box and a list per session. |

**Result:** 19 stories estimated, total **72 points** (MVP S01–S14 = 51, later S15–S19 = 21). No story is 13 or more, so no split was needed (S06 was already split into S06, S09 and S16 during the INVEST check).

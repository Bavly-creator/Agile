# Week 4 — Top 6 User Stories with Acceptance Criteria

**Team 7 — FocusPulse** · Study Streak & Pomodoro Tracker · Section: Group 2
**Product Owner:** Bavly Romany Nabih · **Scrum Master:** Nicole Aziz · **Developers:** Mina Ehab, David Gerges, David Albert

Epics: **E1** Account & Goals · **E2** Pomodoro Timer · **E3** Focus Log & Streak · **E4** Study Groups · **E5** Insights & Motivation (stretch)

The six stories below are the top of the Product Backlog (ordered by the Product Owner). Jira project **AP** (Agile Project): S01 = AP-6 (Bavly), S02 = AP-7 (Mina), S03 = AP-8 (Nicole), S04 = AP-9 (Mina), S05 = AP-10 (Nicole), S06 = AP-11 (Mina). The same scenarios are in the Description of each Jira story.

---

## S01 — Register and log in  ·  Epic E1  ·  3 points

**As a** student, **I want** to register and log in with my e-mail and password **so that** my focus data is saved to my own account.

**Scenario: Successful registration and login**
- **Given** I am on the registration page
- **When** I enter a valid e-mail and a password of at least 8 characters and click "Register"
- **Then** my account is created and I am taken to my dashboard
- **And** the next time I enter the same e-mail and password on the login page I am logged in

**Scenario: Wrong password**
- **Given** I have a registered account and I am on the login page
- **When** I enter my e-mail with the wrong password
- **Then** I see the message "E-mail or password is incorrect"
- **And** I stay on the login page

**Scenario: E-mail already registered**
- **Given** an account exists for `sara@test.com`
- **When** I try to register again with `sara@test.com`
- **Then** I see "This e-mail is already registered"
- **And** no second account is created

---

## S02 — Add my courses  ·  Epic E2  ·  2 points

**As a** student, **I want** to add my courses to my account **so that** I can link every focus session to a course.

**Scenario: Add a course**
- **Given** I am logged in and on the "My courses" page
- **When** I type the course name "Agile Software Engineering" and click "Add"
- **Then** the course appears in my course list
- **And** it is available in the course drop-down on the timer page

**Scenario: Empty course name**
- **Given** I am on the "My courses" page
- **When** I click "Add" with an empty name
- **Then** I see "Course name is required"
- **And** no course is added

**Scenario: Duplicate course**
- **Given** "Agile Software Engineering" is already in my list
- **When** I add "Agile Software Engineering" again
- **Then** I see "You already have this course" and the list is unchanged

---

## S03 — Start a focus session for a course  ·  Epic E2  ·  5 points

**As a** student, **I want** to start a 25-minute Pomodoro timer linked to a course **so that** my focus time is recorded per course.

**Scenario: Complete a focus session**
- **Given** I am logged in and I have chosen the course "Agile Software Engineering"
- **When** I click "Start focus" and the 25-minute timer runs to 00:00
- **Then** a completed session of 25 minutes is saved for "Agile Software Engineering" with today's date
- **And** I see "Session complete"

**Scenario: No course selected**
- **Given** I am on the timer page and no course is selected
- **When** I click "Start focus"
- **Then** I see "Choose a course first"
- **And** the timer does not start

**Scenario: Only one timer at a time**
- **Given** a focus session is already running
- **When** I open the timer page in a second browser tab and click "Start focus"
- **Then** I see "A session is already running" and no second timer starts

---

## S04 — An interrupted session does not count  ·  Epic E2  ·  3 points

**As a** student, **I want** to cancel a running session and know it will not count **so that** my streak only reflects real focus time.

**Scenario: Cancel a running session**
- **Given** a focus session has been running for 10 minutes
- **When** I click "Cancel session" and confirm
- **Then** the timer stops and I see "Session cancelled — not counted"
- **And** my focus minutes for today stay the same as before the session

**Scenario: Close the page during a session**
- **Given** a focus session is running
- **When** I close the browser tab and do not return before the 25 minutes are over
- **Then** the session is marked "interrupted"
- **And** it is not added to my daily total

**Scenario: Dismiss the confirmation**
- **Given** I clicked "Cancel session"
- **When** I choose "Keep going" in the confirmation box
- **Then** the timer keeps running

---

## S05 — Set a daily goal  ·  Epic E1  ·  2 points

**As a** student, **I want** to set a daily goal of a number of focus sessions **so that** my streak grows only when I really study.

**Scenario: Set the goal**
- **Given** I am logged in and on the "Settings" page
- **When** I enter a daily goal of 2 sessions and click "Save"
- **Then** I see "Daily goal: 2 sessions"
- **And** my dashboard shows "0 / 2 sessions today"

**Scenario: Invalid goal**
- **Given** I am on the "Settings" page
- **When** I enter 0, a negative number or text and click "Save"
- **Then** I see "Goal must be a whole number from 1 to 12"
- **And** my previous goal is kept

**Scenario: Changing the goal mid-day**
- **Given** I have completed 2 sessions today and my goal is 3
- **When** I change my goal to 2
- **Then** the dashboard shows "2 / 2 sessions today — goal met"

---

## S06 — See my current streak  ·  Epic E3  ·  5 points

**As a** student, **I want** to see my current streak of days that met my daily goal **so that** I stay motivated to study every day.

**Scenario: Streak grows when the goal is met**
- **Given** my daily goal is 2 sessions and my streak is 3 days
- **When** I complete my second session today
- **Then** my streak shows 4 days

**Scenario: Goal not met yet**
- **Given** my daily goal is 2 sessions and I have completed 1 session today
- **When** I open the dashboard
- **Then** my streak still shows yesterday's value and the message "1 more session to keep your streak"

**Scenario: Interrupted sessions do not count**
- **Given** my daily goal is 2 sessions, I have 1 completed session and 1 interrupted session today
- **When** I open the dashboard
- **Then** today is not counted toward my streak

**Scenario: New user**
- **Given** I registered today and have no completed sessions
- **When** I open the dashboard
- **Then** my streak shows 0 days

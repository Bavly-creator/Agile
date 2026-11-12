# FocusPulse Week 4 User Stories

**Team:** 7 - FocusPulse  
**Idea:** Study Streak & Pomodoro Tracker  
**Section:** Group 2

> This file is a working draft generated from the assignment backlog supplied by the Product Owner. The team must validate the acceptance criteria before they are copied into Jira.

## E1 - Account & Goals

### S01 - Register and log in (3 points, MVP)
As a student, I want to register and log in so that my study data is private to me.

Acceptance criteria:

- Given a valid unused email and a valid password, when I submit registration, then an account is created and I can log in.
- Given valid credentials, when I submit the login form, then I am taken to my FocusPulse home screen.
- Given invalid credentials, when I try to log in, then I see an error and remain logged out.
- Password input is not displayed as plain text.

### S02 - Add my courses (2 points, MVP)
As a student, I want to add my courses so that I can organize my focus sessions by course.

Acceptance criteria:

- Given I am logged in, when I enter a non-empty course name and save it, then the course appears in my course list.
- A course name cannot be saved as blank.
- When I reopen my course list, previously saved courses are still present.

### S05 - Set daily goal (2 points, MVP)
As a student, I want to set a daily focus goal so that I can plan my study day.

Acceptance criteria:

- Given I am logged in, when I enter a positive goal and save it, then the goal is shown as today's target.
- The goal accepts only the supported unit and range defined by the product team.
- The saved goal remains visible after refreshing the page.

### S10 - Log out (2 points, reference story)
As a student, I want to log out so that nobody else can use my account on this device.

Acceptance criteria:

- Given I am logged in, when I select Log out, then my session ends.
- After logging out, protected pages require login again.

### S15 - Reset password (3 points)
As a student, I want to reset my password so that I can regain access if I forget it.

### S16 - Time zone and midnight (5 points)
As a student, I want streak dates to use my time zone so that midnight is calculated correctly.

## E2 - Pomodoro Timer

### S03 - Start focus session (5 points, MVP)
As a student, I want to start a focus session so that I can work for a measured period.

Acceptance criteria:

- Given a selected course and a valid duration, when I start a session, then the timer begins counting down.
- The active session shows the selected course and remaining time.
- I can see clearly that the session is active.

### S04 - Interrupted session does not count (3 points, MVP)
As a student, I want an interrupted session excluded from completed focus time so that my statistics remain accurate.

### S07 - Automatic 5-minute break (3 points, MVP)
As a student, I want a five-minute break to start automatically after a completed focus session so that I can rest.

## E3 - Focus Log & Streak

### S06 - See current streak (5 points, MVP)
As a student, I want to see my current streak so that I know how consistently I study.

Acceptance criteria:

- Given I have completed qualifying study days, when I open the home screen, then my current consecutive-day streak is displayed.
- The displayed number is updated after a qualifying session is completed.
- The streak display identifies the unit as days.

### S08 - Daily log per course (5 points, MVP)
As a student, I want a daily log per course so that I can review where I spent my study time.

### S09 - Streak resets after missed day (3 points, MVP)
As a student, I want a missed day to reset my streak so that the streak reflects consecutive study days.

### S17 - Weekly chart (5 points)
As a student, I want a weekly focus chart so that I can see my study pattern.

### S19 - Distraction notes (3 points)
As a student, I want to record distraction notes so that I can reflect on interruptions.

## E4 - Study Groups

### S11 - Create study group (5 points, MVP)
As a student, I want to create a study group so that I can study with classmates.

### S12 - Join group with code (3 points, MVP)
As a student, I want to join a group with a code so that I can participate in the correct study group.

### S13 - Group weekly total (5 points, MVP)
As a group member, I want to see the group's weekly total so that we can track shared progress.

### S14 - Weekly group challenge (5 points, MVP)
As a group member, I want a weekly group challenge so that the group has a shared target.

## E5 - Insights & Motivation

### S18 - Badges (5 points)
As a student, I want to earn badges so that milestones are recognized.

## Priority and release line

The supplied backlog places the MVP line after S14. Stories S01-S14 are labelled MVP; S15-S19 are stretch work.


# Habit Tracker

A simple, persistent command-line habit tracker built from scratch in Python.
Track daily habits, see your streaks, and never lose your progress between sessions.

Built as my Week 1 project on a 12-month plan to become an AI/ML Engineer.
The goal was to practice and demonstrate core Object-Oriented Programming concepts
in a small but complete application.

---

## Features

- Add new habits to track
- Mark habits as completed for today
- View all habits with their current streak
- Delete habits you no longer want to track
- Automatic save and load — your data persists between sessions via a JSON file
- Handles invalid input gracefully (no crashes on typos, duplicates, or missing habits)

---

## Concepts Practiced

- Object-Oriented Programming: classes, `__init__`, instance methods, `__str__`
- Class methods as alternative constructors (`from_dict`)
- File I/O with the `json` module
- Serialization and deserialization — converting custom objects to and from JSON
- The `datetime` module for date arithmetic and ISO-formatted date strings
- Defensive programming with `try/except` and input validation
- Designing clean class APIs — separating concerns between `Habit` and `HabitTracker`

---

## How to Run

Requires Python 3.8 or higher. No external libraries needed.

```bash
git clone https://github.com/sudith-holla/ai-ml-learning-journey.git
cd ai-ml-learning-journey/phase-1-foundations/week-1-python-oop/habit-tracker
python habit_tracker.py
```

On first run, no habits exist yet — pick option 1 to add your first one.
A `habits.json` file is created automatically and updated after every change.

---

## Sample Session

```
========================
     HABIT TRACKER
========================
1. Add a habit
2. Mark a habit as done
3. View all habits
4. Delete a habit
5. Quit
------------------------
Choose an option: 1
Please enter the habit name: Drink water

Choose an option: 2
Please enter the habit you completed today: Drink water

Choose an option: 3
---> Drink water, Streak: 1
```

---

## Project Structure

```
habit-tracker/
├── habit_tracker.py    Main file with Habit, HabitTracker, and menu loop
├── habits.json         Auto-generated data file (created on first save)
└── README.md           This file
```

---

## What's Next

Planned improvements for future iterations:

- [ ] `RecurringHabit` subclass for habits with custom schedules (e.g. gym Mon/Wed/Fri)
- [ ] Add historical habits with past start dates (`Habit.from_history`)
- [ ] Mark habits as done on past dates (for catching up)
- [ ] Display weekly and monthly completion stats
- [ ] Better terminal formatting and color-coded output

---

## What I Learned

The trickiest part was the streak calculation — figuring out how to count
consecutive completed days, anchored on today, while handling all the edge cases:
today not done but yesterday was, gaps in the middle, empty lists, and so on.
Walking through the logic on paper before writing any code made it far easier
than trying to figure it out in my head.

The most satisfying part was getting persistence working — closing the program,
reopening it, and seeing all my habits still there with the right streaks. That's
when it stopped feeling like a toy and started feeling like a real application.

---

*Built during Week 1 of my 12-month AI/ML Engineer roadmap — June 2026*
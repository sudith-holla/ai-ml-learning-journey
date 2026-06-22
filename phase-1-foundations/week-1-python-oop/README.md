# Week 1 — Python Refresh and Object-Oriented Programming

The first week of my 12-month AI/ML Engineer roadmap. The focus this week was on
refreshing core Python skills, with particular emphasis on Object-Oriented
Programming concepts that will be foundational for the months ahead.

---

## Goals for the Week

- Refresh Python OOP fundamentals: classes, instances, inheritance, methods
- Practice writing clean, modular, reusable code
- Get comfortable with Git and GitHub as part of a daily workflow
- Build at least one small, complete project that exercises these concepts end-to-end

---

## Resources Used

- **Corey Schafer's Python OOP Tutorial Series** (YouTube, 6 videos)
- **Real Python — "Object-Oriented Programming (OOP) in Python 3"**
- **Python official documentation** for `datetime`, `json`, and `os`

---

## Topics Covered

- Classes and instances
- `__init__` and instance attributes
- Instance methods, class methods, static methods
- Inheritance and method overriding
- Special methods like `__str__` and `__repr__`
- Property decorators (light touch — to revisit later when needed)
- File I/O with `json` and basic error handling with `try/except`

---

## Folder Contents

```
week-1-python-oop/
├── oop-notes.ipynb     Annotated notebook with OOP concepts and exercises
├── habit-tracker/      End-of-week project: a persistent CLI habit tracker
└── README.md           This file
```

---

## Project: Habit Tracker

A command-line habit tracker built from scratch to apply everything learned this
week — classes, class methods, file persistence with JSON, and clean separation
of concerns between the `Habit` and `HabitTracker` classes.

See [habit-tracker/README.md](./habit-tracker/README.md) for details.

---

## Reflections

OOP felt familiar from my undergraduate studies, but actually *using* it to build
something from scratch — making real design decisions about which class owns
which data, where validation belongs, when to use a class method versus a regular
method — was a different experience entirely. Reading about a concept and applying
it in a real project are two very different things.

The biggest lessons from this week:

- **Scan first, act after** — a common pattern for any "search the list" operation.
  Writing this incorrectly was the source of multiple bugs in my code.
- **Keep dirty inputs at the edges** — parse and validate user input at the boundary
  (the menu loop), and let internal code work only with clean, valid data.
- **Defensive programming pays off** — wrapping risky operations in `try/except`
  and validating inside class methods (not just at the input layer) prevents bugs
  from propagating.
- **Build incrementally, test as you go** — writing the entire project before
  running anything is a recipe for spending hours debugging. Build one method,
  test it, move on.

---

*Week 1 of 52. June 2026.*
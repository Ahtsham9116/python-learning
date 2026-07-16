# 🦁 Zoo Management System

A console-based **Zoo Management System** built in Python to demonstrate **inheritance, polymorphism, and method overriding** through a multi-level class hierarchy of animals.

---

## 🧠 Overview

This project simulates managing a zoo's animal collection through a menu-driven terminal interface. Unlike a flat data model, it's built around a proper **class hierarchy** — a base `Animal` class extended by category classes (`Mammal`, `Bird`, `Reptile`), which are further extended by specific species (`Lion`, `Elephant`, `Parrot`, `Chicken`, `Snake`). Each species overrides shared behavior (like `make_sound()`) with its own implementation, and the zoo can dispatch species-specific actions dynamically using `isinstance()` checks.

---

## ✨ Features

- **Add Animal** — Guided creation flow: choose a species type, then enter validated details (name, age, health, and species-specific traits like fur color, wing span, or venom status).
- **Remove Animal** — Remove an animal from the zoo by name.
- **Search Animal** — Find an animal by name (case-insensitive) and display its full info.
- **Display All Animals** — List every animal currently in the zoo with formatted details.
- **Feed Animal** — Trigger the shared `eat()` behavior for a specific animal.
- **Make Animal Sound** — Trigger each animal's overridden `make_sound()` (Lions roar, Elephants trumpet, Parrots squawk, Chickens cluck, Snakes hiss).
- **Animal Activity** — Trigger a species-specific special action (hunting, spraying water, repeating words, venom warning) based on the animal's actual type.
- **Exit** — Safely close the program.

---

## 🏗️ Project Structure & Design

### Class Hierarchy

```
Animal (name, age, specie, health)
├── Mammal (+ fur_color)
│   ├── Lion        → hunt(), make_sound() = "Roaring"
│   └── Elephant    → spray_water(), make_sound() = "Trumpet!"
├── Bird (+ wing_span)
│   ├── Parrot      → repeat_words(), make_sound() = "Squaw!"
│   └── Chicken     → fly() disabled, make_sound() = "Cluck"
└── Reptile (+ is_venomous)
    └── Snake       → dangerous(), make_sound() = "Hiss!"
```

- **`Animal`** — base class with shared attributes and behaviors: `display_info()`, `eat()`, `sleep()`, `make_sound()`.
- **`Mammal` / `Bird` / `Reptile`** — intermediate classes that add category-specific attributes and extend `display_info()` via `super()`.
- **Concrete species classes** — override `make_sound()` (polymorphism) and add their own unique method (e.g. `hunt()`, `spray_water()`, `dangerous()`).

### `Zoo`
Manages the collection as a list of `Animal` objects:
- `add_animal()`, `remove_animal()`, `search_animal()`, `display_all_animals()`, `feed_animal()`, `make_animal_sound()` — core management operations
- `animal_activity()` — uses `isinstance()` to call the correct species-specific method
- `find_animal(name)` — case-insensitive lookup helper

### Input Validation Helpers
- `get_non_empty_input()` — re-prompts until a non-empty value is given
- `get_positive_number()` — re-prompts until a valid positive float is given
- `get_valid_health()` — restricts health status to `Healthy / Good / Fair / Bad`, case-insensitive, normalized to the correct casing
- `create_animal_from_input()` — guided flow that builds the right subclass instance based on user's species choice

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Dependencies:** None — uses only the Python standard library
- **Storage:** In-memory (data resets each time the program is run — no database or file persistence yet)

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Ahtsham9116/python-learning.git

# Navigate to the repository root
cd python-learning

# Move into this mini project folder
cd mini_projects/05-zooManagementSystem_project

# Run the program
python zoo_management_system.py
```

**Requirements:** Python 3.6 or higher (no external packages needed).

---

## 📋 Example Menu

```
============================================
           Welcome to the Zoo          
============================================
	1. Add Animal
	2. Remove Animal
	3. Search Animal
	4. Display All Animals
	5. Feed Animal
	6. Make Animal Sound
	7. Animal Activity
	8. Exit
============================================
```

---

## 🔮 Possible Future Improvements

- Persist zoo data using a file (JSON/CSV) or a database (SQLite)
- Add more species and categories (e.g. Fish, Insects)
- Track feeding schedules and health check history over time
- Add unit tests for each class's behavior
- Build a GUI (Tkinter) or web version (Flask)

---

## 👤 Author

**Muhammad Ahtsham Javed**
Part of the [python-learning](https://github.com/Ahtsham9116/python-learning) repository — a collection of Python mini projects built while learning core programming and OOP concepts.

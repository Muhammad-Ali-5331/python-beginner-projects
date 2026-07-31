# Python Beginner Projects

A collection of eight Python projects covering core concepts — CLI apps, OOP, GUI with Tkinter, browser automation with Selenium, and API integration. Each project is self-contained and runnable independently.

---

## Projects

### 1. ☕ Coffee Machine (Procedural)
A terminal-based coffee vending machine simulation. Manages water, milk, and coffee inventory, accepts coin input, and gives change.

**Concepts:** functions, global state, dictionaries, loops  
**Run:** `python main.py`

**Commands:** `espresso` / `latte` / `cappuccino` → insert coins → get coffee  
`report` → view remaining resources | `off` → shutdown

```
Coffee Menu: (espresso/latte/cappuccino)
Get the info about resources available: (report)
Turn Off the Machine: (off)
```

**Files:**
```
Coffee Machine/
├── main.py     # Core logic — coin input, resource checking, dispensing
└── menu.py     # Menu items, prices, ingredients, ASCII art display functions
```

---

### 2. ☕ OOP Coffee Machine
The same coffee machine rebuilt entirely with OOP — clean separation of concerns across three classes.

**Concepts:** classes, encapsulation, method delegation  
**Run:** `python main.py`

**Files:**
```
OOP Coffee Machine/
├── main.py           # Entry point — orchestrates the three classes
├── menu.py           # MenuItem and Menu classes
├── coffee_maker.py   # CoffeeMaker — resource management and dispensing
└── money_machine.py  # MoneyMachine — coin processing and payment validation
```

**Class responsibilities:**

| Class | Responsibility |
|---|---|
| `Menu` | Stores drink options, finds drinks by name |
| `CoffeeMaker` | Tracks resources, checks availability, makes coffee |
| `MoneyMachine` | Processes coins, validates payment, gives change, tracks profit |

---

### 3. 🧠 Quiz Game (CLI)
A True/False trivia quiz that runs in the terminal. Questions are hardcoded in `data.py`.

**Concepts:** OOP, list comprehension, class interaction  
**Run:** `python main.py`

**Files:**
```
Quiz Game/
├── main.py             # Builds question bank, runs quiz loop
├── question_model.py   # Question class (text + answer)
├── quiz_brain.py       # QuizBrain — tracks score, prompts questions, checks answers
└── data.py             # 20 hardcoded True/False questions
```

---

### 4. 🖥️ The Quizzler App (GUI)
The Quiz Game rebuilt as a **Tkinter GUI app** with live score tracking, color feedback (green/red), and questions fetched from the [Open Trivia Database API](https://opentdb.com/).

**Concepts:** Tkinter, OOP, REST API, `html.unescape()`  
**Install:** `pip install requests`  
**Run:** `python main.py`

**Files:**
```
The Quizzler App/
├── main.py             # Entry point
├── ui.py               # QuizInterface — Tkinter window, buttons, canvas
├── quiz_brain.py       # QuizBrain — question flow and answer checking
├── question_model.py   # Question class
├── data.py             # Fetches 10 True/False questions from Open Trivia DB API
├── true.png            # True button image
└── false.png           # False button image
```

> **Note:** `ui.py` has a bug — the False button's `command` incorrectly passes `"True"` instead of `"False"`. Fix: `command=lambda: self.check_answer("False")`.

---

### 5. 🔄 Miles to Km Converter (GUI)
A Tkinter unit converter supporting **14 unit types** across distance, weight, and volume categories. Smart dropdowns filter out invalid conversions (e.g., miles → kg is disabled).

**Concepts:** Tkinter, OOP, dictionary dispatch, invalid-pair filtering  
**Run:** `python main.py`

**Supported conversions:**

| Category | Units |
|---|---|
| Distance | Miles, Km, Meters, Cm, Feet, Inch, Yards |
| Weight | Lb, Gram, Kg, Ounces |
| Volume | Liters, Milliliters, Gallons |

**Files:**
```
Miles to Km Converter/
├── main.py       # Tkinter GUI — two dropdowns, input field, Calculate button
└── functions.py  # Functions class — 60+ conversion methods + invalid-pair filtering
```

---

### 6. 🔤 NATO Alphabet Converter
Converts any word into its NATO phonetic alphabet equivalent (e.g., `HELLO` → `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`).

**Concepts:** pandas, dictionary comprehension, recursion for error handling  
**Install:** `pip install pandas`  
**Run:** `python main.py`

**Files:**
```
NATO Alphabet Converter/
├── main.py                    # Reads CSV, builds dict, converts input word
└── nato_phonetic_alphabet.csv # Letter-to-code mapping
```

> **Note:** `main.py` contains a hardcoded absolute path (`E:/Courses/...`). Change it to a relative path before running: `pandas.read_csv("nato_phonetic_alphabet.csv")`.

---

### 7. 📊 Habit Tracker
Logs daily activity data (e.g. km cycled) to a personal graph on [Pixela](https://pixe.la/) — a pixel-art habit tracking service with a public API.

**Concepts:** `requests`, REST API (POST/PUT/DELETE), datetime formatting  
**Install:** `pip install requests`  
**Run:** `python main.py`

**What the script does:**
- Creates a Pixela user account
- Creates a graph (`graph1`) tracking kilometers cycled
- Has commented blocks for adding a pixel and editing/deleting a pixel by date

**Files:**
```
Habit Tracker/
└── main.py   # Full Pixela API workflow — create user, graph, add/edit/delete pixels
```

> **Note:** `main.py` contains a hardcoded `USER_NAME` (`deadkiller9932`) and `TOKEN` (`userForTesting`). Replace with your own Pixela credentials before running.

---

### 8. 🍪 The Cookie Clicker
A Selenium bot that plays [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) automatically — clicks the cookie as fast as possible and buys the most expensive affordable upgrade every 5 seconds. Runs for 5 minutes then prints the final cookies-per-second score.

**Concepts:** Selenium, time-based logic, CSS selectors  
**Install:** `pip install selenium`  
**Requires:** ChromeDriver matching your Chrome version  
**Run:** `python main.py`

**Files:**
```
The Cookie Clicker/
└── main.py   # Selenium bot — auto-click loop + timed purchase logic
```

---

## Setup

### Clone the repo

```bash
git clone https://github.com/Muhammad-Ali-5331/python-beginner-projects.git
cd python-beginner-projects
```

### Install dependencies

```bash
pip install requests pandas selenium
```

`tkinter` is included in the Python standard library. If it's missing on Linux:

```bash
sudo apt-get install python3-tk
```

### ChromeDriver (for Cookie Clicker)

Download from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) and add to PATH, or install automatically:

```bash
pip install webdriver-manager
```

---

## Concepts Covered

| Concept | Projects |
|---|---|
| Functions & loops | Coffee Machine |
| OOP & encapsulation | OOP Coffee Machine, Quiz Game, Quizzler App |
| Tkinter GUI | Miles to Km Converter, Quizzler App |
| REST APIs & `requests` | Quizzler App, Habit Tracker |
| pandas & CSV | NATO Alphabet Converter |
| Selenium automation | Cookie Clicker |

---

## Note

This project was built while learning Python. Some scripts may reference API keys, email credentials, or local file paths — replace placeholders with your own values (ideally via environment variables / a `.env` file) before running.

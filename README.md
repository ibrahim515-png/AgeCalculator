# Age Calculator

A Python-based command-line application that calculates a person's exact age in years, months, and days using their date of birth. It validates user input, categorizes age groups, and stores calculation results in a text file.

## Overview

Age Calculator is a beginner Python project focused on date calculations, input validation, error handling, and file operations.

The application uses Python's `datetime` module and the `relativedelta` function from `python-dateutil` to calculate age accurately in years, months, and days.

## Features

* **Date of Birth Input:** Accepts dates in `DD/MM/YYYY` format.
* **Input Validation:** Checks date formatting and validates calendar dates.
* **Future Date Validation:** Prevents users from entering future birth dates.
* **Age Calculation:** Calculates age in years, months, and days.
* **Age Classification:** Assigns one of five age categories:

  * Child (0–12)
  * Teenager (13–17)
  * Young Adult (18–35)
  * Adult (36–59)
  * Senior (60+)
* **File Storage:** Saves the calculated age and age category to `age.txt`.
* **Error Handling:** Handles invalid input, interrupted input, and file operation errors.

## Technologies Used

* Python 3
* `datetime`
* `python-dateutil`
* `relativedelta`

## Project Structure

```text
Age-Calculator/
│
├── age_calculator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

* Python 3 installed on your system.

### Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd Age-Calculator
```

3. Install the required dependency:

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python age_calculator.py
```

## Usage

Enter your date of birth using the following format:

```text
DD/MM/YYYY
```

Example input:

```text
28/10/2005
```

The application calculates your age, displays the corresponding age category, and saves the results to `age.txt`.

## Example Output

```text
Enter your birth date (DD/MM/YYYY): 28/10/2005

Your age is: [years] years, [months] months, and [days] days.
Your age category is: [category]
Age saved to age.txt successfully!
```

## Python Concepts Demonstrated

This project applies several fundamental Python programming concepts:

* Functions and modular code organization
* Conditional statements and control flow
* Loops and input validation
* Exception handling
* Date and time manipulation
* File handling and context managers
* External library integration

## Author

**Ibrahim Salah**

GitHub: [@ibrahim515-png](https://github.com/ibrahim515-png)

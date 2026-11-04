# Age Calculator

A Python command-line application that calculates a person's age based on their date of birth.

## Features

* Accepts birth dates in `DD/MM/YYYY` format.
* Validates date input and handles invalid dates.
* Rejects future birth dates.
* Calculates age in years, months, and days.
* Classifies age into five categories:

  * Child
  * Teenager
  * Young Adult
  * Adult
  * Senior
* Saves the calculated age and category to a text file.
* Handles input and file-related errors.

## Technologies Used

* Python 3
* `datetime`
* `python-dateutil` (`relativedelta`)

## Requirements

Install the required dependency:

```bash
pip install -r requirements.txt
```

## How to Run

Run the application using:

```bash
python age_calculator.py
```

## Input Format

Enter your date of birth using the following format:

```text
DD/MM/YYYY
```

Example:

```text
28/10/2005
```

## Example Output

```text
Enter your birth date (DD/MM/YYYY): 28/10/2005

Your age is: [years] years, [months] months, and [days] days.
Your age category is: [category]
Age saved to age.txt successfully!
```

The calculated age and category are saved in `age.txt`.

## Concepts Practiced

* Functions and code organization
* Conditional statements
* Loops
* Exception handling
* Date and time operations
* File handling
* Working with external Python libraries

## Author

Ibrahim Salah

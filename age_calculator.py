from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def get_birth_date():
    while True:
        try:
            birth_date = input("Enter your birth date (DD/MM/YYYY): ")
            birth_date_obj = datetime.strptime(
                birth_date, "%d/%m/%Y"
            ).date()

            if birth_date_obj > date.today():
                print("Error: Birth date cannot be in the future. Try again.")
                continue

            return birth_date_obj

        except ValueError:
            print(
                "Error: Invalid date. Please use DD/MM/YYYY "
                "and enter a valid date."
            )


def calculate_age():
    today = date.today()
    birth_date = get_birth_date()

    age = relativedelta(today, birth_date)

    age_years = age.years
    age_months = age.months
    age_days = age.days

    return age_years, age_months, age_days


def classify_age(years):
    if years < 13:
        return "Child"
    elif years < 18:
        return "Teenager"
    elif years < 36:
        return "Young Adult"
    elif years < 60:
        return "Adult"
    else:
        return "Senior"


def save_age(years, months, days, category):
    try:
        with open("age.txt", "w", encoding="utf-8") as file:
            file.write(
                f"Your age is {years} years, {months} months, "
                f"and {days} days.\n"
            )
            file.write(f"Your age category is: {category}\n")

    except OSError as error:
        print(f"Error: Could not save the file. Details: {error}")
        return False

    return True


def main():
    try:
        years, months, days = calculate_age()

        category = classify_age(years)

        print(
            f"Your age is {years} years, {months} months, "
            f"and {days} days."
        )
        print(f"Your age category is: {category}")

        if save_age(years, months, days, category):
            print("Age saved to age.txt successfully!")

    except EOFError:
        print("\nError: No input received. Exiting the program.")

    except KeyboardInterrupt:
        print("\nProgram cancelled by the user.")


if __name__ == "__main__":
    main()

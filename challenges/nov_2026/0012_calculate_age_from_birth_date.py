## raw findings, written in 19min52
from datetime import datetime, date

def what_s_your_age():
    your_birth_date = input("What is your birth date (YYYY-MM-DD): ")

    def calculate_age(birth_date: str) -> int:
        arranged_str = birth_date.strip().replace(" ", "")
        time_object = datetime.strptime(arranged_str, "%Y-%m-%d")
        today_date = date.today()

        diff_days = today_date - time_object

        return diff_days.days

    result_in_days = calculate_age(your_birth_date)
    result_in_years = round(result_in_days // 365.25, 0)

    remaining_days = result_in_days % 365.25

    result_in_months = remaining_days // 30.4

    final_remaining_days = remaining_days % 30.4

    print(f"You are around {result_in_years} years, {result_in_months} months, and {final_remaining_days} days")

    return


## testing
'what_s_your_age()'

# got an error: TypeError: unsupported operand type(s) for -: 'datetime.date' and 'datetime.datetime'


## refined version
def what_s_your_age_adj():
    birth_date = input("What is your birth date (YYYY-MM-DD): ")

    def calculate_age_in_days(birth_date: str) -> int:
        cleaned_date = birth_date.strip().replace(" ", "")
        birth_date_obj = datetime.strptime(cleaned_date, "%Y-%m-%d").date()
        today = date.today()

        difference = today - birth_date_obj

        return difference.days

    total_days = calculate_age_in_days(birth_date)

    years = int(total_days // 365.25)
    remaining_days = total_days % 365.25

    months = int(remaining_days // 30.4)
    days = int(remaining_days % 30.4)

    print(f"You are approximately {years} years, {months} months, and {days} days old.")


## testing again
what_s_your_age_adj()

# input = '1996-03-29'

# result is very accurate, although using mathematical logic:
'You are approximately 30 years, 7 months, and 18 days old.'


## solution from platform
from dateutil.relativedelta import relativedelta

def calculate_exact_age(birthdate_str):
    try:
        # Parse the input string
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        today = datetime.now().date()
        
        # Calculate the difference
        diff = relativedelta(today, birthdate)
        
        return f"{diff.years} years, {diff.months} months, {diff.days} days"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
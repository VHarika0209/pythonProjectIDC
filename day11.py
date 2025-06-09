import datetime

def calculate_month_year(year, month, day):
    joining_date = datetime.datetime(year, month, day)
    today_date = datetime.datetime.now()
    diff_days = abs(today_date - joining_date).days
    total_months = diff_days // 30
    months = total_months % 12
    years = total_months // 12
    return months, years

def calculate_experience():
    print("Experience Calculator ")
    try:
        role = input("Please enter your role: ").strip().title()
        try:
            input_date = input("Please enter your joining date (YYYY,MM,DD) : ")
            year, month, day = map(int,input_date.split(','))
        except ValueError:
            print("Please enter the date in correct format : (YYYY,MM,DD)")
            return
        months, years = calculate_month_year(year,month,day)
        experience_parts = []
        if years:
            experience_parts.append(f"{years} year{'s' if years != 1 else ''}")
        if months:
            experience_parts.append(f"{months} month{'s' if months != 1 else ''}")
        if experience_parts:
            experience_str = " and ".join(experience_parts)
            print(f"You have {experience_str} of experience as {role}.")
        else:
            print(f"You have less than a month of experience as {role}.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    calculate_experience()
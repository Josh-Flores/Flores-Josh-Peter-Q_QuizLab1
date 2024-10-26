from datetime import date

def get_zodiac_sign(month_of_birth, day_of_birth):
    if (month_of_birth == 'DECEMBER' and day_of_birth >= 22) or (month_of_birth == 'JANUARY' and day_of_birth <= 19):
        return "Capricorn"
    elif (month_of_birth == 'JANUARY' and day_of_birth >= 20) or (month_of_birth == 'FEBRUARY' and day_of_birth <= 18):
        return "Aquarius"
    elif (month_of_birth == 'FEBRUARY' and day_of_birth >= 19) or (month_of_birth == 'MARCH' and day_of_birth <= 20):
        return "Pisces"
    elif (month_of_birth == 'MARCH' and day_of_birth >= 21) or (month_of_birth == 'APRIL' and day_of_birth <= 19):
        return "Aries"
    elif (month_of_birth == 'APRIL' and day_of_birth >= 20) or (month_of_birth == 'MAY' and day_of_birth <= 20):
        return "Taurus"
    elif (month_of_birth == 'MAY' and day_of_birth >= 21) or (month_of_birth == 'JUNE' and day_of_birth <= 20):
        return "Gemini"
    elif (month_of_birth == 'JUNE' and day_of_birth >= 21) or (month_of_birth == 'JULY' and day_of_birth <= 22):
        return "Cancer"
    elif (month_of_birth == 'JULY' and day_of_birth >= 23) or (month_of_birth == 'AUGUST' and day_of_birth <= 22):
        return "Leo"
    elif (month_of_birth == 'AUGUST' and day_of_birth >= 23) or (month_of_birth == 'SEPTEMBER' and day_of_birth <= 22):
        return "Virgo"
    elif (month_of_birth == 'SEPTEMBER' and day_of_birth >= 23) or (month_of_birth == 'OCTOBER' and day_of_birth <= 22):
        return "Libra"
    elif (month_of_birth == 'OCTOBER' and day_of_birth >= 23) or (month_of_birth == 'NOVEMBER' and day_of_birth <= 21):
        return "Scorpio"
    elif (month_of_birth == 'NOVEMBER' and day_of_birth >= 22) or (month_of_birth == 'DECEMBER' and day_of_birth <= 21):
        return "Sagittarius"
    else:
        return "Error"

while True:
    surname = input("What's your last name? ").capitalize()
    first = input("Write your first name here: ").capitalize()
    middle = input("Any middle name? ").capitalize()
    id_code = input("Student ID, enter it here: ")
    residence = input("Where do you live? ").capitalize()

    full_identity = f"{surname}, {first} {middle}"
    print('')


    print("_____________________________________________")
    print("Put birthday details here")
    month_of_birth = input("What month were you born? ").upper()
    day_of_birth = int(input("And the day? "))
    year_of_birth = int(input("Finally, the year? "))

    this_year = date.today().year
    your_age = this_year - year_of_birth
    print("_____________________________________________")

    print("\nYour Name: ", full_identity)
    print("ID Code: ", id_code)
    print("Address: ", residence)
    print("Age: ", your_age)
    print(f"Birthday: {month_of_birth} {day_of_birth}, {year_of_birth}")

    sign = get_zodiac_sign(month_of_birth, day_of_birth)
    print("Your Zodiac Sign is:", sign)

    print("_____________________________________________")
    repeat = input("Wanna try again? (Y/N): ").upper()
    if repeat != 'Y':
        break
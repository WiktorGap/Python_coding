import re

arrMonth = {
    1: "Styczeń",
    2: "Luty",
    3: "Marzec",
    4: "Kwiecień",
    5: "Maj",
    6: "Czerwiec",
    7: "Lipiec",
    8: "Sierpień",
    9: "Wrzesień",
    10: "Październik",
    11: "Listopad",
    12: "Grudzień"
}

def calculateControlSum(user_input):
    val = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    controlSum = 0
    for i in range(len(val)):
        controlSum += val[i] * int(user_input[i])
    controlSum = (10 - (controlSum % 10)) % 10  

    if int(user_input[10]) != controlSum:
        print(f"Invalid control num (expected {controlSum}, got {user_input[10]})")
    else:
        print("Valid control num")

def validate(user_input):
    pesel_regex = re.compile(r"^\d{11}$")  
    if not pesel_regex.match(user_input):
        print("Invalid pesel format")
        return False
    calculateControlSum(user_input)
    
    return True

def makeDate(user_input):
    date = ""
    sex = ""
    month = ""
    year = ""


    month_code = int(user_input[2:4])
    if 1 <= month_code <= 12:
        year = "19" + user_input[0:2]
    elif 21 <= month_code <= 32:
        year = "20" + user_input[0:2]
        month_code -= 20
    elif 41 <= month_code <= 52:
        year = "21" + user_input[0:2]
        month_code -= 40
    elif 61 <= month_code <= 72:
        year = "18" + user_input[0:2]
        month_code -= 60
    else:
        print(f"Invalid month value: {month_code}. Change digits at positions 3 and 4.")
        return "Invalid Pesel in position 3 and 4"

    print(f"Final month: {month_code}")

    if int(user_input[9]) % 2 == 0:
        sex = "Kobieta"
    else:
        sex = "Mężczyzna"

    day = user_input[4:6]
    date = sex + " " + "Rok: " + year + " Miesiac: " + str(month_code) + " Dzień: " + str(day) + "\n"
    diffMonthFormat = arrMonth[month_code]
    diffDateFormat = "Nowy Format: " + sex + " " + str(day) + " " + diffMonthFormat + " " + year

    print(date)
    print(diffDateFormat)
    selectFormat(day, month_code, year, sex)

def selectFormat(day, month, year, sex):
    print("\nWybierz format daty:")
    print("1 - DD.MM.YYYY")
    print("2 - Dzień Miesiąc Rok")
    print("3 - Rok-Miesiąc-Dzień")
    choice = input("Wybór: ")
    
    if choice == "1":
        print(f"{sex}, {day}.{month:02}.{year}")
    elif choice == "2":
        print(f"{sex}, {day} {arrMonth[month]} {year}")
    elif choice == "3":
        print(f"{sex}, {year}-{month:02}-{day}")
    else:
        print("Niepoprawny wybór.")

userEndFlag = True
while userEndFlag:
    user_input = input("Enter pesel:").strip()

    if not validate(user_input):
        continue

    makeDate(user_input)

    userEndFlag = input("Jeśli chcesz zakończyć, wpisz 'false', w przeciwnym razie naciśnij dowolny klawisz: ").lower() != 'false'

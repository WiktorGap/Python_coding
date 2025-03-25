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

def validate(user_input):
    pesel_regex = re.compile(r"^\d{2}[0-9][0-9][0-3][0-9]\d{4}\d$")
    if len(user_input) != 11 or not pesel_regex.match(user_input):
        print("Invalid pesel format")
        return False
    return True

def makeDate(user_input):
    date = ""
    sex = ""
    month = ""
    year = ""
    if user_input[2] == "0" or user_input[2] == "1":
        year = "19" + user_input[0] + user_input[1]
    elif user_input[2] == "2" or user_input[2] == "3":
        year = "20" + user_input[0] + user_input[1]
    elif user_input[4] == "2" or user_input[5] == "1":
        year = "21" + user_input[0] + user_input[1]
    elif user_input[6] == "2" or user_input[7] == "1":
        year = "18" + user_input[0] + user_input[1]
    
    month = user_input[2:4]
    finalMonth = int(month) - 20

    if finalMonth not in arrMonth.keys():
        print(f"Invalid month value: {month}. Change digits at positions 3 and 4.")
        return "Invalid Pesel in position 3 and 4 "

    print(f"Final month: {finalMonth}")
    
    if int(user_input[9]) % 2 == 0:
        sex = "Kobieta"
    else:
        sex = "Mężczyzna"
    
    day = user_input[4:6]
    date = sex + " " + "Rok: " + year + " Miesiac: " + str(finalMonth) + " Dzień: " + str(user_input[4:6]) + "\n"
    diffMonthFormat = arrMonth[finalMonth]
    diffDateFormat = "Nowy Format: " + sex + " " + str(user_input[4:6]) + " " + diffMonthFormat + " " + year

    print(date)
    print(diffDateFormat)
    selectFormat(day, finalMonth, year, sex)

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

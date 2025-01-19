#give me the age
age = input("give me you age ")
# collect age data from user
data = input("chosse the months or days or weeks ").lower()
#the calculation of age
months = int(age) * 12
weeks = months * 4
days = int(age) * 365
#give the age of the user
if data == "months":
    print("tank you for choosing to calculate the month")
    print(f"you lived {months:} ")
if data == "days":
    print("tank you for choosing to calculate  the days")
    print(f"you lived {days:} ")
if data == "weeks":
    print("tank you for choosing to calculate the weeks")
    print(f"you lived {weeks:} ")
#the end of the program:)


from decimal import Decimal, InvalidOperation

class Calculator:
    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def addition(self):
        if self.numberTwo < 0:
            print(f"{self.numberOne} + ({self.numberTwo}) is {self.numberOne + self.numberTwo}")
        else:
            print(f"{self.numberOne} + {self.numberTwo} is {self.numberOne + self.numberTwo}")

    def substraction(self):
        if self.numberTwo < 0:
            print(f"{self.numberOne} - ({self.numberTwo}) is {self.numberOne - self.numberTwo}")
        else:
            print(f"{self.numberOne} - {self.numberTwo} is {self.numberOne - self.numberTwo}")

    def multiplication(self):
        if self.numberTwo < 0:
            print(f"{self.numberOne} * ({self.numberTwo}) is {self.numberOne * self.numberTwo}")
        else:
            print(f"{self.numberOne} * {self.numberTwo} is {self.numberOne * self.numberTwo}")        

    def devision(self):
        if self.numberTwo == 0:
            print("You can not devide by 0.")
        elif self.numberTwo < 0:
            print(f"{self.numberOne} / ({self.numberTwo}) is {self.numberOne / self.numberTwo}")
        else:
            print(f"{self.numberOne} / {self.numberTwo} is {self.numberOne / self.numberTwo}")    


# პირველი რიცხვის არჩევა
while True:
    # რიცხვის ვალიდაცია
    try:
        inputtedNumberOne = Decimal(input("Please enter your first number: "))
    except InvalidOperation:
        print("Please enter a valid number. Characters and special symbols are not allowed.")
        continue
    break

# მეორე რიცხვის არჩევა
while True:
    # რიცხვის ვალიდაცია
    try:
        inputtedNumbertwo = Decimal(input("Please enter your second number: "))
    except InvalidOperation:
        print("Please enter a valid number. Characters and special symbols are not allowed.")
        continue
    break

# ობიექტის შექმნა
func = Calculator(inputtedNumberOne, inputtedNumbertwo)

# მოქმედებების ცხრილი
print("1. add")
print("2. substract")
print("3. multiply")
print("4. devide")

# მოქმედების არჩევა
while True:
    # მოქმედების ვალიდაცია
    try:
        action = int(input("Please enter the id of the action you'd like to do: "))
    except ValueError:
        print("Please enter a valid id. Characters and special symbols are not allowed.")
        continue

    # მოქმედება
    if action == 1:
        func.addition()
        break
    elif action == 2:
        func.substraction()
        break
    elif action == 3:
        func.multiplication()
        break
    elif action == 4:
        func.devision()
        break
    else:
        print("Please choose a valid ID.")
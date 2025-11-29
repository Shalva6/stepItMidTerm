# კომპიუტერები ფლოატებს პირდაპირ ვერ აღიქვავენ და შენახვის დროს ცდილობენ რაც შეიძლება ახლოს იყონ
# წერტილის მარჯვნივ მყოფ რიცხვებთან. 0.65 ინახება როგორც 0.6499999..
# Decimal შემოგვაქვს რომ ეს 'მიახლოება' გავაქროთ და შევიტანოთ 0.65 ისე როგორც 0.65
from decimal import Decimal, InvalidOperation

class Bank:
    def __init__(self, balance):
        self.balance = str(balance)
        with open("bank/userBalance.txt", "a") as f:
            f.write(self.balance)
    
    def printMoney(self):
        with open("bank/userBalance.txt", "r") as f:
            currentBalanace = Decimal(f.read())
            currentBalanace = f"{currentBalanace:,.2f}"
            print(f"You have {currentBalanace}$ on your balance.")
    
    def depositMoney(self, amount):
        with open("bank/userBalance.txt", "r") as f:
            currentBalanace = Decimal(f.read())
        
        # ვქმნით დროებით ცვლადს რომ ახალი მნიშვნელობები მივანიჭოთ
        # ჯერ სტრინგად იმიტომ ვაქცევთ მიცემულ ინფორმაციას რომ ეს 'დაუშნოება' არ მოხდეს
        # სტრინგის გარეშე 0.65 გადაიქცევა 0.6499999..ად. ხოლოს სტრინგი 0.65ს იკავებს ზუსტად
        currentBalanace += amount

        # 'w'ს გამოყენებით შეგვიძლია overwriteის განხორციელება
        with open("bank/userBalance.txt", "w") as f:
            f.write(str(currentBalanace))

    def withdrawMoney(self, amount):
        with open("bank/userBalance.txt", "r") as f:
            currentBalanace = Decimal(f.read())

        # მოწმდება შეგვიძლია თუ არა მაგდენი რაოდენობა თანხის გამოტანა
        if amount > currentBalanace:
            print("You do not have sufficient funds for this action.")
        else:
            # იგივე რაც depositMoneyში
            currentBalanace -= amount
            with open("C:/Users/shalv/OneDrive/Desktop/stepItMidterms/bank/userBalance.txt", "w") as f:
                f.write(str(currentBalanace))

# ზოგადი ვალიდატორი. ამოწმებს ფული სწორადაა თუ არა შეყვანილი
def validateMoneyInput():
    while True:
        try:
            amount = Decimal(input("Please enter the amount of money: "))
        except InvalidOperation:
            print("Do not use non-integer sybmol(s).")
            continue

        if amount < 0:
            print("Enter amount more than 0.")
            continue

        # ამოწმებს რომ წილადის მერე 2ზე მეტი ციფრი არ იყოს
        if amount.as_tuple().exponent < -2:
            print("Only enter 2 numbers after the decimal point.")
            continue

        return amount

# იგივე სტრუქტურა რომელსაც validateMoneyInput იყენებს. ამ ლუპით ვქმნით ზოგადად კლასს.
while True:
    try:
        startingMoney = Decimal(input("Please chose the money you'd like to start working with: "))
    except InvalidOperation:
        print("Do not use non-integer symbol(s).")
        continue

    if startingMoney < 0:
        print("Enter amount equal to or more than 0.")
        continue

    # ამოწმებს რომ წილადის მერე 2ზე მეტი ციფრი არ იყოს
    if startingMoney.as_tuple().exponent < -2:
        print("Only enter 2 numbers after the decimal point.")
        continue

    balance = Bank(startingMoney)
    break

# მთავარი მამუშავებელი
while True:
    # ვაძლევთ მომხმარებელს 
    print("1. Print money.")
    print("2. Deposit money.")
    print("3. Take out money.")
    print("4. Stop the program.")

    # მომხმარებელს შეყავს ქმედების ნომერი და პარალელურად მოწმდება ვალიდაცია
    try:
        actionChooser = int(input("Please enter the action you'd like to do: "))
    except ValueError:
        print("Do not use non-integer symbol(s).")
        continue

    # ქმედების ნომრები და შემთხვევები
    match actionChooser:
        case 1:
            balance.printMoney()
        case 2:
            # მეორე და მესამე ქეისებში იშვება ფულზე მომუშავე და ვალიდაციის გამკეთებელი ფუნქცია
            balance.depositMoney(validateMoneyInput())
        case 3:
            balance.withdrawMoney(validateMoneyInput())
        case 4:
            print("Thank you for using our services.")
            break
        case _:
            print("Please enter numbers '1', '2', or '3'")
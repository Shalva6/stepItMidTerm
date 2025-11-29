import random
 
class GuessNumber:
    def __init__(self):
        """კონსტრუქტორი: ამზადებს თამაშს"""
        
        # 1. კომპიუტერი ირჩევს შემთხვევით რიცხვს 1-დან 100-მდე
        # randint(a, b) აბრუნებს მთელ რიცხვს a-სა და b-ს შორის
        self.secret_number = random.randint(1, 100)
        self.attempts = 5

    def play(self):
        """თამაშის დაწყება"""
        print("კომპიუტერმა ჩაიფიქრა რიცხვი 1-დან 100-მდე.")
        print("გამოიცანი!")

        # პროგრამამ იმუშაოს სანამ ცდების რაოდენობა არ დავარდება 0ზე
        while self.attempts != 0:

            # ვალიდაცია რომ რიცხვი სწორად დაფიქსირდეს
            try:
                numberGuessed = int(input("რა რიცხვი გინდა გამოიცნო?: "))
            except ValueError:
                print("აირჩიე რიცხვი 100სა და 0ს შორის.")
                continue

            # ვალიდაცია რომ რიცხვი მოცემულ შუალედს არ გასცდეს
            if numberGuessed > 100 or numberGuessed < 0:
                print("აირჩიე რიცხვი 100სა და 0ს შორის.")
                continue

            # თუ ჩაწერილი ნაკლებია ჩაფიქრებულზე
            if numberGuessed < self.secret_number:
                # აკლდება 'ცდა'
                self.attempts -= 1
                print(f"{numberGuessed} არის ნაკლები ჩაფიქრებულ რიცხვზე.")
        
            # თუ ჩაწერილი რიცხვი მეტია ჩაფიქრებულზე
            elif numberGuessed > self.secret_number:
                # აკლდება 'ცდა'
                self.attempts -= 1
                print(f"{numberGuessed} არის მეტი ჩაფიქრებულ რიცხვზე.")

            if numberGuessed == self.secret_number:
                print(f"სწორია! {self.secret_number} იყო ჩაფიქრებული რიცხვი!")
                return
        print(f"საწუხაროდ წააგე. ჩაფიქრებული რიცხვი იყო {self.secret_number}")
       
 
# ობიექტის შექმნა
game = GuessNumber()
game.play()
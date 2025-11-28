import random

class Hangman:
    def __init__(self):
        # სიტყვების სია
        self.words_list = ["PYTHON","PYCHARM","ITSTEP"]


        self.secret_word = random.choice(self.words_list)


        self.lives = 6  # სიცოცხლე
        self.guesses = []  # გამოყენებული ასოების სია

    def show_board(self):

        display_list = []


        for char in self.secret_word:
            if char in self.guesses:
                # თუ ასო უკვე გამოცნობილია, ვამატებთ ასოს
                display_list.append(char)
            else:
                # თუ არა, ვამატებთ ტირეს
                display_list.append("_")


        print("სიტყვა:", " ".join(display_list))

        # თუ სიაში ტირე აღარ დარჩა, ესეიგი მოიგო
        if "_" not in display_list:
            return True
        return False

    def play(self):
        """თამაშის მთავარი ციკლი"""
        print("დავიწყეთ თამაში!")

        # სანამ სიცოცხლე გვაქვს
        while self.lives > 0:
            print("\n----------------")
            print(f"დარჩენილი სიცოცხლე: {self.lives}")

            # ვამოწმებთ, ხომ არ მოიგო
            if self.show_board():
                print("გილოცავ! შენ გამოიცანი სიტყვა!")
                return  #თამაში მორჩა

            # ასოს შეყვანა
            letter = input("შეიყვანე ასო: ").upper()  #ვაქცევთ დიდ ასოდ

             #ვალიდაცია
            if len(letter) != 1:
                print("დაწერე მხოლოდ ერთი ასო!")
                continue  # თავიდან იკითხოს

            if letter in self.guesses:
                print("ეს ასო უკვე თქვით.")
                continue

            #ვამატებთ ასოს გამოყენებულებში
            self.guesses.append(letter)

            if letter in self.secret_word:
                print("სწორია!")
            else:
                print("არასწორია!")
                self.lives = self.lives - 1

        # თუ ციკლი დამთავრდა და აქ ჩამოვიდა, ე.ი. სიცოცხლე გათავდა
        print("\nსამწუხაროდ წააგეთ.")
        print(f"სწორი სიტყვა იყო: {self.secret_word}")



game = Hangman()
game.play()

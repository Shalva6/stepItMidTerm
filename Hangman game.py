import random

class Hangman:
    def __init__(self):
        # სიტყვების სია
        self.words_list = ["PYTHON","PYCHARM","ITSTEP"]

        #ირჩევს ერთ random სიტყვას
        self.secret_word = random.choice(self.words_list)


        self.lives = 6  # სიცოცხლე
        self.guesses = []  # გამოყენებული ასოების სია

    def show_board(self):

        display_list = [] #დროებითი სია ვიზუალიზაციისთვის

        #გავდივართ საიდუმლო სიტყვის თითოეულ ასოზე
        for char in self.secret_word:
            if char in self.guesses:
                # თუ ასო უკვე გამოცნობილია, ვამატებთ ასოს
                display_list.append(char)
            else:
                # თუ არა, ვამატებთ ტირეს
                display_list.append("_")

        #join აერთებს სიის ელემენტებს ერთ სტრიქონად შუაში გამოტოვებით
        print("სიტყვა:", " ".join(display_list))

        #მოგების შემოწმება, თუ სიაში ტირე აღარ დარჩა, ესეიგი მოიგო
        if "_" not in display_list:
            return True
        return False

    def play(self):
        """თამაშის მთავარი ციკლი"""
        print("დავიწყეთ თამაში!")

        #ციკლი ტრიალებს სანამ სიცოცხლე გვაქვს
        while self.lives > 0:
            print("\n----------------")
            print(f"დარჩენილი სიცოცხლე: {self.lives}")

            # ვამოწმებთ, ხომ არ მოიგო, თუ ის true-ს დააბრუნებს, ესეიგი მოვიგეთ
            if self.show_board():
                print("გილოცავ! შენ გამოიცანი სიტყვა!")
                return  #თამაში მორჩა

            #მომხმარებელს შეყავს ასო და ვაქცევთ დიდ ასოდ
            letter = input("შეიყვანე ასო: ").upper()

             #ვალიდაცია(შემოწმება)
            if len(letter) != 1:
                print("დაწერე მხოლოდ ერთი ასო!")
                continue  # თავიდან იკითხოს

            if letter in self.guesses:
                print("ეს ასო უკვე თქვით.")
                continue

            #ვამატებთ ასოს გამოყენებულებში
            self.guesses.append(letter)

            #ვამოწმებთ, არის თუ არა ეს ასო საიდუმლო სიტყვაში
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

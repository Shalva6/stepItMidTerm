import json
class BookManager:
    def __init__(self):
        with open("C:/Users/shalv/OneDrive/Desktop/yikes/midTermsStepIt/bookManager/booksCollection.json", "r", encoding = "utf-8") as f:
            self.__listOfAllBooks = json.load(f)

    def showAllBooks(self):
        for eachPerson in self.__listOfAllBooks:
            print(f"Author {eachPerson['Author']}'s works:")
            for personsBook in eachPerson["Author's books"]:
                print(f" - {personsBook['Title']} in {personsBook['Year']}")
        print()

    def dataSaver(self):
        with open("C:/Users/shalv/OneDrive/Desktop/yikes/midTermsStepIt/bookManager/booksCollection.json", "w", encoding = "utf-8") as f:
            json.dump(self.__listOfAllBooks, f, indent = 4, ensure_ascii = False)

    def addBook(self, userBook):
        for eachPersonInList in self.__listOfAllBooks:
            if userBook.author.lower() in eachPersonInList['Author'].lower():
                print("This author already exists in the database.")
                eachPersonInList["Author's books"].append({
                    "Title": userBook.title,
                    "Year": userBook.releaseYear
                }) 
                print("Data has been updated: New book added into the list.")
                self.dataSaver()
                return
            
        self.__listOfAllBooks.append({
            "Author": userBook.author,
            "Author's books": [{
                "Title": userBook.title,
                "Year": userBook.releaseYear
            }]
        })
        print("New author added.")
        self.dataSaver()
    
    def findBookByTitle(self, userBook):
        for eachPersonInList in self.__listOfAllBooks:
            for book in eachPersonInList["Author's books"]:
                if userBook.title.lower() == book["Title"].lower():
                    print(f"{book["Title"]} was written by {eachPersonInList['Author']} in {book["Year"]}")
                    return
        print(f"No book under the title of {userBook.title} found.")

# ვქმნით ახალ წინგს
class Book:
    def __init__(self, author, title, releaseYear):
        self.author = author
        self.title = title
        self.releaseYear = releaseYear

# მენეჯერის კლასს თავიდანვე ვააქტიურებთ
manager = BookManager()

while True:
    # მომხმარებელს ვაჩვენებთ შესაძლო ქმედებებს
    print("1. Show the list of all books.")
    print("2. Look for book by title name.")
    print("3. Add a new book.")
    print("4. Quit the program.")

    # ქმედების აიდის ვალიდაცია
    try:
        action = int(input("Please choose an action: "))
    except ValueError:
        print("Please enter a valid action.")
        continue

    # ქმედებები
    match action:
        case 1:
            manager.showAllBooks()
        case 2:
            userTitle = input("Please enter the name of the book you are trying to find: ")
            userBook = Book(None, userTitle, None)
            manager.findBookByTitle(userBook)
        case 3:
            userAuthor = input("Please enter the name of the name of your author: ")
            userTitle = input("Please enter the name of the name of your author's title: ")
            try:
                userYear = int(input("Please enter the name of the name of your author's book year: "))
            except ValueError:
                print("Please enter a valid year.")
                continue
            userBook = Book(userAuthor, userTitle, userYear)
            manager.addBook(userBook)
        case 4:
            print("Thank you for using BookLibrary.tm. Exiting program.")
            break
        case _:
            print("Please choose a valid option.")
            continue
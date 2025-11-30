import json
class BookManager:
    def __init__(self):
        with open("bookManager/booksCollection.json", "r", encoding = "utf-8") as f:
            self.__listOfAllBooks = json.load(f)

    def showAllBooks(self):
        for eachPerson in self.__listOfAllBooks:
            print(f"ავტორი {eachPerson['Author']}ს მანუშევრებია:")
            for personsBook in eachPerson["Author's books"]:
                print(f" - {personsBook['Title']} დაწერილი {personsBook['Year']} წელს")
        print()

    def dataSaver(self):
        with open("bookManager/booksCollection.json", "w", encoding = "utf-8") as f:
            json.dump(self.__listOfAllBooks, f, indent = 4, ensure_ascii = False)

    def addBook(self, userBook):
        for eachPersonInList in self.__listOfAllBooks:
            if userBook.author.lower() in eachPersonInList['Author'].lower():
                print("This author already exists in the database.")
                eachPersonInList["Author's books"].append({
                    "Title": userBook.title,
                    "Year": userBook.releaseYear
                }) 
                print("დაემატა ახალი წიგნი.")
                self.dataSaver()
                return
            
        self.__listOfAllBooks.append({
            "Author": userBook.author,
            "Author's books": [{
                "Title": userBook.title,
                "Year": userBook.releaseYear
            }]
        })
        print("დაემატა ახალი ავტორი.")
        self.dataSaver()
    
    def findBookByTitle(self, userBook):
        for eachPersonInList in self.__listOfAllBooks:
            for book in eachPersonInList["Author's books"]:
                if userBook.title.lower() == book["Title"].lower():
                    print(f"{book["Title"]} იყო დაწერილი {eachPersonInList['Author']} მიერ {book["Year"]} წელს")
                    return
        print(f"წიგნი {userBook.title} არ არსებობს ბიბლიოთეკაში.")

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
    print("1. წიგნების გამოტანა.")
    print("2. წიგნის სახელით მოძებნა.")
    print("3. ახალი წიგნის დამატება.")
    print("4. გამოსვლა პროგრამიდან.")

    # ქმედების აიდის ვალიდაცია
    try:
        action = int(input("ჩაწერე ქმედების აიდი: "))
    except ValueError:
        print("შეიყვანე სწორი მონაცემი (რიცხვები).")
        continue

    # ქმედებები
    match action:
        case 1:
            manager.showAllBooks()
        case 2:
            userTitle = input("ჩაწერე სახელი წიგნისა, რომელსაც ეძებ: ")
            userBook = Book(None, userTitle, None)
            manager.findBookByTitle(userBook)
        case 3:
            userAuthor = input("ჩაწერე ავტორის სახელი: ")
            userTitle = input("ჩაწერე წიგნის სახელი: ")
            try:
                userYear = int(input("ჩაწერე რომელ წელს დაიწერა ეს წიგნი: "))
            except ValueError:
                print("შეიყვანე მხოლოდ რიცხვები.")
                continue
            userBook = Book(userAuthor, userTitle, userYear)
            manager.addBook(userBook)
        case 4:
            print("სრულდება პროგრამა.")
            break
        case _:
            print("აირჩიეტ სწორი მოქმედება.")
            continue

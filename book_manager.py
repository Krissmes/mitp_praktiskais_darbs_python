import os
import json

directory_path = os.path.dirname(__file__) #atrod library_data.json
file_path = os.path.join(directory_path, "data\library_data.json")

if os.stat(file_path).st_size == 0: #pārbauda vai library_data.json kaut kas ir, ja nē tad izveido tukšu array
    True
    with open(file_path, "w") as f:
        json.dump([], f)

def add_book(): #funkcija ļauj pievienot jaunu grāmatu 
    print("Enter the necessary information about the book to be added:")
    def book_info(): #pieprasa no lietotāja informāciju par grāmatu
        try: #pārbauda vai cena/pieejamais skaits ir pārvēršami par float un int
            nosaukums = input("Enter the name of the book:\n")
            autors = input("Enter the author of the book:\n")
            cena = float(input("Enter the price of the book (number):\n"))
            pieejamais_skaits = int(input("Enter the available number of this book (number):\n"))

            if cena < 0: #pārbauda vai cena/pieejamais skaits ir negatīva vērtība
                raise ValueError("Price cannot be negative")
            if pieejamais_skaits < 0:
                raise ValueError("Available number cannot be negative")
            
            #sagaida ievada vērtības no lietotāja un pārvērš tās par library
            return{
        "nosaukums": nosaukums,
        "autors": autors,
        "cena": cena,
        "pieejamais skaits": pieejamais_skaits,
        "izsniegtais skaits": 0
        }
        except Exception as e:
            print(f"Incorrect data was entered!\nError {e}\n") #paziņo lietotājam ka tika nepareizi ievadīti dati
    

    book = book_info() #neļauj funkcijai kļūdas gadījumā library_data.json ievadīt null
    if book == None:
        return
    with open(file_path, "r") as f: #pievieno iegūtos datus library_data.json
        books = json.load(f)
    books.append(book)
    with open(file_path, "w") as f:
        json.dump(books, f, indent=4)
    print("Book added!")

def all_books(): #izprintē visu sarakstu ar grāmatām
    with open(file_path, "r") as f:
        books = json.load(f)
    saraksts = json.dumps(books, indent=4)
    print(saraksts)

#funkcija top izsniegtākajām grāmatām 
def top5_izsniegts():
    print("Top 5 most given out books:")
    with open(file_path, "r") as f:
        books = json.load(f)
    sorted_books = sorted(books, key=lambda x: x["izsniegtais skaits"], reverse=True) #sakārto ielādētos datus pēc "izsniegtais skaits" dilstošā secībā
    for x in sorted_books[:5]:
        print(f"Name: {x["nosaukums"]}\nAuthor: {x["autors"]}\nGiven: {x["izsniegtais skaits"]} times") #izprintē top 5 grāmatu nosaukumus, autorus, izsniegto skaitu

#tāda pati funkcija kā iepriekšējā tikai dārgākajām grāmatām
def top5_expensive():
    print("Top 5 most expensive books:")
    with open(file_path, "r") as f:
        books = json.load(f)
    sorted_expensive = sorted(books, key=lambda x: x["cena"], reverse=True)
    for x in sorted_expensive[:5]:
        print(f"Name: {x["nosaukums"]}\nAuthor: {x["autors"]}\nCena: {x["cena"]}")
#funkcija grāmatas satura mainīšanai
def change_book():
    with open(file_path, "r") as f:
            books = json.load(f)

    def book_finding(): #atrod grāmatu      
        found_books = []
#pieprasa izvēlēties meklēšanas opciju pēc grāmatas vai autora vārda
        find_option = input("Enter 'name' if you want to search by name or\nEnter 'author' if you want to search by author:\n").lower()
#grāmatas tiek pievienotas listei meklējot tās pēc vārda
        if find_option == "name":
            find_name = input("Enter the name of book you want to change:\n")
            for book in books:
                if book["nosaukums"] == find_name:
                    found_books.append(book)
#tas pats, bet pēc autora
        elif find_option == "author":
            find_author = input("Enter the author name you are looking for:\n")
            for book in books:
                if book["autors"] == find_author:
                    found_books.append(book)
            
        else:
            print("Not sure what you are doing.")
            return found_books
        
        return found_books
#funkcija lāuj izvēlēties grāmatu no atrasto grāmatu saraksta
    def book_choice():
        result = book_finding() #ja grāmatas netika atrastas tad izprintē, ka nekas netika atrasts
        if result == []:
            print("The book you are looking for was not found.")
            return None

        print("Select one book you desire to change:\n") #funkcija izprintē sakārtotu sarakstu ar visām atrastajām grāmatām
        for index, book in enumerate(result, start=1):
            print(f"{index}. Name: {book['nosaukums']}, Author: {book['autors']}")

        while True: #funkcija liek izvēlēties no saraksta grāmatu ievadot tās nr.
            choice = input("Enter the number of the book, or enter 'exit' to stop: ").lower()

            if choice == "exit": #ievadot exit, tiek beigta meklēšana
                print("You exited book changeing.")
                return None

            elif not choice.isdigit(): #pārbauda vai ievadītais skaitlis ir cipars
                print("Please enter a valid number.")
                continue
                
            choice = int(choice) #pārveido ievadi par intiger, lai salīdzinātu ar iepriekš sakārtoto grāmatu sarakstu
            if 1 <= choice <= len(result): #salīdzina ievadi ar sakārtoto sarakstu
                return result[choice - 1]
            
            else:
                print("Number out of range.")

    change = book_choice()
    while True: #funkcija ļauj mainīt izvēlētās grāmatas key values līdz lietotājs ievada stop
        if change == None: #ja iepriekš tika ievadīts exit, apstādina šo funkciju
            return

        print(change) #izprintē iezvēlētās grāmatas visus key and value pārus
        #ļauj izvēlēties key kurā veikt izmaiņas
        key = input("Enter the key you want to change or 'stop' to finish and save change: ").lower()
#ievadot stop tiek pārtraukta funkcija
        if key == "stop":
            print("You exited book changeing.")
            break
#ļauj vēlreiz izvēlēties key, ja tā tika nepareizi ievadīta, un paskaidro, ka key bija nepareizi ievadīta
        if key not in change:
            print("Key was not in dictionary, enter a valid key.")
            continue
        
        new_book = input(f"Enter new value for {key}: ")#sagaida izmaiņas iepriekš izvēlētajam key
        try: #pārbauda vai, piemēram, pie 'cena' netika ievadīts piemēram burts,
            if key == "nosaukums": #un pārveido string uz float vai int, lai formāts netiktu sajauks iekš library_data.json
                change[key] = new_book

            elif key == "autors":
                change[key] = new_book

            elif key == "cena":
                change[key] = float(new_book)

            elif key == "pieejamais skaits":
                change[key] = int(new_book)

            elif key == "izsniegtais skaits":
                change[key] = int(new_book)

            with open(file_path, "w") as f: #izmaina info iekš library_data.json
                json.dump(books, f, indent=4)

            print("Book updated successfully!") #izprintē, ka izmaiņas tika veiksmīgi ieviestas

        except Exception as e: #informē lietotāju par kļūdu tās gadījumā
            print(f"Incorrect data was entered!\nError {e}\n")

"""pieejamo funkciju saraksts:
1. change_book() - ļauj izmainīt esošas grāmatas key values.
2. top5_expensive() - parāda 5 dārgākās grāmatas.
3. top5_izsniegts() - parāda 5 izsniegtākās grāmatas.
4. all_books() - izprintē sarakstu ar visām grāmatām.
5. add_book() - ļauj pievienot grāmatu library_data.json."""
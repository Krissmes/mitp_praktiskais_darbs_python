import book_manager as a #importē studenta A veidotās funkcijas
import borrowing_manager as b #importē studenta B veidotās funkcijas

def user_interface():
    print("Option 1: Add or change book\nOption 2: Look trough entire database\nOption 3: Borrow or return a book\nOption 4: Find a book\nOption 5: Top 5 books")
    user_input = input("Enter 1/2/3/4/5 to start working: ") #izprintē visas iespējamās opcijas un piedāvā izvēlēties vienu
    
    if user_input == "1": #izvēloties opciju 1 piedāvā izvēlēties starp grāmatas datu atjaunināšanu vai grāmatas pieivienošanu, vai atsit lietotāju uz sākumu
        user_input1 = input("Enter 'add' to add a book or\nEnter 'change' to change a book or\nEnter 'back' to go back:\n").lower()
        while True:
            if user_input1 == "add":
                a.add_book() #izsauc grāmatas pievienošanu
                break

            elif user_input1 == "change":
                a.change_book() #izsauc grāmatas atjaunināšanu
                break
            
            else:
                user_interface()

    elif user_input == "2": #izvēloties opciju 2, izsauc grāmatu sarakstu
        a.all_books()

    elif user_input == "3": #izvēloties opciju 3, izsauc grāmatu aizņemšanu/atdošanu
        user_input_1 = input("Enter 'take' to take the wanted book/s\nEnter 'give back' to give back the handed out books:\n").lower()
        if user_input_1 == 'take':
            b.give_book()
        elif user_input_1 == 'give back':
            b.receive_book()
        else:
            print("You wrote something else, try again")
            user_interface() 

    elif user_input == "4": #izvēloties opciju 4, izsauc grāmatu meklēšanu
        b.book_finding()

    elif user_input == "5": #izsauc visus top 5 sarakstus
        a.top5_expensive()
        print("_" * 100)
        a.top5_izsniegts()
        print("_" * 100)
        b.least_5_given_books()

    else:
        print("You chose wrongfully.") #visu citu izvēļu gadījumā atsit lietotāju uz funkcijas sākumu
        user_interface()

user_interface()
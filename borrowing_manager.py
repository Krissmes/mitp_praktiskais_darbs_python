import os
import json

directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, "data\library_data.json")  #ceļš uz datu failu

def read_data(): # nolasa datus no library_data.json faila
    with open(file_path, 'r', encoding = 'utf-8') as file:
        dati = json.load(file)      #šeit tiek saglabāti visi dati
        return dati

    
def book_finding(): 
    """
Funkcija meklē grāmatas balstoties uz ievaddatiem (grāmatas nosaukums un tās autors)
Sagaida grāmatas nosaukumu (name), str tipa mainīgais ; sagaida grāmatas autoru (author), str tipa mainīgais
Atgriež datus par grāmatām, kuru nosaukumi un autori sakrīt ar ievaddatiem
Ja kāda no ievaddata vērtības ir 'all', tad netiek ņemts vērā konkrētais parametrs (tiek ignorētas pārbaudes, tam konkrētajam parametram)
"""
    try:
        name = str(input("Enter the books name\nIf you want all the book names then write 'all':\n"))                                   # lietotājs ievada grāmatas nosaukumu
        author = str(input("Enter the books author\nIf you want all the book authors then write 'all':\n"))                                 # lietotājs ievada grāmatas autoru
    except Exception as e:
        print(f"ValueError: {e}")
    else:
        dati = read_data()                                      #nolasa jaunākos datus
        gramata_eksiste = False                                 #nepieciešams, lai pārbaudītu vai grāmata tika atrasta
        
        for x in range(len(dati)):
            if dati[x]['nosaukums'] == name or name == 'all':      # salīdzina datubāzes grāmatu nosaukumus ar ievadīto grāmatas nosaukumu
                if dati[x]['autors'] == author or author == 'all':         # salīdzina datubāzes grāmatu autoru ar ievadīto grāmatas autoru
                    print(f"{x+1}. Name: {dati[x]['nosaukums']}\nAuthor: {dati[x]['autors']}\nPrice: {dati[x]['cena']}\nIn stock: {dati[x]['pieejamais skaits']}\nGiven out: {dati[x]['izsniegtais skaits']}\n") #parāda lietotājam atrastās grāmatas
                    gramata_eksiste = True
        if not gramata_eksiste:                                 #paziņo lietotājam, ka nav atrasta grāmata, ja tā nav atrasta
            print('ValueError: Could not find a book with that name') 



def give_book():
    """
    Funkcija samazina grāmatas pieejamo skaitu un palielina izsniegto skaitu par izsniedzamo eksemplāru skaitu
    Sagaida grāmatas nosaukumu (name), str tipa mainīgais; sagaida grāmatas izsniedzamo eksemplāru skaitu (give_count), int tipa mainīgais, kas lielāks par 0
    Rezultātā samazina grāmatas pieejamo skaitu un palielina izsniegto skaitu par izsniedzamo eksemplāru skaitu
    Šī darbība netiek veikta, ja ievaddati neatbilst sagaidāmajām vērtībām, vai arī ja funkcijas izpildes laikā, rodas jebkāds error
    
    """
    try:    
        name = str(input("Enter the issue books name:\n"))                                                          # lietotājs ievada grāmatas nosaukumu  
        give_count = int(input("Enter how many copies of the book do you want to issue:\n"))                           # lietotājs ievada cik grāmatas grib saņemt
    except Exception as e:
        print(f"ValueError: {e}")
    else:
        dati = read_data()                                      #nolasa jaunākos datus
        book_exists = False                                 #šis mainīgais ir nepieciešams, lai pārbaudītu, vai beigās atrod grāmatu
        if give_count > 0:
            for x in range(len(dati)):
                if name == dati[x]['nosaukums']:     # atrod izsniedzamo grāmatu
                    book_exists = True          
                    if give_count <= dati[x]['pieejamais skaits']:    # pārbauda vai ir pietiekami daudz grāmatas kuras izsniegt
                        try:
                            temp_pieejamais_skaits = dati[x]['pieejamais skaits'] - give_count          #samazina grāmatu pieejamo skaitu
                            temp_izsniegtais_skaits = dati[x]['izsniegtais skaits'] + give_count        #palielina grāmatu izsniegto skaitu
                        except Exception as e:
                            print(f"Error: {e}")                                                      #izprintē Error, ja notiek negaidīta kļūda(nevajadzētu būt kļūdām pateicoties iepriekšējām pārbaudēm, bet, ņemot vērā to, ka pēc funkcijas dati tiks saglabāti, izlēmu izmantot try un except, lai kods būtu vēl drošāks)
                        else:
                            dati[x]['pieejamais skaits'] = temp_pieejamais_skaits               
                            dati[x]['izsniegtais skaits'] = temp_izsniegtais_skaits             # izmaiņas saglabā mainīgajā dati

                            with open(file_path, 'w', encoding='utf-8') as file:
                                json.dump(dati, file, indent=4)                       #izmaiņas saglabā library_dat.json failā
                            
                            print("Grāmata/s izsniegta/s!")
                    else:
                        print("ValueError: There are not enough books available")
            if book_exists == False:
                print('ValueError: Could not find a book with that name')             
        else:               
            print("ValueError: The number of issued books is expected to be equal or greater than zero")   # paziņo lietotājam, ka ievaddatu izsniedzamo grāmatu skaitam jābūt nenegatīvam.
        

def receive_book():
    """
    Funkcija palielina grāmatas pieejamo skaitu un samazina izsniegto skaitu par atgriežamo eksemplāru skaitu
    Sagaida grāmatas nosaukumu (name), str tipa mainīgais; sagaida grāmatas saņemamo eksemplāru skaitu (recieve_count), int tipa mainīgais, kas lielāks par 0
    Rezultātā palielina grāmatas pieejamo skaitu un samazina izsniegto skaitu par atgriežamo eksemplāru skaitu
    Šī darbība netiek veikta, ja ievaddati neatbilst sagaidāmajām vērtībām, vai arī ja funkcijas izpildes laikā, rodas jebkāds error
    
    """
    try:
        name = str(input("Enter the name of the book you want to return:\n"))
        receive_count = int(input("Enter how many copies of the book do you want to return:\n"))
    except Exception as e:
        print(f"ValueError: {e}")
    else:
        dati = read_data()                                      #nolasa jaunākos datus
        book_exists = False                                     #šis mainīgais ir nepieciešams, lai pārbaudītu, vai beigās atrod grāmatu
        if receive_count > 0:
            for x in range(len(dati)):
                if name == dati[x]['nosaukums']:     # atrod atgriežamo grāmatu
                    book_exists = True
                    if receive_count <= dati[x]['izsniegtais skaits']:    # pārbauda vai ir pietiekami daudz grāmatas kuras atgriezt
                        try:
                            temp_pieejamais_skaits = dati[x]['pieejamais skaits'] + receive_count          #palielina grāmatu pieejamo skaitu
                            temp_izsniegtais_skaits = dati[x]['izsniegtais skaits'] - receive_count        #samazina grāmatu izsniegto skaitu
                        except:
                            print("Error: Kaut kas nogāja greizi.")                                                      #izprintē error, ja notiek negaidīta kļūda(nevajadzētu būt kļūdām pateicoties iepriekšējām pārbaudēm, bet, ņemot vērā to, ka pēc funkcijas dati tiks saglabāti, izlēmu izmantot try un except, lai kods būtu vēl drošāks)
                        else:
                            dati[x]['pieejamais skaits'] = temp_pieejamais_skaits               
                            dati[x]['izsniegtais skaits'] = temp_izsniegtais_skaits             # izmaiņas saglabā mainīgajā dati

                            with open(file_path, 'w', encoding='utf-8') as file:
                                json.dump(dati, file, indent=4)                   #izmaiņas saglabā library_dat.json failā

                            print("Grāmata/s atgriezta/s!")
                    else:
                        print("ValueError: That many books have not been issued") 
                        
            if book_exists == False:
                print('ValueError: Could not find a book with that name')
                            
        else:               
            print("ValueError: The number of books you want to return is expected to be equal or greater than zero")   # paziņo lietotājam, ka ievaddatu atgriežamo grāmatu skaitam jābūt nenegatīvam.
                        

def least_5_given_books():
    """
    Funkcija lietotājam parāda 5 visretāk izsniegtās grāmatas.
    Šeit nav ievaddati, funkcija tikai lietotājam parāda 5 grāmatas atbilstoši kritērjiem.
"""
    dati = read_data()                  #nolasa jaunākos datus
   
    def temp_func(book):                    #key parametrs priekš sort metodes(vajadzīgs, lai sakārtotu pēc atslēgas 'izsniegtais skaits') 
        return book['izsniegtais skaits']

    temp_dati = dati.copy()                     #izveidoju dati kopiju, lai, tad, kad sakārtoju sarakstu, šīs izmaiņas nenotiktu globāli(neizmainītu sarakstu dati)
    temp_dati.sort(key=temp_func)               #sakārto datus augošā secībā

    if len(dati) <= 5:                       # pārbauda vai saraksts garums ir mazāks vai vienāds ar 5
        for x in range(len(temp_dati)):              
            print(f"{x+1}. Name: {temp_dati[x]['nosaukums']}\nAuthor: {temp_dati[x]['autors']}\nPrice: {temp_dati[x]['cena']}\nIn stock: {temp_dati[x]['pieejamais skaits']}\nGiven out: {temp_dati[x]['izsniegtais skaits']}\n")       #parāda lietotājam 5 grāmatas atbilstoši kritērijiem

    else:                                 # ja sarakstā ir vairāk par 5 grāmatām, tad ir jāsaprot, kurām ir vismazākais 'izsniegtais skaits' 
        for x in range(5):
            print(f"{x+1}. Name: {temp_dati[x]['nosaukums']}\nAuthor: {temp_dati[x]['autors']}\nPrice: {temp_dati[x]['cena']}\nIn stock: {temp_dati[x]['pieejamais skaits']}\nGiven out: {temp_dati[x]['izsniegtais skaits']}\n")       #parāda lietotājam 5 grāmatas atbilstoši kritērijiem

    



import os
import json

directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, "data\library_data.json")  #ceļš uz datu failu

def read_data(): # nolasa datus no library_data.json faila
    with open(file_path, 'r', encoding = 'utf-8') as file:
        dati = json.load(file)      #šeit tiek saglabāti visi dati
        return dati

    
def book_finding(name = '' , author = ''): 
    """
Funkcija meklē grāmatas balstoties uz ievaddatiem (grāmatas nosaukums un tās autors)
Sagaida grāmatas nosaukumu (name), str tipa mainīgais, pēc noklusējuma '' ; sagaida grāmatas autoru (author), str tipa mainīgais, pēc noklusējuma ''
Atgriež datus par grāmatām, kuru nosaukumi un autori sakrīt ar ievaddatiem
Ja kāda no ievaddata vērtības ir '', tad netiek ņemts vērā konkrētais parametrs (tiek ignorētas pārbaudes, tam konkrētajam parametram)
"""
    dati = read_data()                                      #nolasa jaunākos datus
    rezultata_gramatas = []                                 # saraksts ar grātamām, kas atbilst ievaddatiem
    
    if isinstance(name, str) and isinstance(author, str):    # pārliecinās, ka ievaddati ir string tipa dati
        for x in range(len(dati)):
            if dati[x]['nosaukums'] == name or name == '':      # salīdzina datubāzes grāmatu nosaukumus ar ievadīto grāmatas nosaukumu
                if dati[x]['autors'] == author or author == '':         # salīdzina datubāzes grāmatu autoru ar ievadīto grāmatas autoru
                    rezultata_gramatas.append(dati[x])          # pievieno konkrēto grāmatu klāt sarakstam ar grāmatām, kas atbilst ievaddatiem
     
    else:
        print("ValueError: Tiek gaidīts string tipa mainīgais, tika ievadīts kaut kas cits.")   # paziņo lietotājam, ka ievaddatiem ir jābūt string formātā
    
    print(rezultata_gramatas)                                  # parāda lietotājam sarakstu, ar sameklētajām grāmatām


# book_finding()

def give_book(name, give_count):
    """
    Funkcija samazina grāmatas pieejamo skaitu un palielina izsniegto skaitu par izsniedzamo eksemplāru skaitu
    Sagaida grāmatas nosaukumu (name), str tipa mainīgais; sagaida grāmatas izsniedzamo eksemplāru skaitu (give_count), int tipa mainīgais, kas lielāks par 0
    Rezultātā samazina grāmatas pieejamo skaitu un palielina izsniegto skaitu par izsniedzamo eksemplāru skaitu
    Šī darbība netiek veikta, ja ievaddati neatbilst sagaidāmajām vērtībām, vai arī ja funkcijas izpildes laikā, rodas jebkāds error
    
    """
    dati = read_data()                                      #nolasa jaunākos datus
    book_exists = False                                 #šis mainīgais ir nepieciešams, lai pārbaudītu, vai beigās atrod grāmatu
    if isinstance(name, str) and isinstance(give_count, int) and give_count > 0:
        for x in range(len(dati)):
            if name == dati[x]['nosaukums']:     # atrod izsniedzamo grāmatu
                book_exists = True          
                if give_count <= dati[x]['pieejamais skaits']:    # pārbauda vai ir pietiekami daudz grāmatas kuras izsniegt
                    try:
                        temp_pieejamais_skaits = dati[x]['pieejamais skaits'] - give_count          #samazina grāmatu pieejamo skaitu
                        temp_izsniegtais_skaits = dati[x]['izsniegtais skaits'] + give_count        #palielina grāmatu izsniegto skaitu
                    except:
                        print("Error: Kaut kas nogāja greizi")                                                      #izprintē Error, ja notiek negaidīta kļūda(nevajadzētu būt kļūdām pateicoties iepriekšējām pārbaudēm, bet, ņemot vērā to, ka pēc funkcijas dati tiks saglabāti, izlēmu izmantot try un except, lai kods būtu vēl drošāks)
                    else:
                        dati[x]['pieejamais skaits'] = temp_pieejamais_skaits               
                        dati[x]['izsniegtais skaits'] = temp_izsniegtais_skaits             # izmaiņas saglabā mainīgajā dati

                        with open(file_path, 'w', encoding='utf-8') as file:
                            json.dump(dati, file, indent=4)                       #izmaiņas saglabā library_dat.json failā
                        
                        print("Grāmata/s izsniegta/s!")
                else:
                    print("ValueError: Tik daudz grāmatas nav pieejamas")
        if book_exists == False:
            print('ValueError: Nevarēja atrast grāmatu ar tādu nosaukumu.')             
    else:               
        print("ValueError: Grāmatas nosaukumam tiek gaidīts string tipa mainīgais un izsniedzamo grāmatu skaitam tiek gaidīts nenegatīvs integer tipa mainīgais, tika ievadīts kaut kas cits.")   # paziņo lietotājam, ka ievaddatu nosaukumam ir jābūt string formātā un ka izsniedzamo grāmatu skaitam jābūt integer formātā.
    

def recive_book(name, recieve_count):
    """
    Funkcija palielina grāmatas pieejamo skaitu un samazina izsniegto skaitu par atgriežamo eksemplāru skaitu
    Sagaida grāmatas nosaukumu (name), str tipa mainīgais; sagaida grāmatas saņemamo eksemplāru skaitu (recieve_count), int tipa mainīgais, kas lielāks par 0
    Rezultātā palielina grāmatas pieejamo skaitu un samazina izsniegto skaitu par atgriežamo eksemplāru skaitu
    Šī darbība netiek veikta, ja ievaddati neatbilst sagaidāmajām vērtībām, vai arī ja funkcijas izpildes laikā, rodas jebkāds error
    
    """
    dati = read_data()                                      #nolasa jaunākos datus
    book_exists = False                                     #šis mainīgais ir nepieciešams, lai pārbaudītu, vai beigās atrod grāmatu
    if isinstance(name, str) and isinstance(recieve_count, int) and recieve_count > 0:
        for x in range(len(dati)):
            if name == dati[x]['nosaukums']:     # atrod atgriežamo grāmatu
                book_exists = True
                if recieve_count <= dati[x]['izsniegtais skaits']:    # pārbauda vai ir pietiekami daudz grāmatas kuras atgriezt
                    try:
                        temp_pieejamais_skaits = dati[x]['pieejamais skaits'] + recieve_count          #palielina grāmatu pieejamo skaitu
                        temp_izsniegtais_skaits = dati[x]['izsniegtais skaits'] - recieve_count        #samazina grāmatu izsniegto skaitu
                    except:
                        print("Error: Kaut kas nogāja greizi.")                                                      #izprintē error, ja notiek negaidīta kļūda(nevajadzētu būt kļūdām pateicoties iepriekšējām pārbaudēm, bet, ņemot vērā to, ka pēc funkcijas dati tiks saglabāti, izlēmu izmantot try un except, lai kods būtu vēl drošāks)
                    else:
                        dati[x]['pieejamais skaits'] = temp_pieejamais_skaits               
                        dati[x]['izsniegtais skaits'] = temp_izsniegtais_skaits             # izmaiņas saglabā mainīgajā dati

                        with open(file_path, 'w', encoding='utf-8') as file:
                            json.dump(dati, file, indent=4)                   #izmaiņas saglabā library_dat.json failā

                        print("Grāmata/s atgriezta/s!")
                else:
                    print("ValueError: Tik daudz grāmatas nav izsniegtas") 
                     
        if book_exists == False:
            print('ValueError: Nevarēja atrast grāmatu ar tādu nosaukumu.')
                          
    else:               
        print("ValueError: Grāmatas nosaukumam tiek gaidīts string tipa mainīgais un atgriežamo grāmatu skaitam tiek gaidīts nenegatīvs integer tipa mainīgais, tika ievadīts kaut kas cits.")  # paziņo lietotājam, ka ievaddatu nosaukumam ir jābūt string formātā un ka atgriežamo grāmatu skaitam jābūt integer formātā.
                      


def least_5_given_books():
    """
    Funkcija lietotājam parāda 5 visretāk izsniegtās grāmatas.
    Šeit nav ievaddati, funkcija tikai lietotājam parāda sarakstu ar 5 grāmatām.
"""
    dati = read_data()                  #nolasa jaunākos datus
    least_given_books = []              #saraksts ar piecām visretāk izsniegtajām grāmatām

    if len(dati) <= 5:                       # pārbauda vai saraksts garums ir mazāks vai vienāds ar 5
        for x in range(len(dati)):              # ja tā ir, tad visas grāmatas pievieno least_given_books sarakstam
            least_given_books.append(dati[x])

    else:                                   # ja sarakstā ir vairāk par 5 grāmatām, tad ir jāsaprot, kurām ir vismazākais 'izsniegtais skaits' 
        def temp_func(book):                    #key parametrs priekš sort metodes(vajadzīgs, lai sakārtotu pēc atslēgas 'izsniegtais skaits') 
            return book['izsniegtais skaits']

        temp_dati = dati.copy()                     #izveidoju dati kopiju, lai, tad, kad sakārtoju sarakstu, šīs izmaiņas nenotiktu globāli(neizmainītu sarakstu dati)
        temp_dati.sort(key=temp_func)               #sakārto datus augošā secībā
                                
        for x in range(5):
            least_given_books.append(temp_dati[x])       #pirmos piecus elemntus pievieno sarakstam ar piecām visretāk izsniegtajām grāmatām

    print(least_given_books)                # parāda lietotājam sarakstu ar piecām visretāk izsniegtajām grāmatām

    




import os
import json

directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, "data\library_data.json")  #ceļš uz datu failu

file = open(file_path, 'r')
dati = json.load(file)      #šeit tiek saglabāti visi dati
file.close()

def book_finding(name = '' , author = ''): 
    """
Funkcija meklē grāmatas balstoties uz ievaddatiem (grāmatas nosaukums un tās autors)
Sagaida grāmatas nosaukumu (name), str tipa mainīgais, pēc noklusējuma '' ; sagaida grāmatas autoru (author), str tipa mainīgais, pēc noklusējuma ''
Atgriež datus par grāmatām, kuru nosaukumi un autori sakrīt ar ievaddatiem
Ja kāda no ievaddata vērtības ir '', tad netiek ņemts vērā konkrētais parametrs (tiek ignorētas pārbaudes, tam konkrētajam parametram)
"""
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
    book_exists = False
    if isinstance(name, str) and isinstance(give_count, int) and give_count > 0:
        for x in range(len(dati)):
            if name == dati[x]['nosaukums']:     # atrod izsniedzamo grāmatu
                book_exists = True
                if give_count <= dati[x]['pieejamais skaits']:    # pārbauda vai ir pietiekami daudz grāmatas kuras izsniegt
                    try:
                        temp_pieejamais_skaits = dati[x]['pieejamais skaits'] - give_count          #samazina grāmatu pieejamo skaitu
                        temp_izsniegtais_skaits = dati[x]['izsniegtais skaits'] + give_count        #palielina grāmatu izsniegto skaitu
                    except:
                        print("Error: Kaut kas nogāja greizi")                                                      #izprintē error, ja notiek negaidīta kļūda(nevajadzētu būt kļūdām pateicoties iepriekšējām pārbaudēm, bet, ņemot vērā to, ka pēc funkcijas dati tiks saglabāti, izlēmu izmantot try un except, lai kods būtu vēl drošāks)
                    else:
                        dati[x]['pieejamais skaits'] = temp_pieejamais_skaits               
                        dati[x]['izsniegtais skaits'] = temp_izsniegtais_skaits             # izmaiņas saglabā mainīgajā dati
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
    book_exists = False
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
                        print("Grāmata/s atgriezta/s!")
                else:
                    print("ValueError: Tik daudz grāmatas nav izsniegtas") 
                     
        if book_exists == False:
            print('ValueError: Nevarēja atrast grāmatu ar tādu nosaukumu.')
                          
    else:               
        print("ValueError: Grāmatas nosaukumam tiek gaidīts string tipa mainīgais un atgriežamo grāmatu skaitam tiek gaidīts nenegatīvs integer tipa mainīgais, tika ievadīts kaut kas cits.")  # paziņo lietotājam, ka ievaddatu nosaukumam ir jābūt string formātā un ka atgriežamo grāmatu skaitam jābūt integer formātā.
                      

# give_book('ABC', 1 )
# print(dati)
# recive_book('ABC', 1 )
# print(dati)
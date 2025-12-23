import os
import json

directory_path = os.path.dirname(__file__)
file_path = os.path.join(directory_path, "library_data.json")


file = open(file_path, 'r')
dati = json.load(file)      #šeit tiek saglabāti visi dati
file.close()

def book_finding(name = '' , author = ''): 
    """
funkcija meklē grāmatas balstoties uz ievaddatiem (grāmatas nosaukums un tās autors)
Sagaida grāmatas nosaukumu (name) pēc noklusējuma '' ; sagaida grāmatas autoru (author) pēc noklusējuma ''
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
        print("ValueTypeError: Tiek gaidīts string tipa mainīgais, tikai ievadīts kaut kas cits.")   # paziņo lietotājam, ka ievaddatiem ir jābūt string formātā
    
    print(rezultata_gramatas)                                  # parāda lietotājam sarakstu, ar sameklētajām grāmatām


book_finding()
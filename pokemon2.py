import requests
import json

counter2 = 0
url2 = 'https://pokeapi.co/api/v2/egg-group/5/'
response2 = requests.get(url2)
if response2.status_code == 200:
    data2 = response2.json()
    results2 = data2.get('pokemon_species', [])
    if results2: 
        for pokemon2 in results2:
            
            names2 = (pokemon2.get('name'))
            if names2 != 'raichu':
                #print (names2)
                counter2 = counter2 + 1
else :
    print('Error')
print(counter2)
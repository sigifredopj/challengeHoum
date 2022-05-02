import requests
import json
counter = 0
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1128'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        if results: 
            for pokemon in results:
                
                names = (pokemon.get('name'))
                aaList = names.count('a')
                if aaList == 2:
                        subs = 'at'
                        
                        if subs in names:
                            
                            counter = counter + 1
                           # print (names)
    else :
        print('Error: {}'.format(response.status_code))
print(counter)
                

                




              
              


             
               
       
     
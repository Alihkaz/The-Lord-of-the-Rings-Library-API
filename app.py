#imports

import requests
import os

#----------------------------------------------------------#----------------------------------------------------------

#description 
# The massive "The Lord of the Rings" database related to this API will provide you with information about the books
# , the movie trilogy, many characters and quotes.
#  You are welcome to use the data in your own apps, mixups and (fun) projects — like I did with creating this API.


#----------------------------------------------------------constants----------------------------------------------------------------------

ONE_API_Endpoint = "https://the-one-api.dev/v2"

header={
      'Authorization': 'Bearer your token from one api'
   }

#----------------------------------------------------------requests and end point --------------------------------------------------------

Search_type=int(input("Please Select what do you want to search for by number:\n 1-List of all books\n 2-one specific book\n 3-all chapters of one specific book\n 4-List of all movies\n  5-one specific movie\n 6-Request all movie quotes for one specific movie (only working for the LotR trilogy)\n 7-List of characters\n 8-Request one specific character\n 9-Request all movie quotes of one specific character\n 10-List of all movie quotes\n 11-Request one specific movie quote\n 12-List of all book chapters\n 13-Request one specific book chapter\n"))


#----------------------------------------------------------#----------------------------------------------------------

# The Lord of the Rings" books

if Search_type==1:
   
   response = requests.get(f'{ONE_API_Endpoint}/book')

   dictionary=response.json()

   for n in range(dictionary['total']):
      print(f'The Lord of the Rings" books are:\n {dictionary["docs"][n]["name"]}')


#----------------------------------------------------------#----------------------------------------------------------

# The Lord of the Rings" specific book

if Search_type==2:
   
   response = requests.get(f'{ONE_API_Endpoint}/book')

   dictionary=response.json()
   
   for n in range(dictionary['total']):
      print(f'The Lord of the Rings" books are:\n -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ') 

   book_id=int(input(f"Please Select the corresponding id for the book you want to serach for\n"))
   
   

   response = requests.get(f'{ONE_API_Endpoint}/book/{dictionary["docs"][book_id]["_id"]}')

   book_dictionary=response.json()
   
  
   print(f"Name: {book_dictionary['docs'][0]['name']}\nlimit:{book_dictionary['limit']} ")
  


#----------------------------------------------------------#----------------------------------------------------------

# All chapters of one specific book

if Search_type==3:
   
   response = requests.get(f'{ONE_API_Endpoint}/book')

   dictionary=response.json()
   
   for n in range(dictionary['total']):
      print(f'The Lord of the Rings" books are:\n -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ') 

   book_id=int(input(f"Please Select the corresponding id for the book you want to search chapters for\n"))
   
   
   response = requests.get(f'{ONE_API_Endpoint}/book/{dictionary["docs"][book_id]["_id"]}/chapter')

   chapters_dictionary=response.json()
   
   
   print(f'{dictionary["docs"][book_id]["name"]} Chapters  are:\n')
   for n in range(chapters_dictionary['total']):
      print(f' -Name: {chapters_dictionary["docs"][n]["chapterName"]} , -ID:{chapters_dictionary["docs"][n]["_id"]} ') 
   
#----------------------------------------------------------#----------------------------------------------------------

# List of all movies

if Search_type==4:
 
   
   response = requests.get(f'{ONE_API_Endpoint}/movie',headers=header)

   dictionary=response.json()

   print('The Lord of the Rings" Movies are:\n')
   for n in range(dictionary['total']):
      print(f' {dictionary["docs"][n]["name"]}')


#----------------------------------------------------------#----------------------------------------------------------
      
# one specific movie

if Search_type==5:
   
   response = requests.get(f'{ONE_API_Endpoint}/movie',headers=header)

   dictionary=response.json()

   print('The Lord of the Rings" Movies are:\n')
   for n in range(dictionary['total']):
      print(f' -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ')
   
   movie_id=int(input(f"Please Select the corresponding id for the Movie you want to search chapters for\n"))
   
 
   response = requests.get(f'{ONE_API_Endpoint}/movie/{dictionary["docs"][movie_id]["_id"]}',headers=header)

   movie_dictionary=response.json()
   
   print(movie_dictionary['docs'])


      


#----------------------------------------------------------#----------------------------------------------------------

# Request all movie quotes for one specific movie (only working for the LotR trilogy)

if Search_type==6:
   

   response = requests.get(f'{ONE_API_Endpoint}/movie',headers=header)

   dictionary=response.json()

   print('The Lord of the Rings" Movies are:\n')
   for n in range(dictionary['total']):
      print(f' -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ')
   
   movie_id=int(input(f"Please Select the corresponding id for the Movie you want to search  Quotes for\n"))
   
 
   response = requests.get(f'{ONE_API_Endpoint}/movie/{dictionary["docs"][movie_id]["_id"]}/quote',headers=header)

   movie_qoutes_dictionary=response.json()
   
   print(movie_qoutes_dictionary['docs'])

#----------------------------------------------------------#----------------------------------------------------------

# List of characters including metadata like name, gender, realm, race and more

if Search_type==7:
   
   response = requests.get(f'{ONE_API_Endpoint}/character',headers=header)

   dictionary=response.json()

  

   print('The Lord of the Rings" characters are:\n')
   for n in range(dictionary['total']):
      try:
        print(f' -Name: {dictionary["docs"][n]["name"]} , -Gender:{dictionary["docs"][n]["gender"]} , -Race:{dictionary["docs"][n]["race"]} ')
      except:
         pass


#----------------------------------------------------------#----------------------------------------------------------

# Request one specific character

if Search_type==8:
   

   response = requests.get(f'{ONE_API_Endpoint}/character',headers=header)

   dictionary=response.json()

   
   for n in range(dictionary['total']):
      try:
        print(f' -Name: {dictionary["docs"][n]["name"]} , -Gender:{dictionary["docs"][n]["gender"]} , -Race:{dictionary["docs"][n]["race"]} ')
      except:
         pass
      
   char_id=int(input('Please select the character you want to search for:\n'))
   
   sp_response = requests.get(f'{ONE_API_Endpoint}/character/{dictionary["docs"][char_id]["_id"]}',headers=header)



   character_dictionary=sp_response.json()
   print(f' -Name: {character_dictionary["docs"][0]["name"]} ,\n-height:{dictionary["docs"][0]["height"]},\n -race:{dictionary["docs"][0]["race"]},\n -gender:{dictionary["docs"][0]["gender"]},\n-birth:{dictionary["docs"][0]["birth"]},\n-spouse:{dictionary["docs"][0]["spouse"]}, \n -death:{dictionary["docs"][0]["death"]}, \n -hair:{dictionary["docs"][0]["hair"]}, \n-wikiUrl:{dictionary["docs"][0]["wikiUrl"]}')


#----------------------------------------------------------#----------------------------------------------------------

# Request all movie quotes of one specific character


if Search_type==9:
   
   
   response = requests.get(f'{ONE_API_Endpoint}/character',headers=header)

   dictionary=response.json()

   
   for n in range(dictionary['total']):
      try:
        print(f' -Name: {dictionary["docs"][n]["name"]} , -Gender:{dictionary["docs"][n]["gender"]} , -Race:{dictionary["docs"][n]["race"]} ')
      except:
         pass
      
   char_id=int(input('Please select the character you want to search the quotes for:\n'))
   
   cq_response = requests.get(f'{ONE_API_Endpoint}/character/{dictionary["docs"][char_id]["_id"]}/quote',headers=header)
   
   cq_dic=cq_response.json()

   print(cq_dic['docs'])

#----------------------------------------------------------#----------------------------------------------------------
# List of all movie quotes   

if Search_type==10:
   

   response = requests.get(f'{ONE_API_Endpoint}/quote',headers=header)

   dictionary=response.json()

   print('The List of all movie quotes are:\n')
   
   for n in range(100000):
      try:
        print(f' -Movie: {dictionary["docs"][n]["movie"]} , -dialog:{dictionary["docs"][n]["dialog"]} ')
      except:
         pass


   

#----------------------------------------------------------#----------------------------------------------------------

# Request one specific movie quote


if Search_type==11:
   

   response = requests.get(f'{ONE_API_Endpoint}/movie',headers=header)

   dictionary=response.json()

   print('The Lord of the Rings" Movies are:\n')
   for n in range(dictionary['total']):
      print(f' -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ')
   
   specific_movie_id=int(input(f"Please Select the corresponding id for the Movie you want to search Quote for\n"))
   
 
   response = requests.get(f'{ONE_API_Endpoint}/quote/{dictionary["docs"][specific_movie_id]["_id"]}',headers=header)

   movie_qoutes_dictionary=response.json()
   
   print(movie_qoutes_dictionary['docs'])
      



#----------------------------------------------------------#----------------------------------------------------------

# List of all book chapters


if Search_type==12:
   
   response = requests.get(f'{ONE_API_Endpoint}/chapter',headers=header)

   dictionary=response.json()

   print('The List of all book chapters are:\n')
   for n in range(dictionary['total']):
      print(f' -chapterName: {dictionary["docs"][n]["chapterName"]} , -book id: {dictionary["docs"][n]["book"]}')


#----------------------------------------------------------#----------------------------------------------------------

# Request one specific book chapter


if Search_type==13:
      
   response = requests.get(f'{ONE_API_Endpoint}/book')

   dictionary=response.json()
   
   for n in range(dictionary['total']):
      print(f'The Lord of the Rings" books are:\n -Name: {dictionary["docs"][n]["name"]} , -ID:{dictionary["docs"][n]["_id"]} ') 

   book_id=int(input(f"Please Select the corresponding id for the book you want to serach chapter in \n"))
   
   response = requests.get(f'{ONE_API_Endpoint}/chapter/{dictionary["docs"][book_id]["_id"]}',headers=header)

   cbook_dictionary=response.json()
    
   print(cbook_dictionary)    

#----------------------------------------------------------#----------------------------------------------------------
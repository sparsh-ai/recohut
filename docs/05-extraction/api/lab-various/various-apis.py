import requests

request = requests.get('http://api.open-notify.org')
print(request.status_code)

people = requests.get('http://api.open-notify.org/astros.json')
people_json  = people.json()

#To print the number of people in space
print("Number of people in space:",people_json['number'])

#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])

parameter = {"rel_rhy":"jingle"}
request = requests.get('https://api.datamuse.com/words',parameter)
rhyme_json = request.json()
for i in rhyme_json[0:3]:
 print(i['word'])

 
#Call the API and verify a response
response = requests.get("http://numbersapi.com/random/math")
print(response.status_code)

#Print random fact
print(response.text)



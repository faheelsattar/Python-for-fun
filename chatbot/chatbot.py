import json
import numpy as np
with open('lab3/data.json', 'r+') as f: 
  data=json.load(f)
  f.seek(0)

for index in range(len(data["data"])):
  greet=input()
  print("Chatbot:")
  for i in range(len(data["data"][index]["question"])):
    f=0
    key=0
    checker=0
    if greet == data["data"][index]["question"][i]:
      if data["data"][index]["name"] == "menu":
        print('If you have a key press 1. If you dont have a key press 2 to generate a key to help you in the future')
        choice=int(input())
        if choice == 1:
          key=int(input('Please enter the key'))
          k=data["users"]
          for i in range(len(data["users"])):
            if k[i]["userid"] == key:
              print('We would like to recommend you:')
              foods=k[i]["preference"]
              menu=data["data"][index]["patterns"]
              for startersindex in range(len(menu[0]["starters"])):
                for foodindex in range(len(foods)):
                  if foods[foodindex].split()[0] in menu[0]["starters"][startersindex].split()[0]:
                    print(menu[0]["starters"][startersindex]+" "+"in starters")
              for maincourseindex in range(len(menu[0]["maincourse"])):
                for foodindex in range(len(foods)):
                  if foods[foodindex].split()[0] in menu[0]["maincourse"][maincourseindex].split()[0]:
                    print(menu[0]["maincourse"][maincourseindex]+" "+"in maincourse")
              for desertsindex in range(len(menu[0]["deserts"])):
                for foodindex in range(len(foods)):
                  if foods[foodindex].split()[0] in menu[0]["deserts"][desertsindex].split()[0]:
                    print(menu[0]["deserts"][desertsindex]+" "+"in deserts")
              print("Our menu")
              print(data["data"][index]["patterns"])
              eat=input("what would you like to eat starters, maincourse, deserts")
              if eat == "starters":
                  print(data["data"][index]["patterns"][0]["starters"])
              elif eat == "maincourse":
                  print(data["data"][index]["patterns"][0]["maincourse"])
              elif eat == "deserts":
                  print(data["data"][index]["patterns"][0]["deserts"])
              for menu in data["data"][index]["patterns"][0][eat]:
                  print("press"," ",f," ","for",menu)
                  f+=1
              pref=int(input())
              for foodindex in range(len(foods)):
                if(data["data"][index]["patterns"][0][eat][pref] == foods[foodindex]):
                  print("enjoy your"+" "+data["data"][index]["patterns"][0][eat][pref])
                  checker=1
              if(checker==0):
                preference=data["data"][index]["patterns"][0][eat][pref]
                with open('lab3/data.json', 'r+') as f: 
                  data["users"][i]["preference"].append(preference)
                  f.seek(0)
                  f.truncate()
                  json.dump(data,f,indent=4)
                  print("enjoy your"+" "+data["data"][index]["patterns"][0][eat][pref]+" "+ data["users"][i]["username"])
          print(data["data"][index]["patterns"][np.random.randint(low=0,high=len(data["data"][index]["patterns"]))])        

        else:
            username=input('Please enter your name')
            key=len(data["users"])+1
            print("Your key is"," ",key," ",".Next time enter it for the food recommendations from Elle that you most likely will choose ")
            print("Our menu")
            print(data["data"][index]["patterns"])
            eat=input("what would you like to eat starters, maincourse, deserts")
            if eat == "starters":
              print(data["data"][index]["patterns"][0]["starters"])
            elif eat == "maincourse":
              print(data["data"][index]["patterns"][0]["maincourse"])
            elif eat == "deserts":
              print(data["data"][index]["patterns"][0]["maincourse"])
            for menu in data["data"][index]["patterns"][0][eat]:
              print("press"," ",f," ","for",menu)
              f+=1
            food=int(input())
            user={
              "userid":key,
              "username": username,
              "preference":[data["data"][index]["patterns"][0][eat][food]]
            }
            with open('lab3/data.json', 'r+') as f: 
              data["users"].append(user)
              f.seek(0)
              f.truncate()
              json.dump(data,f,indent=4)
              print("enjoy your"+" "+data["data"][index]["patterns"][0][eat][food]+" "+ username) 
      print(data["data"][index]["patterns"][np.random.randint(low=0,high=len(data["data"][index]["patterns"]))])        

import subprocess
import random
import json
import webbrowser
import datetime
import time
import pyjokes
import requests
import wikipedia
from googlesearch import search

with open("intents.json") as file:
    data = json.load(file)
    
def lower_1(word):
    return word.lower()


def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)


def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    print("The time is " + hour + " Hours and " + min + " Minutes")  


def app():
    subprocess.Popen("chrome.exe")


def latestnews():

    
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=c49ae54b15f4415f89b1f5cbed9ce8ec')

    try:
        response = requests.get(url)
    except:
        print("Couldn't access link, plz check you internet ")
    
    news = json.loads(response.text)
    
    
    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']), "\n\n")
        print('______________________________________________________\n')
    
        print(str(new['description']), "\n")
        print("..............................................................")
        time.sleep(1)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        elif "google" in inp:
            inp = inp.replace("google", "")
            chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
            for url in search(inp, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % inp)
                continue

        elif "which day" in inp:
            tellDay()
            continue

        elif "time" in inp:
            tellTime()
            continue

        elif "joke" in inp:
            print(pyjokes.get_joke(language="en", category="neutral"))
            continue

        elif "from wikipedia" in inp:
        
            print("Checking the wikipedia ")
            inp = inp.replace("wikipedia", "")
            result = wikipedia.summary(inp, sentences=4)
            print("According to wikipedia")
            print(result)
        
        elif "reminder" in inp:

            print("What shall I remind you about?")
            text = str(input())
            print("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            print(text)
        
        elif "game" in inp:
            import snake_pygame
            continue

        elif "news" in inp:
            latestnews()
            continue
        
        elif "app" in inp:
            app()
            continue

        else:
            count = 0
            if(count == 0):
                for tg in data["intents"]:
                    if inp in map(lower_1, tg["patterns"]):
                        count = 0
                        responses = tg["responses"]
                        print(random.choice(responses))
                        break
                    count = 1

            if(count == 1):
                print("I didn't get that, Try again")
            

chat()
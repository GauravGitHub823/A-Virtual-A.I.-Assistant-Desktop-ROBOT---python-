import os
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import smtplib
import pywhatkit
import keyboard
import pyjokes
import pyautogui
import requests
import pytz
import geocoder
from bs4 import BeautifulSoup
from googletrans import Translator
from PyDictionary import PyDictionary as dicts
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import folium
from opencage.geocoder import OpenCageGeocode


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    print(" ")
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except:
        print("Say that again please...")
        return "none"
    return query

################################## Speaking, Listening, & Wishing ###################################=====>>

def start():
    speak("Initializing system")
    speak("Starting all system applications")
    speak("Installing & checking all drivers")
    speak("Examining all the core processor")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    time.sleep(2)
    speak("All drivers are running up")
    speak("All systems have been activated")
    speak("Now I am online Sir")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning Sir!")
        speak("Good Morning Sir!")
    elif 12 <= hour < 16:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif 16 <= hour < 19:
        print("Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print("Good Night Sir!")
        speak("Good Night Sir!")
    speak("Allow me to introduce myself. I am Jarvis, A virtual artificial intelligence and I am here to assist you with the variety of tasks as best as I can, 24 hours in a day, 7 days in a week. System is now fully operational.")
    print("Please tell me, how may I help you.")
    speak("Please tell me, how may I help you.")

################################## Speaking, Listening, & Wishing ###################################=====>>


#######################################=====>> [{(\-_+_-/)}] <<=====########################################
def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"User said:{query}\n")
    except:
        print("Say that again please...")
        return "none"
    return query

def Trans():
    try:
        speak("Tell me the line sir!")
        line = TakeHindi()
        trans = Translator()
        result = trans.translate(line)
        Text = result.text
        print(f"Translation: {Text}")
        speak(f"The translation of this line is: {Text}")
    except:
        speak("Please Say again")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('gauravmeetbhu123@gmail.com','gauravmeetbhu')
        server.sendmail('gauravmeetbhu123@gmail.com',to,content)
        server.close()
    except:
        speak("Please tell me again Sir")

def YouTubeAuto():
    speak("Whats your command")
    comm = takeCommand()
    try:
        if 'pause' in comm:
            keyboard.press('k')

        elif 'play' in comm:
            keyboard.press('k')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'un mute' in comm:
            keyboard.press('m')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'back screen' in comm:
            keyboard.press('f')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'film mode' in comm:
            keyboard.press('t')

        elif 'normal mode' in comm:
            keyboard.press('t')
    except:
        speak("Please tell me again Sir")

    speak("Done Sir")

def ChromeAuto():
    speak("Whats your command")
    command = takeCommand()
    try:
        if 'open tab' in command:
            keyboard.press_and_release('Ctrl + t')

        elif 'close tab' in command:
            keyboard.press_and_release('Ctrl + w')

        elif 'open window' in command:
            keyboard.press_and_release('Ctrl + n')

        elif 'close window' in command:
            keyboard.press_and_release('Ctrl + Shift + w')

        elif 'open history' in command:
            keyboard.press_and_release('Ctrl + h')
    except:
        speak("Please tell me again Sir")

def Dictionary():
    speak("Activated Dictionary")
    speak("Tell me the problem")
    prob = takeCommand()

    try:
        if 'meaning' in prob:
            prob = prob.replace("what is meaning of ","")
            result = dicts.meaning(prob)
            speak(f"the meaning of {prob} is {result}")
            print(f"the meaning of {prob} is {result}")

        elif 'synonym' in prob:
            prob = prob.replace("what is synonym of ","")
            result = dicts.meaning(prob)
            speak(f"the synonym of {prob} is {result}")
            print(f"the synonym of {prob} is {result}")

        elif 'antonym' in prob:
            prob = prob.replace("what is antonym of ","")
            result = dicts.meaning(prob)
            speak(f"the antonym of {prob} is {result}")
            print(f"the antonym of {prob} is {result}")
    except:
        speak("Please tell me the correct name")
        print("Please tell me the correct name")

    speak("Exit Dictionary")

def ScreenShot():
    try:
        speak("Ok sir, what should i name that file")
        path = takeCommand()
        pathname = path + ".png"
        path1 = "D:\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\Image\\Screen Shot\\" + pathname
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\Image\\Screen Shot\\")
        speak("Here is your Screenshot")
    except:
        speak("Your image is not saved")
        print("Your image is not saved")

def DateConverter(query):
    try:
        Date = query.replace(" and ","-")
        Date = Date.replace(" and ","-")
        Date = Date.replace(" and ","-")
        Date = Date.replace(" ","")
        return str(Date)
    except:
        speak("Please tell me again Sir")

def Temperature():
    speak("tell me the name of place")
    search = takeCommand()
    try:
        url = f"https://www.google.com/search?q={search} temperature"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div", class_='BNeawe').text
        print(f"The temperature of {search} is {temperature}")
        speak(f"The temperature of {search} is {temperature}")
    except:
        speak("Please tell me the correct name of place")

def TimeZone():
    speak("single or double")
    command = takeCommand()

    try:
        if 'single' in command:
            speak("tell me the name of place")
            place = takeCommand()
            print(place)
            country_time_zone = pytz.timezone(f"{place}")
            country_time = datetime.datetime.now(country_time_zone)
            print(country_time.strftime(f"{place} => Date: %d-%m-%y & Time: %H:%M:%S"))
            speak(country_time.strftime(f"Date & Time of {place} is %d-%m-%y &  %H:%M:%S"))

        elif 'double' in command:
            speak("tell me the name of continent")
            continent = takeCommand()
            print(continent)
            speak("tell me the name of place")
            place = takeCommand()
            print(place)
            country_time_zone = pytz.timezone(f"{continent}/{place}")
            country_time = datetime.datetime.now(country_time_zone)
            print(country_time.strftime(f"{continent}/{place} => Date: %d-%m-%y & Time: %H:%M:%S"))
            speak(country_time.strftime(f"Date & Time of {continent}/{place} is %d-%m-%y &  %H:%M:%S"))
    except:
        print("Unknown place")
        speak("Please tell correct name of place")

def My_location():

    try:
        op = "https://www.google.co.in/maps/place/Varanasi,+Uttar+Pradesh/@25.3301947,82.9179572,11.73z/data=!4m5!3m4!1s0x398e2db76febcf4d:0x68131710853ff0b5!8m2!3d25.3176452!4d82.9739144?hl=en"
        print("Checking...")
        speak("Checking...")
        webbrowser.open(op)

        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        city = geo_d['city']
        country = geo_d['country']
        print(f"City: {city} | Country: {country}")
        speak(f"Sir, You are now in City {city} of Country {country}")
    except:
        speak("Unable to find your location Sir")

def locate():
    try:
        speak(f"Please enter mobile number you want to search")
        mobileNo = input("Mobile No. with country code : ")
        mobileNo = phonenumbers.parse(mobileNo)
        location = geocoder.description_for_number(mobileNo, "en")

        key = '307a190cdf094afaa6c96906a27d4aca'
        geo = OpenCageGeocode(key)
        query = str(location)
        results = geo.geocode(query)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)
        myMap.save("D:\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\Image\\Location.html")

        print("Time Zone :",timezone.time_zones_for_number(mobileNo))
        print("SIM :",carrier.name_for_number(mobileNo, "en"))
        print(f"Country: {location}")
        print("Valid Mobile Number :", phonenumbers.is_valid_number(mobileNo))
        print("Checking possibility of number :", phonenumbers.is_possible_number(mobileNo))
        print(f"Latitude: {lat} & Longitude: {lng}")


        speak(timezone.time_zones_for_number(mobileNo))
        speak(carrier.name_for_number(mobileNo,"en"))
        speak(geocoder.description_for_number(mobileNo,"en"))

        if phonenumbers.is_valid_number(mobileNo):
            speak("Valid Mobile Number")
        else:
            speak("Invalid Mobile Number")

        if phonenumbers.is_possible_number(mobileNo):
            speak("Possible number")
        else:
            speak("Impossible number")

        speak(f"Latitude is {lat} & Longitude is {lng}")
    except:
        speak("Unable to find the location of your given number")

def weather():
    try:
        speak("Please tell me the name of place")
        city = takeCommand()
        print(city)
        print('Displaying Weather report:' + city)

        url = 'https://wttr.in/{}'.format(city)
        res = requests.get(url)
        print(res.text)
        speak(f"This is Weather report for {city}")
    except:
        speak("Please tell me the correct name of place")

#######################################=====>> [{(\-_+_-/)}] <<=====########################################

def Task_Gui():

    wishMe()

    while True:

        query = takeCommand().lower()

        if "hello" in query or "hey" in query or "hi" in query:
            speak("hello sir, may I help you with something.")

        elif "how are you" in query:
            speak("I am fine sir, what about you?")

        elif "thank you" in query or "thanks" in query:
            speak("It's my pleasure sir.")

        elif "goodbye" in query or "bye" in query:
            speak("Thanks for giving me the chance to help you, have a good day sir")

        elif "exit" in query or "quit" in query or "sleep" in query:
            speak("System is now closing. See you again sir. Bye Sir")
            exit()


    ################### SEARCH ###################=====>>

        elif 'wikipedia' in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Please tell me again Sir")

        elif 'website' in query or "websites" in query:
            try:
                speak("Ok Sir, Launching...")
                query = query.replace("website","")
                query = query.replace(" ","")
                web = 'https://www.' + query + '.com'
                webbrowser.open(web)
                speak("Launched!")
            except:
                speak("Please tell me again Sir")

    #########################################=====>>

        elif 'open google' in query:
            try:
                webbrowser.open("google.com")
            except:
                speak("Please tell me again Sir")

        elif 'google search' in query:
            try:
                speak("Searching Google...")
                query = query.replace("google search", "")
                pywhatkit.search(query)
                speak("Ok sir, This is what I found for your google search")
                speak("Done Sir")
            except:
                speak("Please tell me again Sir")

        elif 'google automate' in query:
            try:
                ChromeAuto()
            except:
                speak("Please tell me again Sir")

        elif 'open tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'close window' in query:
            keyboard.press_and_release('ctrl + shift + w')

        elif 'open history' in query:
            keyboard.press_and_release('ctrl + h')

    #########################################=====>>

        elif 'open youtube' in query:
            try:
                webbrowser.open("youtube.com")
            except:
                speak("Please tell me again Sir")

        elif 'youtube search' in query:
            try:
                speak("Searching Youtube...")
                query = query.replace("youtube search","")
                web = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(web)
                speak("Ok sir, This is what I found for your youtube search")
                speak("Done Sir")
            except:
                speak("Please tell me again Sir")

        elif 'youtube automate' in query:
            try:
                YouTubeAuto()
            except:
                speak("Please tell me again Sir")

        elif 'pause' in query:
            keyboard.press('k')

        elif 'play' in query:
            keyboard.press('k')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'un mute' in query:
            keyboard.press('m')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'back screen' in query:
            keyboard.press('f')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'normal mode' in query:
            keyboard.press('t')

    ################### SEARCH ###################=====>>

        elif 'joke' in query or "jokes" in query:
            try:
                get = pyjokes.get_joke()
                print(get)
                speak(get)
            except:
                speak("Please tell me again Sir")

        elif 'repeat word' in query or "repeat" in query or "word" in query or "word repeat" in query:
            try:
                speak("Speak Sir!")
                j = takeCommand()
                print(f"You said {j}")
                speak(f"You said {j}")
            except:
                speak("Please tell me again Sir")

        elif 'translator' in query or "translating" in query or "translators" in query:
            try:
                Trans()
            except:
                speak("Please tell me again Sir")

        elif 'dictionary' in query or "dictionaries" in query:
            try:
                Dictionary()
            except:
                speak("Please tell me again Sir")

        elif 'screenshot' in query or "screen shot" in query or "screen" in query or "shot" in query:
            try:
                ScreenShot()
            except:
                speak("Please tell me again Sir")

        elif 'temperature' in query or "temperatures" in query:
            try:
                Temperature()
            except:
                speak("Please tell me again Sir")

        elif 'time zone' in query or "zone" in query or "zones" in query:
            try:
                TimeZone()
            except:
                speak("Please tell me again Sir")

        elif 'time' in query or "times" in query:
            try:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Time : {strTime}")
                speak(f"Sir,the time is {strTime}")
            except:
                speak("Please tell me again Sir")

        elif 'date' in query or "dates" in query:
            try:
                date = datetime.date.today()
                print(f"Date : {date}")
                speak(f"Sir,date is {date}")
            except:
                speak("Please tell me again Sir")

        elif 'today' in query:
            try:
                day = datetime.datetime.now().strftime("%A")
                print(f"Today : {day}")
                speak(f"Sir,today is {day}")
            except:
                speak("Please tell me again Sir")

        elif 'open code' in query or "code" in query or "powershell" in query or "shell" in query:
            try:
                codePath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
                os.startfile(codePath)
            except:
                speak("Please tell me again Sir")

        elif 'email send' in query or "email" in query or "send email" in query:
            try:
                speak("What  should I say?")
                content = takeCommand()
                to = "gauravmeetbhu123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to find the email")

        elif "phone" in query or "mobile" in query or "telephone" in query:
            try:
                locate()
            except:
                speak("Please tell me again Sir")

        elif "my location" in query:
            try:
                My_location()
            except:
                speak("Please tell me again Sir")

        elif "weather" in query:
            try:
                weather()
            except:
                speak("Please tell me again Sir")

        elif "climate" in query:
            try:
                from Weather import forecast
                forecast()
            except:
                speak("Please tell me again Sir")

        elif "covid" in query or "corona" in query or "covid cases" in query or "corona cases" in query:
            try:
                from Covid import corona
                corona()
            except:
                speak("Please tell me again Sir")

        elif "simulation" in query or "Simulation" in query or "simulations" in query or "planet" in query or "planets" in query:
            from PlanetSimulation import planet
            planet()


    ############# Driver Drowsiness ##############=====>>
        elif "driver" in query or "drivers" in query or "drowsiness" in query or "driver drowsiness" in query:
            from GouravDriver import driver
            driver()
    ############# Driver Drowsiness ##############=====>>


    ################## NASA ######################=====>>
        elif "universe" in query or "space news" in query or "galaxy" in query:
            try:
                speak("Tell me the date of News extraction")
                Date = takeCommand()
                Value = DateConverter(Date)
                from NASA import NasaNews
                NasaNews(Value)
            except:
                speak("Please tell me again Sir")

        elif "space station" in query or "station" in query or "Space Station" in query:
            from NASA import Iss
            Iss()

        elif "solar system" in query or "solar" in query or "system" in query or "solar bodies" in query:
            try:
                from NASA import SolarBodies
                speak("Tell me the name of body")
                bod = takeCommand()
                body = bod.replace(" ","")
                Body = str(body)
                SolarBodies(body=Body)
            except:
                speak("Please tell me again Sir")

        elif "asteroid" in query or "asteroids" in query:
            try:
                from NASA import Astro
                speak("Tell me the initial date")
                initial = takeCommand()
                starts = DateConverter(initial)
                speak("Tell me the final date")
                final = takeCommand()
                end = DateConverter(final)
                Astro(starts, end)
            except:
                speak("Please tell me again Sir")
    ################## NASA ######################=====>>

        else: speak("Please tell me something Sir!!!")




if __name__ == '__main__':
    #start()
    Task_Gui()


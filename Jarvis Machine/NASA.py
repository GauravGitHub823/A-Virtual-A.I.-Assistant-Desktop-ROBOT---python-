
#==> https://api.nasa.gov/planetary/apod?api_key=bv4lnTIkbeTljS7IcLqWzl95fTRhz3q0djab5HAS <==#

import requests
import os
import pandas as pd
from PIL import Image
import pyttsx3
import random
import ISS_Info
import urllib.request
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")


Api_Key = "bv4lnTIkbeTljS7IcLqWzl95fTRhz3q0djab5HAS"


def NasaNews(Date):

    Speak("Extracting Data from NASA")
    try:
        Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

        Params = {'date': str(Date)}

        r = requests.get(Url,params=Params)

        Data = r.json()

        Info = Data['explanation']
        In = Info[0:300]

        Title = Data['title']

        Image_Url = Data['url']

        Image_r = requests.get(Image_Url)

        FileName = str(Date) + '.jpg'

        with open(FileName,'wb') as f:

            f.write(Image_r.content)

        Path_1 = "D:\\Gourav(M.Sc.-CSA)\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\" + str(FileName)

        Path_2 = "D:\\Gourav(M.Sc.-CSA)\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\Image\\NasaDataBase\\" + str(FileName)

        os.rename(Path_1,Path_2)

        img = Image.open(Path_2)
        img.show()

        Speak(f"Title : {Title}")
        Speak(f"According to NASA : {In}")
    except:
        print(f"Wrong date: {Date}")
        Speak("Please tell me the correct date")

def SolarBodies(body):

    try:
        import cv2
        cap = cv2.VideoCapture("D:\\Gourav(M.Sc.-CSA)\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\SolarSystem.webm")

        while True:
            ret, frame = cap.read()

            frame = cv2.resize(frame, (1500, 770))
            cv2.imshow("Planet", frame)

            k = cv2.waitKey(100)

            if k == ord("x"):
                break

        cap.release()
        cv2.destroyAllWindows()

        url_1 = "https://api.le-systeme-solaire.net/rest/bodies/"

        r = requests.get(url_1)

        Data_1 = r.json()

        bodies = Data_1['bodies']

        Number = len(bodies)

        url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"

        rr = requests.get(url_2)

        Data_2 = rr.json()


        mass = Data_2['mass']['massValue']
        volume = Data_2['vol']['volValue']
        density = Data_2['density']
        gravity = Data_2['gravity']
        escape = Data_2['escape']

        Speak(f"Number of bodies in Solar System : {Number}")
        Speak(f"Mass of {body} is {mass} Kg.")
        Speak(f"Gravity of {body} is {gravity} metre per second squared.")
        Speak(f"Escape Velocity of {body} is {escape} metre per second.")
        Speak(f"Density of {body} is {density} grams per cubic centimetre.")
    except:
        print(f"Wrong Body name: {body}")
        Speak("Please tell me the correct name of body present in this solar system")

def Astro(start_date,end_date):

    try:
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

        r = requests.get(url)

        Data = r.json()

        Total_Astro = Data['element_count']

        neo = Data['near_earth_objects']

        list__ = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        value = random.choice(list__)
        path = "D:\\Gourav(M.Sc.-CSA)\\PYCHARM\\PycharmWorkspace\\Jarvis Machine\\Image\\Solar Images" + str(value) + ".jpg"
        os.startfile(path)

        Speak(f"Total Asteroids between {start_date} and {end_date} is {Total_Astro}")

    except:
        Speak("Please tell me the correct date")
        print("Please tell me the correct date")

def Iss():

    try:
        response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
        print(response)
        obj = json.loads(response.read())
        lat = obj['iss_position']['latitude']
        long = obj['iss_position']['longitude']

        url_2 = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(long) + '#map=3/' + str(lat) + '/' + str(long)
        import webbrowser
        webbrowser.open_new_tab(url_2)

        # https://www.openstreetmap.org/?mlat=38.9212&mlon=-80.8151#map=3/38.92/-80.82

        url_1 = "http://api.open-notify.org/iss-now.json"
        df = pd.read_json(url_1)
        df['latitude'] = df.loc['latitude', 'iss_position']
        df['longitude'] = df.loc['longitude', 'iss_position']
        df.reset_index(inplace=True)
        print(df)

        details = ISS_Info.iss_people_in_space()
        print("There are currently {} astronauts in space".format(details['number']))
        x = details['number']
        Speak(f"There are currently {x} astronauts in international space station & there name is")
        for p in details['people']:
            print("Name: {} (Craft: {})".format(p['name'],p['craft']))
            y = p['name']
            Speak(y)
    except:
        Speak("I am unable to load the information from internet")


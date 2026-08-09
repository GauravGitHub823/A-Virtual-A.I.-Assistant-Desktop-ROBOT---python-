from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def forecast():
    root = Tk()
    root.title("Weather App")
    root.geometry("900x600+300+200")
    root.resizable(False,False)

    def getWeather():
        try:
            city = textfield.get()
            geolocator =Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

            home = pytz.timezone(result)
            local_time=datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            # Weather
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fa1da447e72c9b11038da8f413988c66"

            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            t.config(text=(temp,"°C"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))

            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
        except:
            messagebox.showerror("Weather App","Invalid Entry!!!")

    # Search Box
    Search_image = PhotoImage(file="search.png")
    myimage = Label(image=Search_image)
    myimage.place(x=30,y=30)

    textfield = tk.Entry(root,justify="center",width=17,font=("poppins",20,"bold"),bg="#404040",border=0,fg="white")
    textfield.place(x=75,y=40)
    textfield.focus()

    Search_icon = PhotoImage(file="search_icon.png")
    myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
    myimage_icon.place(x=400,y=43)

    # Logo
    logo_image = PhotoImage(file="logo.png")
    logo = Label(image=logo_image)
    logo.place(x=150,y=180)

    # Bottom Box
    Frame_image = PhotoImage(file="box.png")
    frame_myimage = Label(image = Frame_image)
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

    # Time
    name = Label(root,font=("arial",15,"bold"))
    name.place(x=30,y=120)
    clock=Label(root,font=("Helvetica",20))
    clock.place(x=30,y=160)

    # Label
    label1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
    label1.place(x=100,y=500)

    label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
    label2.place(x=230,y=500)

    label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
    label3.place(x=410,y=500)

    label4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
    label4.place(x=640,y=500)


    t = Label(font=("arial",70,"bold"),fg="#ee666d")
    t.place(x=400,y=150)
    c = Label(font=("arial",15,'bold'))
    c.place(x=400,y=400)

    w = Label(text="...",font=("arial",12,"bold"),bg="#1ab5ef")
    w.place(x=120,y=535)
    h = Label(text="...",font=("arial",12,"bold"),bg="#1ab5ef")
    h.place(x=280,y=535)
    d = Label(text="...",font=("arial",12,"bold"),bg="#1ab5ef")
    d.place(x=420,y=535)
    p = Label(text="...",font=("arial",12,"bold"),bg="#1ab5ef")
    p.place(x=670,y=535)


    root.mainloop()

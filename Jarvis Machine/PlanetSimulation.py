import tkinter

main_window = tkinter.Tk()

main_window.resizable(False,False)
main_window.title("Planet Simulation")

c = tkinter.Canvas(main_window, width=500, height=500)
c.pack()

radius = 100
sunX = 250
sunY = 250
moonX = 500 + radius
moonY = 250
darkness = 150

def planet():
    def draw_eclipse(cs):
        global sunX, sunY, moonX, moonY, darkness, radius
        cs.create_rectangle(-10, -10, 510, 510, fill=('#%02x%02x%02x' % (darkness, darkness, darkness)), width=0)
        cs.create_oval(sunX - radius, sunY - radius, sunX + radius, sunY + radius, fill="orange", width=0)
        cs.create_oval(moonX - (radius - 2), moonY - (radius - 2), moonX + (radius - 2), moonY + (radius - 2), fill="black", width=0)


    def clear(cs):
        cs.delete(tkinter.ALL)


    def repeat():
        global moonX, sunX, darkness, radius
        moonX = moonX - 1
        if abs(moonX - sunX) < (radius * 2):
            darkness = abs(moonX - sunX)
        else:
            darkness = (radius * 2)
        if moonX < -radius:
            moonX = 500 + radius
        c.delete(tkinter.ALL)
        draw_eclipse(c)

        main_window.after(50, repeat)


    main_window.after(0, repeat)

    main_window.mainloop()


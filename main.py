import customtkinter
import threading
import time
import random

app = customtkinter.CTk()
app.title('Gacha Gambling')
app.geometry("480x480")
app.resizable(0,0)

clicks = 0
inc = 1
upg1cost = 100
upg1lvl = 0
upg2cost = 20
upg2lvl = 0
upg3cost = 1000
upg3lvl = 0
duration = 2.2
auto_enables = 0
Num = 80
GambleCost = 1
end = False
purps = 0

#Gambling stuff#

box1 = customtkinter.CTkButton(app, text="", width=30, height=30)
box1.grid(row=2, column=1, sticky="nw", pady=55, padx=(20,0))

box2 = customtkinter.CTkButton(app, text="", width=30, height=30)
box2.grid(row=2, column=1, sticky="nw", pady=55, padx=(60,0))

box3 = customtkinter.CTkButton(app, text="", width=30, height=30)
box3.grid(row=2, column=1, sticky="nw", pady=55, padx=(100,0))

box4 = customtkinter.CTkButton(app, text="", width=30, height=30)
box4.grid(row=2, column=1, sticky="nw", pady=55, padx=(140,0))

box5 = customtkinter.CTkButton(app, text="", width=30, height=30)
box5.grid(row=2, column=1, sticky="nw", pady=55, padx=(180,0))

box6 = customtkinter.CTkButton(app, text="", width=30, height=30)
box6.grid(row=2, column=2, sticky="nw", pady=55, padx=(20,0))

box7 = customtkinter.CTkButton(app, text="", width=30, height=30)
box7.grid(row=2, column=2, sticky="nw", pady=55, padx=(60,0))

box8 = customtkinter.CTkButton(app, text="", width=30, height=30)
box8.grid(row=2, column=2, sticky="nw", pady=55, padx=(100,0))

box9 = customtkinter.CTkButton(app, text="", width=30, height=30)
box9.grid(row=2, column=2, sticky="nw", pady=55, padx=(140,0))

box10 = customtkinter.CTkButton(app, text="", width=30, height=30)
box10.grid(row=2, column=2, sticky="nw", pady=55, padx=(180,0))

#Clicking/Upg sys#
def clicked():
    global clicks
    global clicklab
    global inc
    clicks = clicks+inc
    clicklab.configure(text="Clicks : " +str(int(clicks)))

def autoclicker_value():
    global duration
    global auto_enables
    if auto_enables == 1:
        while True:
            clicked()
            time.sleep(duration)

boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9,box10]

def Gacha():
    global purps
    for i in range(10):
        G = random.randint(1, Num)
        if G == random.randint(1, Num):
            print("🟪")
            purps += 1
            purp.configure(text="Purples gained : " + str(purps))
            boxes[i].configure(fg_color="#7a2cd4", hover_color="#7a2cd4")
        else:
            r = random.randint(1, 2)
            if r == 2:
                print("🟨")
                boxes[i].configure(fg_color="#ffcb33", hover_color="#ffcb33")
            else:
                print("🟦")
                boxes[i].configure(fg_color="#1F6AA5", hover_color="#1F6AA5")
    return

Autoclicker = threading.Thread(target=autoclicker_value)
Autoclicker.daemon = True



def Upgrade1():
    global inc
    global clicks
    global clicklab
    global upg1cost
    global upg1
    global upg1lvl
    if upg1lvl >= 10:
        print("Max level reached")
        upg1.configure(text="Increase value : Max lvl")

    else:
        if clicks >= upg1cost:
            print("Clicks +1 added")
            inc = inc +2
            clicks = clicks - upg1cost
            upg1cost = upg1cost*2
            clicklab.configure(text="Clicks : " +str(clicks))
            upg1lvl = upg1lvl +1
            if upg1lvl >=10:
                upg1.configure(text="Increase value : Max lvl")
            else:
                upg1.configure(text="Increase value : Cost "+str(upg1cost))
def gamble_start():
    global GambleCost, clicks
    if clicks >= GambleCost:
        clicks = clicks - GambleCost
        clicklab.configure(text="Clicks : " +str(clicks))
        Gambling = threading.Thread(target=Gacha)
        Gambling.daemon = True
        global end
        end = False
        Gambling.start()


def Upgrade2():
    global inc
    global clicks
    global clicklab
    global upg2cost
    global upg2
    global upg2lvl
    global auto_enables
    global duration
    if upg2lvl >= 20:
        print("Max level reached")
        upg2.configure(text="Auto Clicker : Max lvl")

    else:
        if clicks >= upg2cost:
            if auto_enables == 0:
                auto_enables = 1
                print("Auto clicker enabled/ upgraded")
                clicks = clicks - upg2cost
                clicklab.configure(text="Clicks : " +str(int(clicks)))
                upg2cost = upg2cost*1.5
                upg2.configure(text="Auto Clicker : Cost "+str(int(upg2cost)))
                duration = duration - 0.1
                Autoclicker.start()

            else:
                print("Auto clicker enabled/ upgraded")
                clicks = clicks - upg2cost
                clicklab.configure(text="Clicks : " +str(int(clicks)))
                upg2cost = upg2cost*1.5
                duration = duration - 0.1
                print("New timeout : " +str(duration))

                if upg2lvl >=20:
                    upg2.configure(text="Increase value : Max lvl")
                else:
                    upg2.configure(text="Auto Clicker : Cost "+str(int(upg2cost)))


#TO DO#
#def Upgrade3():
    #global upg3lvl, upg3cost, upg3, Num
    #if upg3lvl  >= 10:
        #print("Max level reached")
        #upg3.configure(text="Auto Clicker : Max lvl")
    #else:
        #if clicks >= upg3cost:
            #clicks = clicks - upg3cost
            #Num = Num -5
            #print("Not finished")


#Buttons#

clicker = customtkinter.CTkButton(app, width=200, height=200, text="", corner_radius=100, command=clicked)
clicker.grid(row=1, column=1, pady=0, padx = 20)

upg1 = customtkinter.CTkButton(app, text="Increase value : Cost 100", command=Upgrade1, width=200)
upg1.grid(row=1, column=2, pady=(5,120), padx=20, sticky = "e")

upg2 = customtkinter.CTkButton(app, text="Auto Clicker : Cost 20", width=200, command=Upgrade2)
upg2.grid(row=1, column=2, pady=120, padx=20, sticky = "e")

upg3 = customtkinter.CTkButton(app, text="Increase Luck : Cost 200", width=200)
upg3.grid(row=1, column=2, pady=(120,5), padx=20, sticky = "e")

gamble = customtkinter.CTkButton(app, text="GAMBLE!!!! : Cost 500", width=200, command=gamble_start)
gamble.grid(row=2, column=1,pady = 170, padx=20, sticky = "n")

#Labels#

clicklab = customtkinter.CTkLabel(app, text="Clicks : 0", height=20)
clicklab.grid(row=1, column=1, sticky="n")

purp = customtkinter.CTkLabel(app, text="Purples gained : 0")
purp.grid(row=2, column=2, sticky="n", pady=170)





app.mainloop()
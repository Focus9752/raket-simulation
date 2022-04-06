from numpy import number
import math
import matplotlib.pyplot as plt
import sys

def simulate():
    tList = []
    yList = []
    vList = []
    aList = []

    rocketType = "a"

    if input("Vælg rakettype (a/b): ").lower() == "a":
        m_tom = 0.090
        m_brænd = 0.00656
        Fm = 6
        t_brænd = 0.4
        rocketType = "a"
    else:
        m_tom = 0.090
        m_brænd = 0.00798
        Fm = 4
        t_brænd = 1.1
        rocketType = "b"

    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))
    
    m = m_tom + m_brænd
    #R er raten hvormed raketten taber masse når motoren brænder
    R = m_brænd / t_brænd
    g = -9.82
    #k1 er rakettens luftmodstandsfaktor før faldskærmen er udfoldet
    k1 = 0.5 * 0.0008294 * 0.04 * 1.225
    #k2 er rakettens luftmodstandsfaktor når faldskærmen er udfoldet
    k2 = 0.5 * 0.08 * 0.5 * 1.225
    k = k1
    v, y, t = 0, 0, 0

    while(True):
        #Beregn ændringen i masse
        dm = R * dt
        m = m - dm
        #Hvis motoren er færdig med at brænde
        if t >= t_brænd:
            #Sæt masse til masse af tom raket
            m = m_tom
            #Sæt motorkraft til 0 N
            Fm = 0
            #"Udløs faldskærmen" når raketten begynder at falde nedad
            if rocketType == "a" and t >= 4.8:
                k = k2
            elif rocketType == "b" and t >= 5.5:
                k = k2
        #Tyngdekraften
        Ft = m * g
        #Resulterende kraft
        Fres = Fm + Ft
        #Læg luftmodstand til resulterende kraft - men tjek fortegn
        if v >= 0:
            Fres -= k * v**2
        else:
            Fres += k * v**2
        a = Fres / m
        v = v + a * dt
        y = y + v * dt
        t = t + dt 
        #Stop simulationen når raketten rammer jorden        
        if y < 0: break
        #Vis værdierne i konsollen
        print("t = % .2f s, v = % .2f m/s, y = % .2f m" % (t, v, y))
        #Gem værdierne i nogle lister
        tList.append(t)
        yList.append(y)
        vList.append(v)
        aList.append(a)

    
    plot1 = plt.figure(1)
    plt.plot(tList,aList)
    plt.xlabel("t / s")
    plt.ylabel("acceleration / m/s^2")
    plt.title("Rakettens acceleration")
    #plt.show()

    plot2 = plt.figure(2)
    plt.plot(tList,vList)
    plt.xlabel("t / s")
    plt.ylabel("hastighed / m/s")
    plt.title("Rakettens hastighed")
    #plt.show()

    plot3 = plt.figure(3)
    plt.plot(tList,yList)
    plt.xlabel("t / s")
    plt.ylabel("højde / m")
    plt.title("Rakettens højde")
    plt.show()

    sys.exit()

simulate()

#Motortype A

#Fm = 4 N
#t_brænd = 1.3 s

#Raket masse tom omkring 0.09126 kg
#Masse af brændstof 0.006562 kg

#Motortype B

#Fm = 6 N
#t_brænd = 0.6 s

#Raket masse tom omkring 0.09060 kg
#Masse af brændstof 0.00798 kg


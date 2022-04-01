from numpy import number
import math
import matplotlib.pyplot as plt

def model1():
    Fm = float(input("Angiv motorkraften i N: "))
    m = float(input("Angiv rakettens masse i kg: "))
    g = 9.82
    Ft = g * m
    v = float(input("Angiv begyndelsesfarten i m/s: "))
    y = float(input("Angiv begyndelseshøjden i m: "))
    t = float(input("Angiv starttid i s: "))
    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))

    numberOfRuns = int(input("Angiv antal gennemløb: "))
    showSteps = False
    if input("Vis trinvis simulering? (j/n): ").lower() == "j":
        showSteps = True

    for i in range(numberOfRuns):
        if (showSteps):
            Fres = Fm - Ft
            a = Fres / m
            v = v + a * dt
            y = y + v * dt
            t = t + dt
            print("t = % .2f s, v = % .2f m/s, y = % .2f m" % (t, v, y))

def model2():
    Fm = float(input("Angiv motorkraften i N: "))
    m_tom = float(input("Angiv rakettens masse uden brændstof i kg: "))
    m_brænd = float(input("Angiv massen af rakettens brændstof i kg: "))
    t_brænd = float(input("Angiv brændselstiden i s: "))
    m = m_tom + m_brænd
    R = m_brænd / t_brænd
    g = 9.82
    Ft = g * m
    v = float(input("Angiv begyndelsesfarten i m/s: "))
    y = float(input("Angiv begyndelseshøjden i m: "))
    t = float(input("Angiv starttid i s: "))
    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))

    numberOfRuns = int(input("Angiv antal gennemløb: "))
    showSteps = False
    if input("Vis trinvis simulering? (j/n): ").lower() == "j":
        showSteps = True

    for i in range(numberOfRuns):
        if (showSteps):
            dm = R * dt
            m = m - dm
            if t >= t_brænd:
                m = m_tom
                Fm = 0
            Fres = Fm - Ft
            a = Fres / m
            v = v + a * dt
            y = y + v * dt
            t = t + dt
            print("t = % .2f s, v = % .2f m/s, y = % .2f m" % (t, v, y))

def model3():
    tList = []
    yList = []

    # Fm = float(input("Angiv motorkraften i N: "))
    Fm = 6
    #m_tom = float(input("Angiv rakettens masse uden brændstof i kg: "))
    m_tom = 0.09138
    #m_brænd = float(input("Angiv massen af rakettens brændstof i kg: "))
    m_brænd = 0.00798
    #t_brænd = float(input("Angiv brændselstiden i s: "))
    t_brænd = 0.6
    m = m_tom + m_brænd
    R = m_brænd / t_brænd
    g = -9.82
    A = 0.000962
    cw = 0.5
    rho_luft = 1.225
    k = 0.5 * A * cw * rho_luft
    #v = float(input("Angiv begyndelsesfarten i m/s: "))
    #y = float(input("Angiv begyndelseshøjden i m: "))
    #t = float(input("Angiv starttid i s: "))
    v, y, t = 0, 0, 0
    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))

    numberOfRuns = int(input("Angiv antal gennemløb: "))
    showSteps = False
    if input("Vis trinvis simulering? (j/n): ").lower() == "j":
        showSteps = True

    for i in range(numberOfRuns):
        if (showSteps):
            if t >= t_brænd:
                m = m_tom
                Fm = 0
            dm = R * dt
            m = m - dm
            Ft = m * g
            if v <= 0:
                k = 0.5 * 0.1257 * 0.8 * 1.225
            Fres = Fm + Ft - math.sin(v) * k * v**2
            a = Fres / m
            v = v + a * dt
            y = y + v * dt
            if y < 0: break
            t = t + dt
            tList.append(t)
            yList.append(y)
            print("t = % .2f s, v = % .2f m/s, y = % .2f m" % (t, v, y))
    
    plt.plot(tList,yList)
    plt.xlabel("t / s")
    plt.ylabel("højde / m")
    plt.show()

modelChoice = input("Vælg model (1/2/3): ").lower()
if modelChoice == "1":
    model1()
elif modelChoice == "2":
    model2()
else:
    model3()

#Med motortype A

#Fm =6 N
#t_brænd = 0.6 s

#Raket masse tom omkring 0.09138 kg
#Masse af brændstof 0.00798 kg



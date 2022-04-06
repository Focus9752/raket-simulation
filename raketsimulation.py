from numpy import number
import math
import matplotlib.pyplot as plt
import sys

def simulate():
    tList = []
    yList = []

    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))
    simulatedTime = int(input("Angiv simuleret tid i s: "))
    
    Fm = 6
    m_tom = 0.09138
    m_brænd = 0.00798
    m = m_tom + m_brænd
    t_brænd = 0.6
    #R er raten hvormed raketten taber masse når motoren brænder
    R = m_brænd / t_brænd
    g = -9.82
    #k1 er rakettens luftmodstandsfaktor før faldskærmen er udfoldet
    k1 = 0.5 * 0.000962 * 0.5 * 1.225
    #k2 er rakettens luftmodstandsfaktor når faldskærmen er udfoldet
    k2 = 0.5 * 0.1257 * 0.8 * 1.225
    k = k1
    v, y, t = 0, 0, 0

    while(True):
        dm = R * dt
        m = m - dm
        if t >= t_brænd:
            m = m_tom
            Fm = 0
            if v > 0:
                k = k2
        Ft = m * g
        Fres = Fm + Ft
        if v >= 0:
            Fres -= k * v**2
        else:
            Fres += k * v**2
        a = Fres / m
        v = v + a * dt
        y = y + v * dt
        t = t + dt
        tList.append(t)
        yList.append(y)
        if 17.78 <= v <= 19.55:
            pass
        print("t = % .2f s, v = % .2f m/s, y = % .2f m" % (t, v, y))
        if y <= 0: break
        if t >= simulatedTime: break
            
    
    plt.plot(tList,yList)
    plt.xlabel("t / s")
    plt.ylabel("højde / m")
    plt.title("Simulering af raket")
    plt.show()

    sys.exit()

simulate()

#Motortype A

#Fm = 6 N
#t_brænd = 0.6 s

#Raket masse tom omkring 0.09138 kg
#Masse af brændstof 0.00798 kg

#Motortype B

#Fm = 4 N
#t_brænd = 1.3 s

#Raket masse tom omkring 0.09138 kg
#Masse af hel motor 0.01819 kg



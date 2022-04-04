from numpy import number
import math
import matplotlib.pyplot as plt
import sys

def simulate():
    tList = []
    yList = []

    dt = float(input("Angiv tidsskridtsstørrelsen i s: "))
    simulatedTime = int(input("Angiv simuleret tid i s: "))

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
    k1 = 0.5 * 0.000962 * 0.5 * 1.225
    k2 = 0.5 * 0.1257 * 0.8 * 1.225
    k = k1
    
    #v = float(input("Angiv begyndelsesfarten i m/s: "))
    #y = float(input("Angiv begyndelseshøjden i m: "))
    #t = float(input("Angiv starttid i s: "))
    v, y, t = 0, 0, 0
    

    while(True):
        if t >= t_brænd:
            m = m_tom
            Fm = 0
            if k < k2:
                #Antager at faldskærmen åbner sig på 3s
                k += (k2 - k1) * dt / 3
            if k >= k2:
                k = k2
        dm = R * dt
        m = m - dm
        Ft = m * g
        Fres = Fm + Ft - math.sin(v) * k * v**2
        a = Fres / m
        v = v + a * dt
        y = y + v * dt
        t = t + dt
        tList.append(t)
        yList.append(y)
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

#Med motortype A

#Fm = 6 N
#t_brænd = 0.6 s

#Raket masse tom omkring 0.09138 kg
#Masse af brændstof 0.00798 kg



tor=int(input("Tors tid ? "))
mor=int(input("Mors tid ? "))

y=40

if tor>mor:
    x=tor/mor
    t=0
    m=0
    while y>1:
        y-=(1+x*1)
        t+=1
        m+=1*x
    print("Svar: Tor ", int(t), "Mor ", int(m))
elif mor>tor:
    x=mor/tor
    t=0
    m=0
    while y>1:
        y-=(1+x*1)
        t+=1*x
        m+=1
    print("Svar: Tor ", int(t), "Mor ", int(m))

else:
    print("Savr:Tor 20, Mor 20")

import sys
import subprocess
import time
def scansione(tipo=0):

        if tipo==0:
            risultato = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=BSSID"])
        else:
            risultato = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=BSSID"])
        risultato = risultato.decode("ascii") 
        risultato = risultato.replace("\r","")
        ssidScan = risultato.split("\n")
        
        ssidScan = ssidScan[4:]
        ssids = []
        x = 0

        while x < len(ssidScan):
            if "BSSID" in ssidScan[x]:
                print(ssidScan[x],end="")
            else:
            
                if "SSID" in ssidScan[x]:
                    print(ssidScan[x])
                if "Signal" in ssidScan[x]:
                    print(ssidScan[x])
            x += 1

print ("CLEME wifi scanner r1.0 ",end="")
tipo=0
tempo=30
if len(sys.argv)>=1:
    tipo=sys.argv[1]
    print(" scan your ssid")
else:
    print(" scan all ssid")

if len(sys.argv)>2:
    tempo=int(sys.argv[2])

while True:
    scansione(tipo)
    time.sleep(tempo)
    print("_________________________________________________________________________________") 

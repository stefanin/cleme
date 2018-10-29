import subprocess
import time
def scansione():

        risultato = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=BSSID"])
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

print ("CLEME wifi scanner r1.0")
while True:
    scansione()
    time.sleep(30)
    print("_________________________________________________________________________________") 

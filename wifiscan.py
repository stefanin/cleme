import subprocess
risultato = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=BSSID"])
risultato = risultato.decode("ascii") 
risultato = risultato.replace("\r","")
ssidScan = risultato.split("\n")
#print ("totale")
#print (ssidScan)
#print ("parziale")
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
 

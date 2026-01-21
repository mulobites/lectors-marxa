
import tkinter as tk
from tkinter import ttk
import time
import json
import paho.mqtt.client as paho
from paho import mqtt
from urllib.request import urlretrieve


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.callback_api_version.VERSION2
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username="marxa", password="marxaUEC1")
client.connect("fd483681811b46998f1720ee6faf6416.s1.eu.hivemq.cloud", 8883)
client.loop_start()

def on_connect(client, userdata, flags, rc, blue):
    print("Connected")

def on_subscribe(client, userdata, mid, reasoncodes, properties):
    print("Subscribed")

def on_message(client, userdata, msg):
    print (msg.payload)
    contador=json.loads(msg.payload)
    print(contador)
    for x in contador:
        index=contador.index(x)
        numdorsal = tk.Label(sort2)
        numdorsal.config(text=contador[index], font=("Arial", 20))
        numdorsal.grid(row=(contador.index(x)+1), column=1, sticky="nsEW")



client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message

client.subscribe(topic="resultats", qos=1)
#llistacontrols = ["gracia", "sants", "can cuias", "papiol", "olesa"]

file_url="https://raw.githubusercontent.com/mulobites/lectors-marxa/refs/heads/main/controls.json"
filename = "controls.json"

urlretrieve(file_url, filename)




with open("controls.json") as llistacontrols:
    llistacontrols=json.loads(llistacontrols.read())

with open("dorsals.json") as llistadorsals:
    llistadorsals=json.loads(llistadorsals.read())

print(llistadorsals)
print(llistacontrols)


def llegirxip(event):
    xip["text"]=xip["text"]+event.char
    print(xip["text"])



def principal(event):
    if xip["text"] in llistadorsals:
        dorsal["text"]=llistadorsals[xip["text"]]
        triada=(dorsal["text"], control.get(), hora["text"])
        quartet=(dorsal["text"], xip["text"], control.get(), hora["text"])
    else:
        print("no llegeix")
        triada=(xip["text"], control.get(), hora["text"])
        quartet=("desconegut", xip["text"], control.get(), hora["text"])
    print(quartet)
    triadaj=json.dumps(triada)
    quartetj=json.dumps(quartet)
    file = open("resultats2026.txt", "a")
    file.write(control.get())
    file.write(',')
    file.write(dorsal["text"])
    file.write(',')
    file.write(xip["text"])
    file.write(',')
    file.write(time.strftime("%H:%M:%S"))
    file.write('\n')
    file.close()
    client.publish(topic="marxa", payload=triadaj, qos=1)
    xip["text"]=""






marc = tk.Tk()
marc.title('Barcelona-Montserrat')
marc.geometry('800x480')
marc.bind("<Key>",llegirxip)
marc.bind("<Return>", principal)
marc.columnconfigure(0, weight=1)
marc.rowconfigure(0, weight=1)
marc.rowconfigure(1, weight=9)


xip=tk.Label(marc, text="")



entrades = tk.Frame(marc)
entrades.config()
entrades.grid(row=0, column=0, sticky="nsew")
entrades.columnconfigure (0, weight=6)
entrades.columnconfigure (1, weight=2)
entrades.columnconfigure (2, weight=1)
entrades.columnconfigure (3, weight=1)
entrades.rowconfigure (0, weight=1)

hora=tk.Label(entrades)
hora.config(font=("Arial", 30))
hora.grid(row=0, column=1, sticky="nsew")

control=ttk.Combobox(entrades, values=llistacontrols, state="readonly")
control.config(text="coll d'olesa", font=("Arial", 30))
control.grid(row=0, column=0, sticky="NSEW")

gps = tk.Label(entrades)
gps.config(bg='red', text="gps", font=("Arial", 15))
gps.grid(row=0, column=2, sticky="nsew")

xarxa=tk.Label(entrades)
xarxa.config(bg='yellow', text="xar", font=("Arial", 15))
xarxa.grid(row=0, column=3, sticky="nsew")

sortides=tk.Frame(marc)
sortides.config()
sortides.columnconfigure(0, weight=6)
sortides.columnconfigure(1, weight=4)
sortides.rowconfigure(0, weight=1)
sortides.grid(row=1, column=0, sticky="nsew")

sort1=tk.Frame(sortides)
sort1.config()
sort1.columnconfigure(0, weight=1)
sort1.columnconfigure(1, weight=3)
sort1.rowconfigure(0, weight=1)
sort1.grid(row=0, column=0, sticky="nsew")

etdorsal = tk.Label(sort1)
etdorsal.config(text="dorsal:", font=("Arial", 30))
etdorsal.grid(row=0, column=0, sticky="new")

dorsal=tk.Label(sort1)
dorsal.config(text="dorsal", font=("Arial", 50))
dorsal.grid(row=0, column=1, sticky="new")

sort2=tk.Frame(sortides)
sort2.config()
sort2.columnconfigure(0, weight=3)
sort2.columnconfigure(1, weight=2)
sort2.grid(row=0, column=1, sticky="nsew")

total=tk.Label(sort2)
total.config(text="total:", font=("Arial", 15))
total.grid(row=0, column=0, sticky="nsew")

numtotal=tk.Label(sort2)
numtotal.config(text=len(llistadorsals), font=("Arial", 15))
numtotal.grid(row=0, column=1, sticky="nsew")
for x in  llistacontrols:
    nomdorsal = tk.Label(sort2)
    nomdorsal.config(text=x, font=("Arial", 20))
    nomdorsal.grid(row=(llistacontrols.index(x)+1), column=0, sticky="nsew")

    #numdorsal = tk.Label(sort2)
    #numdorsal.config(bg='yellow', text="123", font=("Arial", 20))
    #numdorsal.grid(row=(llistacontrols.index(x)+1), column=2, sticky="nsEW")




def tick():
    temps=time.strftime("%H:%M:%S")
    hora.config(text=temps)
    hora.after(500, tick)

tick()





marc.mainloop()

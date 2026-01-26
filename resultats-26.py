import streamlit as st
import json
import pandas as pd
import paho.mqtt.client as paho
from paho import mqtt



st.header ("resultats 2026")

with open("controls.json") as llistacontrols:
    llistacontrols=json.loads(llistacontrols.read())

with open("dorsals.json") as llistadorsals:
    llistadorsals=json.loads(llistadorsals.read())

resultats={}
for d in llistadorsals:
    v=llistadorsals[d]
    resultats[v]={}
    for c in llistacontrols:
       resultats[v][c]=""


with open("resultats.json") as llistaresultats:
    resultats=json.loads(llistaresultats.read())


contador={}
for d in llistadorsals:
    contador[d]=0

espai=st.empty()



respd=pd.DataFrame.from_dict(resultats).transpose()
espai.table(resultats)
espai.write("respd")
espai.table(respd)

espai.write("contador")
espai.table(contador)

def on_connect(client, userdata, flags, rc, blue):
    print("Connected")
    st.write("Connected")

def on_subscribe(client, userdata, mid, reasoncodes, properties):
    print("Subscribed")
    st.write("Subscribed")

def on_message(client, userdata, msg):
    espai.empty()
    triada=json.loads(msg.payload)
    espai.table(triada)
    resultats[triada[0]][triada[1]]=triada[2]
    with open("resultats.json", "w") as llistaresultats:
        json.dump(resultats, llistaresultats)
    respd=pd.DataFrame.from_dict(resultats).transpose()
    #respd.loc[triada[0], triada[1]]=triada[2]
    espai.table(respd)
    #contador=list(len(resultats))
    #st.table(contador)
    #client.publish(topic="resultats", payload=json.dumps(contador), qos=1)

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username="marxa", password="marxaUEC1")
client.connect("fd483681811b46998f1720ee6faf6416.s1.eu.hivemq.cloud", 8883)




client.subscribe("marxa", 1)


client.loop_forever()
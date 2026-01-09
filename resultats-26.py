import paho.mqtt.client as paho
from paho import mqtt
import streamlit as st
import json
import pandas as pd
import openpyxl as xl


with open("controls.json") as llistacontrols:
    llistacontrols=json.loads(llistacontrols.read())

with open("dorsals.json") as llistadorsals:
    llistadorsals=json.loads(llistadorsals.read())


resultats=pd.DataFrame(index=llistadorsals.values(), columns=llistacontrols)

st.write(resultats)
st.write(resultats.count())


def on_connect(client, userdata, flags, rc, blue):
    print("Connected")
    st.write("Connected")

def on_subscribe(client, userdata, mid, reasoncodes, properties):
    print("Subscribed")
    st.write("Subscribed")

def on_message(client, userdata, msg):
    triada=json.loads(msg.payload)
    resultats.loc[triada[0], triada[1]]=triada[2]
    st.write(resultats)
    contador=list(resultats.count())
    st.write(contador)
    client.publish(topic="resultats", payload=json.dumps(contador), qos=1)



client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username="marxa", password="marxaUEC1")
client.connect("fd483681811b46998f1720ee6faf6416.s1.eu.hivemq.cloud", 8883)




client.subscribe("marxa", 1)


st.header("resultats")



client.loop_forever()



import json

import streamlit as st
import pandas as pd

st.title("gestió de controls")

llistacontrols=json.loads(open("controls.json", "r").read())

with st.form(key="formcontrols"):
    nom=st.text_input("nom control")
    desa=st.form_submit_button("desa")
    if desa:
        llistacontrols.append(nom)
        with open("controls.json", "w") as llistacontrols2:
            json.dump(llistacontrols, llistacontrols2)

reset=st.button("reset")
if reset:
    llistacontrols=[]
    with open("controls.json", "w") as llistacontrols2:
        json.dump(llistacontrols, llistacontrols2)


st.table(llistacontrols)

st.title("gestio de dorsals")

with open("dorsals.json", "r") as f:
    dorsals=json.load(f)


with st.form(key="formdorsals"):
    numdorsals=st.text_input("num dorsals")
    xip=st.text_input("xip")
    intro=st.form_submit_button("desa")
    if intro:
        dorsals[xip]=numdorsals
        with open("dorsals.json", "w") as dorsals2:
            json.dump(dorsals, dorsals2)


reset2=st.button("reset2")
if reset2:
    dorsals={}
    with open("dorsals.json", "w") as f:
        json.dump(dorsals, f)

st.table(dorsals)

with open("resultats.json", "r") as r:
    resultat=json.load(r)


with open("dorsals.json", "r") as f:
    dorsals=json.load(f)

resultats=pd.DataFrame(index=dorsals.values(), columns=llistacontrols)



st.write("resultats")
st.write(resultats)

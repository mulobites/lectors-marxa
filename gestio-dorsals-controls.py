import json

import streamlit as st
import pandas as pd

llistacontrols=json.loads(open("controls.json", "r").read())

st.write("controls")
st.write(llistacontrols)

with open("dorsals.json", "r") as f:
    dorsals=json.load(f)
st.write ("dorsals")
st.write(dorsals)

with open("resultats.json", "r") as r:
    resultat=json.load(r)

st.write("resultats")
st.write(resultat)

st.title("gestió de controls")

llistacontrols=json.loads(open("controls.json", "r").read())

st.write("llistacontrols")
st.write(llistacontrols)

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


st.write(llistacontrols)


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

resultats=pd.DataFrame(index=dorsals.values(), columns=llistacontrols)



st.write("resultats")
st.write(resultats)


import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="TCO Terminaltrekkers", layout="centered")

st.title("TCO Vergelijking: Elektrisch vs. Diesel - Terminaltrekker")

st.markdown("Vergelijk de Total Cost of Ownership (TCO) van een elektrische terminaltrekker met een dieselvariant.")

st.header("Invoer")

# Voertuigprijzen
st.subheader("Voertuigprijzen")
elek_voertuig = st.number_input("Aanschafprijs elektrische truck (€)", value=255681)
diesel_voertuig = st.number_input("Aanschafprijs diesel truck (€)", value=131323)

# Gebruiksduur
st.subheader("Gebruik")
levensduur = st.slider("Gebruiksduur (jaren)", 1, 15, 7)
gebruik_per_jaar = st.number_input("Gebruik per jaar (in km of uren)", value=50000)

# Energieprijzen en verbruik
st.subheader("Energie & verbruik")
diesel_prijs = st.number_input("Dieselprijs (€/liter)", value=1.30)
verbruik_diesel = st.number_input("Dieselverbruik (l/km of l/u)", value=0.3)

stroomprijs_depot = st.number_input("Stroomprijs depot (€/kWh)", value=0.25)
stroomprijs_snellader = st.number_input("Stroomprijs snellader (€/kWh)", value=0.65)
verbruik_elektrisch = st.number_input("Elektrisch verbruik (kWh/km of kWh/u)", value=1.5)

# Subsidies
st.subheader("Subsidies")
aanzet_subsidie = st.number_input("AanZET subsidie (€)", value=30000)
mia_percentage = st.number_input("MIA (% van aanschafprijs)", value=36.0)

# Restwaarde
st.subheader("Restwaarde")
rest_diesel = st.number_input("Restwaarde diesel (%)", value=15.0)
rest_elektrisch = st.number_input("Restwaarde elektrisch (%)", value=15.0)

# Berekening
st.header("Resultaten")

# Netto aanschaf na subsidie
mia_subsidie = elek_voertuig * (mia_percentage / 100)
netto_elek_voertuig = elek_voertuig - aanzet_subsidie - mia_subsidie

# Restwaarde in €
rest_diesel_eur = diesel_voertuig * (rest_diesel / 100)
rest_elek_eur = elek_voertuig * (rest_elektrisch / 100)

# Totale kosten
tco_diesel = diesel_voertuig - rest_diesel_eur + gebruik_per_jaar * levensduur * (verbruik_diesel * diesel_prijs)
tco_elek = netto_elek_voertuig - rest_elek_eur + gebruik_per_jaar * levensduur * (verbruik_elektrisch * stroomprijs_depot)

col1, col2 = st.columns(2)
col1.metric("TCO Diesel", f"€ {tco_diesel:,.0f}")
col2.metric("TCO Elektrisch", f"€ {tco_elek:,.0f}")

# Visualisatie
st.subheader("Vergelijking")

fig, ax = plt.subplots()
labels = ['Diesel', 'Elektrisch']
values = [tco_diesel, tco_elek]
ax.bar(labels, values, color=['grey', 'green'])
ax.set_ylabel("Totale kosten (€)")
st.pyplot(fig)

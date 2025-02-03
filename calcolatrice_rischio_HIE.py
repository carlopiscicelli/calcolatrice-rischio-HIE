import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

# Modello di regressione logistica fittizio (per esempio)
# In un'app reale, qui caricheresti un modello pre-addestrato
log_reg = LogisticRegression()
log_reg.coef_ = np.array([[0.5, -0.3]])  # Coefficienti d'esempio
log_reg.intercept_ = np.array([-1])     # Intercetta d'esempio
log_reg.classes_ = np.array([0, 1])     # Classi binarie (0 = no HIE, 1 = HIE)

# Funzione per calcolare il rischio di HIE
def calcola_rischio(pH, BE, LATA):
    if LATA < 3:
        return 0, "Basso rischio"
    else:
        prob_rischio = log_reg.predict_proba([[pH, BE]])[:, 1][0]
        
        if prob_rischio < 0.10:
            categoria = "Basso rischio"
        elif prob_rischio < 0.50:
            categoria = "Rischio moderato"
        else:
            categoria = "Alto rischio"

        return round(prob_rischio * 100, 2), categoria

# Interfaccia Streamlit
st.title("Calcolatrice del Rischio di HIE")

pH = st.number_input("Inserisci il valore di pH arterioso (PHA):", min_value=6.5, max_value=7.5, step=0.01)
BE = st.number_input("Inserisci il valore di Base Excess arterioso (BEA):", min_value=-30.0, max_value=10.0, step=0.1)
LATA = st.number_input("Inserisci la concentrazione di lattati (LATA):", min_value=0.0, max_value=30.0, step=0.1)

if st.button("Calcola Rischio"):
    rischio, categoria = calcola_rischio(pH, BE, LATA)
    st.write(f"**Rischio Predetto di HIE:** {rischio}%")
    st.write(f"**Categoria di Rischio:** {categoria}")

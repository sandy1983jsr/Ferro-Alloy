import streamlit as st
import numpy as np

def show_electrode_optimizer(df):
    st.subheader("Electrode Paste Optimizer")
    st.write("Uses rheology and thermal resistance for paste quality optimization.")

    # Paste resistivity (Ohm's Law): R = ρ * L / A
    # Assume L=10cm, A=2cm^2, ρ (resistivity) estimated from wear and loss
    L = 0.1  # m
    A = 0.0002  # m^2
    resistance = np.mean(df['Resistance_Loss_kWh']) * 3600 / (L / A)  # Simplified for illustration

    st.metric("Estimated Paste Resistance (Ohms)", f"{resistance:.3f}")

    st.line_chart(df.set_index('Date')[['Electrode_Wear_mm']])
    st.bar_chart(df.groupby(df['Date'].dt.month)['Electrode_Wear_mm'].mean())
    st.write("Recommended maintenance window (days):", int(df['Electrode_Wear_mm'].mean() // 0.25))

import streamlit as st
import plotly.express as px
import numpy as np

def show_furnace_analytics(df):
    st.subheader("Furnace Analytics and Optimization")
    st.write("Includes heat transfer and reaction kinetics modeling for optimal operation.")

    # Arrhenius Equation for Reaction Rate (simplified)
    # k = A * exp(-Ea/(R*T))
    R = 8.314  # J/mol-K
    A = 1e7  # pre-exponential factor, 1/s (example)
    Ea = 120000  # Activation energy J/mol (example)
    T = df['Furnace_Temperature_C'].mean() + 273.15
    k = A * np.exp(-Ea / (R * T))

    st.metric("Calc. Reaction Rate k (1/s)", f"{k:.2e}")

    # Cycle time estimate (inverse proportional to rate)
    cycle_time = 1 / k if k != 0 else np.nan
    st.metric("Est. Cycle Time (s)", f"{cycle_time:.1f}")

    st.line_chart(df.set_index('Date')[['Furnace_Temperature_C', 'Furnace_Efficiency_%']])
    st.markdown("##### Furnace Efficiency Distribution")
    st.plotly_chart(px.histogram(df, x='Furnace_Efficiency_%', nbins=20, color_discrete_sequence=['#f95d1d']))

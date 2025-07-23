import streamlit as st
import plotly.express as px

def show_cost_ghg_dashboard(df):
    st.subheader("Cost and GHG Dashboard")
    st.write("Cost and emissions attributed by scientific loss root causes.")

    # Root cause attribution (example: 70% energy, 20% material, 10% reprocessing)
    total_cost = df['Cost_USD'].mean()
    energy_cost = 0.7 * total_cost
    material_cost = 0.2 * total_cost
    reprocessing_cost = 0.1 * total_cost

    st.metric("Avg. Cost (USD)", f"{int(total_cost):,}")
    st.metric("Energy Cost (USD)", f"{int(energy_cost):,}")
    st.metric("Material Cost (USD)", f"{int(material_cost):,}")
    st.metric("Reprocessing Cost (USD)", f"{int(reprocessing_cost):,}")
    st.metric("Avg. GHG Emissions (tCO2e)", f"{round(df['GHG_Emissions_tCO2e'].mean(), 2)}")
    st.plotly_chart(px.line(df, x='Date', y=['Cost_USD', 'GHG_Emissions_tCO2e'], color_discrete_sequence=['#f95d1d', '#cccccc']))

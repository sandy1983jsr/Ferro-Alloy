import streamlit as st
import plotly.express as px
import numpy as np

def show_cost_ghg_dashboard(df):
    st.subheader("Resource Utilization Dashboard")
    st.write("Electricity and feed utilization per product (sample MVP view).")

    prod_cols = [
        'HC_Low_Boron_kg', 'SiMn_HC_kg', 'SiMn_MC_kg', 'SiMn_LC_kg', 'SiMn_ELC_kg'
    ]
    # Electricity per ton product
    st.markdown("**Electricity Consumption per Ton Product**")
    for prod in prod_cols:
        if prod in df.columns and 'Electricity_Consumed_kWh' in df.columns:
            # Convert to numeric to avoid type errors
            df['Electricity_Consumed_kWh'] = pd.to_numeric(df['Electricity_Consumed_kWh'], errors='coerce')
            df[prod] = pd.to_numeric(df[prod], errors='coerce')
            tons = df[prod] / 1000
            # Avoid division by zero
            tons = tons.replace(0, np.nan)
            kwh_per_ton = df['Electricity_Consumed_kWh'] / tons
            st.line_chart(kwh_per_ton, use_container_width=True)
            st.write(f"Avg Electricity per ton for {prod}: {kwh_per_ton.mean():.2f} kWh/t")

    # Pie chart of feed mix
    st.markdown("**Average Feed Mix Composition**")
    feed_cols = [
        'Manganese_Ore_kg', 'Slag_Ferro_Manganese_kg', 'Remelts_kg', 
        'Coal_kg', 'Coke_kg', 'Dolomite_kg', 'Quartz_kg', 'Quartzite_kg'
    ]
    feed_cols_present = [c for c in feed_cols if c in df.columns]
    if feed_cols_present:
        feed_means = df[feed_cols_present].mean()
        st.plotly_chart(px.pie(
            values=feed_means.values, names=feed_means.index,
            title="Average Daily Feed Mix", color_discrete_sequence=px.colors.sequential.Oranges
        ))

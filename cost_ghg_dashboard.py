import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def clean_numeric(series):
    # Remove commas and convert to float
    return pd.to_numeric(series.astype(str).str.replace(",", ""), errors='coerce')

def show_cost_ghg_dashboard(df):
    st.subheader("Resource Utilization Dashboard")
    st.write("Electricity and feed utilization per product (sample MVP view).")

    # Clean numeric columns
    df['Electricity_Consumed_kWh'] = clean_numeric(df['Electricity_Consumed_kWh'])

    prod_cols = [
        'HC_Low_Boron_kg', 'SiMn_HC_kg', 'SiMn_MC_kg', 'SiMn_LC_kg', 'SiMn_ELC_kg'
    ]
    st.markdown("**Electricity Consumption per Ton Product**")
    any_graph = False
    for prod in prod_cols:
        if prod in df.columns:
            df[prod] = clean_numeric(df[prod])
            tons = df[prod] / 1000
            # Only plot if there is some valid production
            if tons.notnull().sum() > 0 and (tons > 0).sum() > 0:
                kwh_per_ton = df['Electricity_Consumed_kWh'] / tons
                kwh_per_ton = kwh_per_ton.replace([np.inf, -np.inf], np.nan)
                if kwh_per_ton.notnull().sum() > 0:
                    st.line_chart(kwh_per_ton, use_container_width=True)
                    st.write(f"Avg Electricity per ton for {prod}: {kwh_per_ton.mean():.2f} kWh/t")
                    any_graph = True
    if not any_graph:
        st.warning("No valid product data found to plot electricity consumption per ton.")

    st.markdown("**Average Feed Mix Composition**")
    feed_cols = [
        'Manganese_Ore_kg', 'Slag_Ferro_Manganese_kg', 'Remelts_kg', 
        'Coal_kg', 'Coke_kg', 'Dolomite_kg', 'Quartz_kg', 'Quartzite_kg'
    ]
    feed_cols_present = [c for c in feed_cols if c in df.columns]
    if feed_cols_present:
        for col in feed_cols_present:
            df[col] = clean_numeric(df[col])
        feed_means = df[feed_cols_present].mean()
        if feed_means.sum() > 0:
            st.plotly_chart(px.pie(
                values=feed_means.values, names=feed_means.index,
                title="Average Daily Feed Mix", color_discrete_sequence=px.colors.sequential.Oranges
            ))
        else:
            st.warning("No valid feed mix data found to plot pie chart.")
    else:
        st.warning("No feed mix columns found in uploaded data.")

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
            valid_mask = tons.notnull() & (tons > 0)
            if valid_mask.sum() > 0:
                kwh_per_ton = df['Electricity_Consumed_kWh'] / tons
                kwh_per_ton = kwh_per_ton.replace([np.inf, -np.inf], np.nan)
                # Prepare a cleaned DataFrame for plotting
                plot_df = pd.DataFrame({
                    'Date': df['Date'],
                    'Electricity_per_Ton': kwh_per_ton
                }).dropna()
                if not plot_df.empty:
                    fig = px.line(
                        plot_df,
                        x='Date',
                        y='Electricity_per_Ton',
                        title=f'Electricity Consumption per Ton for {prod}',
                        labels={
                            'Date': 'Production Date',
                            'Electricity_per_Ton': 'Electricity Consumed (kWh/ton)'
                        }
                    )
                    fig.update_layout(xaxis_title='Production Date', yaxis_title='Electricity Consumed (kWh/ton)')
                    st.plotly_chart(fig, use_container_width=True)
                    st.write(f"Avg Electricity per ton for {prod}: {plot_df['Electricity_per_Ton'].mean():.2f} kWh/t")
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
            fig_pie = px.pie(
                names=feed_means.index,
                values=feed_means.values,
                title="Average Daily Feed Mix",
                color_discrete_sequence=px.colors.sequential.Oranges
            )
            fig_pie.update_traces(textinfo='percent+label')
            fig_pie.update_layout(
                legend_title_text='Feed Material',
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.warning("No valid feed mix data found to plot pie chart.")
    else:
        st.warning("No feed mix columns found in uploaded data.")

import streamlit as st
import plotly.graph_objects as go

def show_materials_energy_balance(df):
    st.subheader("Materials and Energy Balance Engine")
    st.write("Overview of all feed materials and product outputs.")

    # Material inputs and outputs
    input_cols = [
        'Manganese_Ore_kg', 'Slag_Ferro_Manganese_kg', 'Remelts_kg', 
        'Coal_kg', 'Coke_kg', 'Dolomite_kg', 'Quartz_kg', 'Quartzite_kg'
    ]
    prod_cols = [
        'HC_Low_Boron_kg', 'SiMn_HC_kg', 'SiMn_MC_kg', 'SiMn_LC_kg', 'SiMn_ELC_kg'
    ]
    # Show summary statistics
    st.markdown("**Inputs (mean daily):**")
    st.dataframe(df[input_cols].mean().to_frame("Mean (kg)"))

    st.markdown("**Production Outputs (mean daily):**")
    st.dataframe(df[prod_cols].mean().to_frame("Mean (kg)"))

    # Sankey Diagram
    label = input_cols + prod_cols
    source = list(range(len(input_cols))) * len(prod_cols)
    target = [len(input_cols) + i for i in range(len(prod_cols)) for _ in input_cols]
    value = [df[col].mean() for col in input_cols for _ in prod_cols]

    # For illustration, connect each input to all outputs equally (customize as needed)
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15, thickness=20,
            label=label,
            color=["#f95d1d"] * len(input_cols) + ["#cccccc"] * len(prod_cols)
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=["#f95d1d"] * len(source)
        )
    )])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Electricity Consumption (kWh)")
    st.line_chart(df.set_index('Date')['Electricity_Consumed_kWh'])

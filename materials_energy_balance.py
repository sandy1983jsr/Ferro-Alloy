import streamlit as st
import plotly.graph_objects as go

def show_materials_energy_balance(df):
    st.subheader("Materials and Energy Balance Engine")
    st.write("Detailed mass and energy balance, including heat transfer modes.")

    # Advanced energy loss calculation
    # Assume: Q_loss = Q_conduction + Q_convection + Q_radiation (simplified)
    Q_total = df['Electricity_Consumed_kWh'].mean() * 3600  # convert to kJ
    Q_conduction = 0.2 * Q_total  # Example: 20% conduction loss
    Q_convection = 0.15 * Q_total
    Q_radiation = 0.1 * Q_total
    Q_useful = Q_total - (Q_conduction + Q_convection + Q_radiation)

    st.metric("Avg. Useful Energy (kJ)", f"{int(Q_useful):,}")
    st.metric("Conduction Loss (kJ)", f"{int(Q_conduction):,}")
    st.metric("Convection Loss (kJ)", f"{int(Q_convection):,}")
    st.metric("Radiation Loss (kJ)", f"{int(Q_radiation):,}")

    # Sankey Diagram for Materials Flow
    label = ["Raw Material", "Batch Weight", "Metal", "Slag"]
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15, thickness = 20, line = dict(color = "black", width = 0.5),
            label = label, color = ["#f95d1d", "#cccccc", "#b0b0b0", "#e6e6e6"]),
        link = dict(
            source = [0, 1, 1], target = [1, 2, 3],
            value = [df['Raw_Material_Input_kg'].mean(), df['Metal_Produced_kg'].mean(), df['Slag_Produced_kg'].mean()],
            color = ["#f95d1d", "#b0b0b0", "#e6e6e6"]
        ))])
    st.plotly_chart(fig, use_container_width=True)

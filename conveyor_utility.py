import streamlit as st
import plotly.express as px

def show_conveyor_utility_efficiency(df):
    st.subheader("Conveyor and Utility Efficiency")
    st.write("Mechanical efficiency and friction loss analysis.")

    # Efficiency = Output work / Input energy
    # For demo: assume output work proportional to material moved, input is conveyor energy
    output_work = df['Batch_Weight_kg'].mean() * 9.81 * 10  # m*kg*gravity*height (simplified)
    input_energy = df['Conveyor_Energy_kWh'].mean() * 3600  # kWh to kJ
    efficiency = output_work / input_energy if input_energy else np.nan

    st.metric("Mechanical Efficiency", f"{efficiency:.3f}")
    st.line_chart(df.set_index('Date')[['Conveyor_Energy_kWh', 'Utility_Energy_kWh']])
    st.plotly_chart(px.box(df, y=['Conveyor_Energy_kWh', 'Utility_Energy_kWh'], color_discrete_sequence=['#cccccc', '#f95d1d']))

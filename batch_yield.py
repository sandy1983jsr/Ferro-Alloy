import streamlit as st
import numpy as np

def show_batch_mixing_yield(df):
    st.subheader("Batch Mixing and Yield Model")
    st.write("PID control simulation for batch ratio stabilization.")

    # Simulated PID control: adjust ratio to target (e.g. 0.97)
    target = 0.97
    error = df['Batch_Mix_Ratio'] - target
    Kp, Ki, Kd = 1, 0.1, 0.01
    integral = np.cumsum(error)
    derivative = np.diff(error, prepend=0)
    adjustment = Kp * error + Ki * integral + Kd * derivative

    st.line_chart(pd.DataFrame({
        'Batch Mix Error': error,
        'PID Adjustment': adjustment
    }, index=df['Date']))

    st.markdown("##### Correlation (Mix Ratio vs. Yield)")
    st.write("Correlation coefficient:", round(df['Batch_Mix_Ratio'].corr(df['Yield_%']), 3))

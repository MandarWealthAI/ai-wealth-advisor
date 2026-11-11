import streamlit as st

st.title("AI Wealth Advisor")

st.subheader("Your Personal Wealth Calculator")

investment = st.number_input(
    "Enter Investment Amount (₹)",
    min_value=0
)

st.write("Investment Amount:", investment)

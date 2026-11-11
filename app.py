import streamlit as st

st.title("AI Wealth Advisor")

st.subheader("Your Personal Wealth Calculator")

investment = st.number_input(
    "Enter Investment Amount (₹)",
    min_value=0
)

st.write("Investment Amount:", investment)
annual_return = st.number_input(
    "Expected Annual Return (%)",
    min_value=1.0,
    value=12.0
)

years = st.number_input(
    "Investment Period (Years)",
    min_value=1,
    value=10
)

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

monthly_rate = annual_return / 100 / 12
months = years * 12

future_value = investment * (1 + annual_return / 100) ** years

profit = future_value - investment

st.metric("Estimated Wealth", f"₹{future_value:,.0f}")
st.metric("Estimated Profit", f"₹{profit:,.0f}")

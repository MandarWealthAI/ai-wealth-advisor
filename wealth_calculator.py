
# AI Wealth Advisor
# My First Python Program

print("Welcome to AI Wealth Advisor")

investment = float(input("Enter your investment amount (₹): "))
rate = float(input("Enter expected annual return (%): "))
years = int(input("Enter investment period (years): "))

future_value = investment * (1 + rate / 100) ** years

print("Your Future Investment Value: ₹", round(future_value, 2))

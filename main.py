# Collecting Data
winrate = float(input("Winrate (over 100 without %): "))
minimum_odd = float(input("Minimum Odd? (e.g: 1.65): "))
daily_bets = float(input("Bets per day?: "))
amount_per_bet = float(input("Stake per bet? In % without writing %: "))
initial_balance = float(input("Initial balance?: "))

# Based on winrate we calculate won and lost bets
monthly_bets = daily_bets * 30.0
looserate = (100.0 - winrate) / 100
lost_bets = monthly_bets * looserate
won_bets = float(monthly_bets - lost_bets)

# Calculate what we loose
balance_minus_lost = initial_balance - amount_per_bet * lost_bets

# Fix Minimum Odd
real_odd = minimum_odd - 1.0

# Calculate final balance
finalbalance = round(balance_minus_lost + (won_bets * amount_per_bet * real_odd), 2)

# Enchant  
percentage_profit = round(finalbalance - initial_balance, 2)
daily_profit = round(percentage_profit / 30.0, 2)

# Print Data
print("\n\n")
print(f"Final Balance: {finalbalance}")
print(f"Profit (%): {percentage_profit}%")
print(f"Daily Profit (%): {daily_profit}%")

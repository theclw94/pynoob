fee_monthly = int(input("Gym monthly membership fee: "))
fee_once = int(input("Gym single entry fee: "))

# First, ask yourself, how often would you go to the gym. Second, how many days
# are there in a month? Third, How many days in a month will you go to the gym?
gym_enter_interval = int(input("Go to gym every x days, what is x?: "))
month_days = 30
gym_enter_freq = month_days / gym_enter_interval

print(" ")

# Determine how much you'll be paying in a month,
# and compare that to the monthly fee.
fee = gym_enter_freq * fee_once
if fee >= fee_monthly:
    print("It is recommended to take up the monthly membership.")
elif fee < fee_monthly:
    print("You're better off just paying per entry.")

print("Fee to pay per month: RM{:.2f}".format(fee))

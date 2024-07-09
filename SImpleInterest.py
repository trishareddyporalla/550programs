def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
interest = calculate_simple_interest(principal, rate, time)

# Print the result
print("Simple Interest:", interest)

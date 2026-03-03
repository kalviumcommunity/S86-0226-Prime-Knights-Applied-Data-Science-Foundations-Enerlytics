# 1️⃣ Function with parameters
def calculate_total_energy(units, rate_per_unit):
    total_cost = units * rate_per_unit
    return total_cost


# 2️⃣ Function returning a computed result
def calculate_average_energy(total_units, days):
    average = total_units / days
    return average


# 3️⃣ Using returned values

# Passing arguments into the function
total_bill = calculate_total_energy(250, 6)

print("Total Energy Bill:", total_bill)

# Using returned value in further computation
average_daily_usage = calculate_average_energy(250, 30)

print("Average Daily Usage:", average_daily_usage)

# Passing returned value into another function
estimated_cost = calculate_total_energy(average_daily_usage, 6)

print("Estimated Cost Based on Average Usage:", estimated_cost)
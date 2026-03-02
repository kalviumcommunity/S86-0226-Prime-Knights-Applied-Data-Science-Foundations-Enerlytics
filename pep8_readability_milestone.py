# ❌ Poor variable naming example (not recommended)
x = 250
y = 6
z = x * y
print(z)


# ✅ Improved readable version using PEP 8 conventions

# Number of energy units consumed in a month
monthly_energy_units = 250

# Cost per unit of electricity
cost_per_unit = 6

# Calculate total monthly energy cost
total_monthly_energy_cost = monthly_energy_units * cost_per_unit

print("Total Monthly Energy Cost:", total_monthly_energy_cost)


# ✅ Example of meaningful comments

def calculate_average_daily_usage(total_units_consumed, number_of_days):
    """
    Calculates the average daily energy usage.

    Parameters:
    total_units_consumed (int): Total units used in a given period
    number_of_days (int): Number of days in that period

    Returns:
    float: Average daily energy usage
    """

    # Dividing total units by number of days to get average usage
    average_daily_usage = total_units_consumed / number_of_days
    return average_daily_usage


average_usage = calculate_average_daily_usage(300, 30)

print("Average Daily Usage:", average_usage)
"""
Structured Python Program Example
Demonstrates clean organization, reuse, and readability.
"""


# =========================
# Configuration Section
# =========================

DEFAULT_RATE_PER_UNIT = 6


# =========================
# Helper Functions
# =========================

def calculate_total_cost(units_consumed, rate_per_unit):
    """Calculate total electricity cost."""
    return units_consumed * rate_per_unit


def calculate_average_daily_usage(total_units, number_of_days):
    """Calculate average daily energy usage."""
    return total_units / number_of_days


def display_energy_report(total_units, days, rate):
    """Generate and display a structured energy usage report."""

    total_cost = calculate_total_cost(total_units, rate)
    average_usage = calculate_average_daily_usage(total_units, days)

    print("===== Energy Usage Report =====")
    print(f"Total Units Consumed: {total_units}")
    print(f"Average Daily Usage: {average_usage}")
    print(f"Rate Per Unit: {rate}")
    print(f"Total Cost: {total_cost}")
    print("================================")


# =========================
# Main Execution Section
# =========================

def main():
    """Main execution function."""

    monthly_units = 300
    number_of_days = 30

    display_energy_report(
        total_units=monthly_units,
        days=number_of_days,
        rate=DEFAULT_RATE_PER_UNIT
    )


if __name__ == "__main__":
    main()
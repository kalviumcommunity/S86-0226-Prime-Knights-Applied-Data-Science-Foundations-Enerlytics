print("=" * 70)
print("PYTHON FUNCTIONS: DEFINING AND CALLING FUNCTIONS")
print("=" * 70)
print()

# ============================================================================
# SECTION 1: DEFINING A FUNCTION
# ============================================================================
print("SECTION 1: DEFINING A FUNCTION")
print("-" * 70)
print("Functions are defined using the 'def' keyword")
print("They contain reusable blocks of code")
print()

# Example 1.1: Simple function with no parameters
print("1.1 Simple Function - No Parameters")
print("-" * 40)

def greet():
    """Display a greeting message"""
    print("Hello! Welcome to Python Functions!")

print("Function 'greet()' has been defined.")
print("Calling the function...")
greet()
print()

# Example 1.2: Function that performs a calculation
print("1.2 Function - Simple Calculation")
print("-" * 40)

def calculate_energy_cost():
    """Calculate energy cost for 100 kWh at $0.12 per kWh"""
    kwh = 100
    rate = 0.12
    cost = kwh * rate
    print(f"Energy cost for {kwh} kWh at ${rate}/kWh: ${cost:.2f}")

print("Function 'calculate_energy_cost()' defined.")
print("Calling the function...")
calculate_energy_cost()
print()

# Example 1.3: Function with a return value
print("1.3 Function - With Return Value")
print("-" * 40)

def get_average_consumption():
    """Calculate and return average energy consumption"""
    consumption = [120, 135, 98, 142, 115]
    average = sum(consumption) / len(consumption)
    return average

print("Function 'get_average_consumption()' defined.")
print("Calling the function and storing result...")
avg = get_average_consumption()
print(f"Average energy consumption: {avg:.2f} kWh")
print()

# ============================================================================
# SECTION 2: CALLING A FUNCTION
# ============================================================================
print("SECTION 2: CALLING A FUNCTION")
print("-" * 70)
print("Functions are executed by calling them with their name followed by ()")
print()

# Example 2.1: Multiple function calls
print("2.1 Multiple Function Calls")
print("-" * 40)

def display_separator():
    """Display a separator line"""
    print("*" * 50)

print("Calling 'display_separator()' three times:")
display_separator()
print("Energy Data Report")
display_separator()
print("Report Complete")
display_separator()
print()

# Example 2.2: Function calling another function
print("2.2 Function Calling Another Function")
print("-" * 40)

def format_message(message):
    """Format a message with decorative lines"""
    display_separator()
    print(f"  {message}")
    display_separator()

def show_report():
    """Display a formatted report"""
    format_message("Monthly Energy Report")

print("Calling 'show_report()' which internally calls 'format_message()':")
show_report()
print()

# Example 2.3: Understanding execution flow
print("2.3 Understanding Execution Flow")
print("-" * 40)

def step_one():
    """First step in process"""
    print("Step 1: Data collection started")

def step_two():
    """Second step in process"""
    print("Step 2: Data processing initiated")

def step_three():
    """Third step in process"""
    print("Step 3: Analysis complete")

def run_pipeline():
    """Execute the complete pipeline"""
    print("Starting data pipeline...")
    step_one()
    step_two()
    step_three()
    print("Pipeline execution complete!")

print("Calling 'run_pipeline()' - observe the execution order:")
run_pipeline()
print()

# ============================================================================
# SECTION 3: USING PARAMETERS AND ARGUMENTS
# ============================================================================
print("SECTION 3: USING PARAMETERS AND ARGUMENTS")
print("-" * 70)
print("Parameters allow functions to accept input values")
print("Arguments are the actual values passed when calling functions")
print()

# Example 3.1: Function with single parameter
print("3.1 Function with Single Parameter")
print("-" * 40)

def greet_customer(name):
    """Greet a customer by name"""
    print(f"Hello, {name}! Welcome to Enerlytics!")

print("Function 'greet_customer(name)' defined with one parameter.")
print("Calling with different arguments:")
greet_customer("Alice")
greet_customer("Bob")
greet_customer("Charlie")
print()

# Example 3.2: Function with multiple parameters
print("3.2 Function with Multiple Parameters")
print("-" * 40)

def calculate_cost(kwh, rate):
    """Calculate energy cost based on consumption and rate"""
    cost = kwh * rate
    print(f"Consumption: {kwh} kWh | Rate: ${rate}/kWh | Total: ${cost:.2f}")
    return cost

print("Function 'calculate_cost(kwh, rate)' defined with two parameters.")
print("Calling with different arguments:")
cost1 = calculate_cost(150, 0.12)
cost2 = calculate_cost(200, 0.15)
cost3 = calculate_cost(95, 0.10)
print()

# Example 3.3: Function with default parameter values
print("3.3 Function with Default Parameter Values")
print("-" * 40)

def analyze_consumption(kwh, threshold=100):
    """Analyze if consumption exceeds threshold"""
    if kwh > threshold:
        status = "HIGH"
    else:
        status = "NORMAL"
    print(f"Consumption: {kwh} kWh | Threshold: {threshold} kWh | Status: {status}")
    return status

print("Function 'analyze_consumption(kwh, threshold=100)' with default parameter.")
print("Calling with and without the optional parameter:")
analyze_consumption(120)  # Uses default threshold of 100
analyze_consumption(85)   # Uses default threshold of 100
analyze_consumption(150, 130)  # Uses custom threshold of 130
print()

# Example 3.4: Matching argument order
print("3.4 Matching Argument Order")
print("-" * 40)

def calculate_bill(customer_name, kwh, rate, tax_rate):
    """Calculate total bill including tax"""
    subtotal = kwh * rate
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"Customer: {customer_name}")
    print(f"  Consumption: {kwh} kWh × ${rate}/kWh = ${subtotal:.2f}")
    print(f"  Tax ({tax_rate*100}%): ${tax:.2f}")
    print(f"  Total: ${total:.2f}")
    return total

print("Function with 4 parameters - order matters!")
print("Calling with positional arguments:")
calculate_bill("Diana", 180, 0.12, 0.08)
print()

print("Calling with keyword arguments (order doesn't matter):")
calculate_bill(rate=0.15, kwh=210, tax_rate=0.10, customer_name="Eve")
print()

# Example 3.5: Meaningful parameter names
print("3.5 Using Meaningful Parameter Names")
print("-" * 40)

def compare_consumption(current_month, previous_month):
    """Compare current month consumption with previous month"""
    difference = current_month - previous_month
    if difference > 0:
        trend = "INCREASED"
        change = difference
    else:
        trend = "DECREASED"
        change = abs(difference)
    
    print(f"Previous: {previous_month} kWh | Current: {current_month} kWh")
    print(f"Trend: {trend} by {change:.2f} kWh")

print("Function with clear, meaningful parameter names.")
compare_consumption(150, 120)
compare_consumption(95, 140)
print()

# ============================================================================
# SECTION 4: UNDERSTANDING FUNCTION SCOPE (BASICS)
# ============================================================================
print("SECTION 4: UNDERSTANDING FUNCTION SCOPE (BASICS)")
print("-" * 70)
print("Variables inside functions have LOCAL scope")
print("Variables outside functions have GLOBAL scope")
print()

# Example 4.1: Local variables
print("4.1 Local Variables")
print("-" * 40)

def calculate_local():
    """Function with local variables"""
    local_kwh = 150  # This is a local variable
    local_rate = 0.12  # This is also local
    local_cost = local_kwh * local_rate
    print(f"Inside function - Cost: ${local_cost:.2f}")

print("Calling function with local variables:")
calculate_local()
print("Local variables exist only inside the function.")
print("Trying to access 'local_kwh' outside would cause an error.")
print()

# Example 4.2: Global variables
print("4.2 Global Variables")
print("-" * 40)

global_rate = 0.12  # This is a global variable
print(f"Global variable 'global_rate' = ${global_rate}/kWh")

def use_global():
    """Function that reads a global variable"""
    kwh = 200
    cost = kwh * global_rate  # Can read global variable
    print(f"Inside function - Using global rate: ${cost:.2f}")

print("Calling function that uses global variable:")
use_global()
print(f"Global variable still accessible: ${global_rate}/kWh")
print()

# Example 4.3: Local vs Global with same name
print("4.3 Local vs Global with Same Name")
print("-" * 40)

consumption = 100  # Global variable
print(f"Global 'consumption' = {consumption} kWh")

def process_data():
    """Function with local variable that shadows global"""
    consumption = 200  # Local variable (different from global)
    print(f"Inside function - Local 'consumption' = {consumption} kWh")

print("Calling function with local variable:")
process_data()
print(f"After function - Global 'consumption' still = {consumption} kWh")
print("The local variable did not change the global variable.")
print()

# Example 4.4: Avoiding side effects
print("4.4 Avoiding Unintended Side Effects")
print("-" * 40)

def calculate_clean(kwh, rate):
    """Clean function - uses only parameters, no globals"""
    cost = kwh * rate
    return cost

def calculate_with_globals():
    """Less clean - relies on global variables"""
    global global_kwh, global_rate_value
    return global_kwh * global_rate_value

print("Best practice: Keep function logic self-contained")
print("Use parameters instead of global variables when possible")

global_kwh = 150
global_rate_value = 0.12

result1 = calculate_clean(150, 0.12)
result2 = calculate_with_globals()

print(f"Clean function result: ${result1:.2f}")
print(f"Global-dependent function result: ${result2:.2f}")
print("Clean functions are easier to test, debug, and reuse!")
print()

# Example 4.5: Variable lifetime inside functions
print("4.5 Variable Lifetime Inside Functions")
print("-" * 40)

def demonstrate_lifetime():
    """Show that variables are created and destroyed"""
    temp_value = 999
    print(f"Inside function - temp_value = {temp_value}")
    print("temp_value will be destroyed when function ends")

print("Before calling function - temp_value doesn't exist yet")
demonstrate_lifetime()
print("After function ends - temp_value no longer exists")
print()

# ============================================================================
# PRACTICAL EXAMPLES: PUTTING IT ALL TOGETHER
# ============================================================================
print("SECTION 5: PRACTICAL EXAMPLES")
print("-" * 70)
print("Combining all concepts: definition, calling, parameters, and scope")
print()

# Example 5.1: Energy analysis system
print("5.1 Energy Analysis System")
print("-" * 40)

def validate_reading(reading):
    """Validate that a reading is positive"""
    if reading < 0:
        print(f"Error: Invalid reading {reading}")
        return False
    return True

def calculate_average(readings):
    """Calculate average from a list of readings"""
    valid_readings = []
    for reading in readings:
        if validate_reading(reading):
            valid_readings.append(reading)
    
    if valid_readings:
        avg = sum(valid_readings) / len(valid_readings)
        return avg
    return 0

def generate_report(readings, customer_name):
    """Generate a complete report"""
    print(f"\n--- Energy Report for {customer_name} ---")
    print(f"Number of readings: {len(readings)}")
    avg = calculate_average(readings)
    print(f"Average consumption: {avg:.2f} kWh")
    
    if avg > 120:
        print("Status: High consumption - consider energy saving tips")
    else:
        print("Status: Normal consumption")
    print("--- End of Report ---\n")

# Using the system
print("Running energy analysis system:")
monthly_readings = [115, 123, 108, 135, 118]
generate_report(monthly_readings, "Green Energy Corp")
print()

# Example 5.2: Price calculator with multiple functions
print("5.2 Multi-Function Price Calculator")
print("-" * 40)

def get_base_cost(kwh, rate):
    """Calculate base cost"""
    return kwh * rate

def get_tax(base_cost, tax_rate):
    """Calculate tax on base cost"""
    return base_cost * tax_rate

def get_service_fee(kwh):
    """Calculate service fee based on consumption"""
    if kwh > 200:
        return 15.00
    elif kwh > 100:
        return 10.00
    else:
        return 5.00

def calculate_total_bill(kwh, rate, tax_rate):
    """Calculate complete bill with all charges"""
    base = get_base_cost(kwh, rate)
    tax = get_tax(base, tax_rate)
    service = get_service_fee(kwh)
    total = base + tax + service
    
    print(f"Consumption: {kwh} kWh")
    print(f"Base cost: ${base:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Service fee: ${service:.2f}")
    print(f"TOTAL: ${total:.2f}")
    return total

print("Calculating bill with multiple component functions:")
calculate_total_bill(180, 0.12, 0.08)
print()


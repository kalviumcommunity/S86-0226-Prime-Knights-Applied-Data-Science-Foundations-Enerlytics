"""
Understanding Python Data Types - Numeric and String Fundamentals
==================================================================
This script demonstrates core Python data types: integers, floats, and strings.
Understanding these types is essential for all data analysis work.

Purpose: Learn numeric and string data types through practical examples
Author: Prime Knights Team
Date: February 27, 2026
"""

print("=" * 70)
print("PYTHON DATA TYPES: NUMERIC AND STRING FUNDAMENTALS")
print("=" * 70)
print()

# ============================================================================
# SECTION 1: NUMERIC DATA TYPES - INTEGERS
# ============================================================================
print("SECTION 1: INTEGER DATA TYPE")
print("-" * 70)

# Integers are whole numbers (no decimal point)
age = 25
year = 2026
temperature = -5
count = 0

print("Examples of integers:")
print(f"  age = {age}")
print(f"  year = {year}")
print(f"  temperature = {temperature}")
print(f"  count = {count}")
print()

# Integer arithmetic operations
print("Integer arithmetic operations:")
a = 10
b = 3

print(f"  Addition: {a} + {b} = {a + b}")
print(f"  Subtraction: {a} - {b} = {a - b}")
print(f"  Multiplication: {a} * {b} = {a * b}")
print(f"  Division: {a} / {b} = {a / b}")  # Returns float!
print(f"  Integer Division: {a} // {b} = {a // b}")  # Whole number only
print(f"  Modulus (remainder): {a} % {b} = {a % b}")
print(f"  Exponentiation: {a} ** {b} = {a ** b}")
print()

# Important: Division always returns a float
result = 10 / 2
print(f"⚠️  Note: Even 10 / 2 = {result} (this is a float, not an integer)")
print()

# ============================================================================
# SECTION 2: NUMERIC DATA TYPES - FLOATING-POINT NUMBERS
# ============================================================================
print("SECTION 2: FLOATING-POINT (FLOAT) DATA TYPE")
print("-" * 70)

# Floats are numbers with decimal points
price = 19.99
temperature_celsius = 22.5
pi = 3.14159
measurement = 0.001

print("Examples of floats:")
print(f"  price = {price}")
print(f"  temperature_celsius = {temperature_celsius}")
print(f"  pi = {pi}")
print(f"  measurement = {measurement}")
print()

# Float arithmetic operations
print("Float arithmetic operations:")
x = 5.5
y = 2.0

print(f"  Addition: {x} + {y} = {x + y}")
print(f"  Subtraction: {x} - {y} = {x - y}")
print(f"  Multiplication: {x} * {y} = {x * y}")
print(f"  Division: {x} / {y} = {x / y}")
print()

# Mixing integers and floats
print("Mixing integers and floats:")
int_num = 10
float_num = 3.5
result = int_num + float_num
print(f"  Integer: {int_num}")
print(f"  Float: {float_num}")
print(f"  Result: {int_num} + {float_num} = {result} (becomes a float)")
print()

# ============================================================================
# SECTION 3: STRING DATA TYPE
# ============================================================================
print("SECTION 3: STRING DATA TYPE")
print("-" * 70)

# Strings are text data enclosed in quotes
customer_name = "Alice Johnson"
product_id = "PROD-12345"
message = 'Hello, World!'
empty_string = ""

print("Examples of strings:")
print(f'  customer_name = "{customer_name}"')
print(f'  product_id = "{product_id}"')
print(f'  message = \'{message}\'')
print(f'  empty_string = "{empty_string}"')
print()

# String operations
print("String operations:")

# Concatenation (joining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"  Concatenation: \"{first_name}\" + \" \" + \"{last_name}\" = \"{full_name}\"")

# Repetition
word = "Data"
repeated = word * 3
print(f"  Repetition: \"{word}\" * 3 = \"{repeated}\"")

# Length
text = "Python"
length = len(text)
print(f"  Length: len(\"{text}\") = {length}")

# Accessing characters (indexing starts at 0)
print(f"  First character: \"{text}\"[0] = \"{text[0]}\"")
print(f"  Last character: \"{text}\"[-1] = \"{text[-1]}\"")

# String slicing
print(f"  First 3 characters: \"{text}\"[0:3] = \"{text[0:3]}\"")
print()

# String methods
print("Common string methods:")
sample = "  Hello, Python!  "
print(f'  Original: "{sample}"')
print(f'  Upper case: "{sample.upper()}"')
print(f'  Lower case: "{sample.lower()}"')
print(f'  Stripped: "{sample.strip()}"')
print(f'  Replace: "{sample.replace("Python", "World")}"')
print()

# ============================================================================
# SECTION 4: TYPE INSPECTION
# ============================================================================
print("SECTION 4: INSPECTING DATA TYPES")
print("-" * 70)

# Using type() to check variable types
integer_var = 42
float_var = 3.14
string_var = "Hello"
division_result = 10 / 2

print("Checking types with type() function:")
print(f"  type(42) = {type(integer_var)}")
print(f"  type(3.14) = {type(float_var)}")
print(f"  type(\"Hello\") = {type(string_var)}")
print(f"  type(10 / 2) = {type(division_result)} ⚠️  (division always returns float)")
print()

# ============================================================================
# SECTION 5: MIXING TYPES - COMMON ERRORS
# ============================================================================
print("SECTION 5: MIXING NUMBERS AND STRINGS")
print("-" * 70)

# This section demonstrates type conversion and common errors
age_num = 25
age_str = "25"

print("Understanding type differences:")
print(f"  age_num = {age_num} (type: {type(age_num).__name__})")
print(f"  age_str = \"{age_str}\" (type: {type(age_str).__name__})")
print()

# Attempting to mix types
print("❌ COMMON ERROR: Mixing types incorrectly")
print("  Attempting: age_num + age_str")
try:
    result = age_num + age_str
    print(f"  Result: {result}")
except TypeError as e:
    print(f"  ERROR: {e}")
print()

# ============================================================================
# SECTION 6: TYPE CONVERSION
# ============================================================================
print("SECTION 6: TYPE CONVERSION (CASTING)")
print("-" * 70)

# Converting between types
print("Converting strings to numbers:")
num_string = "100"
num_integer = int(num_string)
num_float = float(num_string)
print(f'  Original: "{num_string}" (type: {type(num_string).__name__})')
print(f"  int(\"{num_string}\") = {num_integer} (type: {type(num_integer).__name__})")
print(f"  float(\"{num_string}\") = {num_float} (type: {type(num_float).__name__})")
print()

print("Converting numbers to strings:")
price_num = 29.99
price_str = str(price_num)
print(f"  Original: {price_num} (type: {type(price_num).__name__})")
print(f'  str({price_num}) = "{price_str}" (type: {type(price_str).__name__})')
print()

# ============================================================================
# SECTION 7: PRACTICAL EXAMPLE - SAFE MIXING
# ============================================================================
print("SECTION 7: MIXING TYPES SAFELY")
print("-" * 70)

# Correct way to mix numbers and strings
quantity = 5
item = "apples"
price_per_item = 1.50

# Method 1: Convert numbers to strings for concatenation
message1 = "I bought " + str(quantity) + " " + item + " for $" + str(price_per_item) + " each."
print(f"Method 1 (concatenation): {message1}")

# Method 2: Use f-strings (recommended)
message2 = f"I bought {quantity} {item} for ${price_per_item} each."
print(f"Method 2 (f-strings): {message2}")

# Method 3: Use format() method
message3 = "I bought {} {} for ${} each.".format(quantity, item, price_per_item)
print(f"Method 3 (format): {message3}")
print()

# Calculating total
total = quantity * price_per_item
print(f"Calculation: {quantity} items × ${price_per_item} = ${total}")
print(f"Result type: {type(total).__name__} (float)")
print()

# ============================================================================
# SECTION 8: DATA ANALYSIS EXAMPLE
# ============================================================================
print("SECTION 8: PRACTICAL DATA ANALYSIS SCENARIO")
print("-" * 70)

# Energy consumption data (simulating values from a dataset)
customer_id = "CUST001"
consumption_kwh = 150.5
cost_per_kwh = 0.12
days = 30

print("Energy consumption analysis:")
print(f"  Customer ID: {customer_id} (type: {type(customer_id).__name__})")
print(f"  Consumption: {consumption_kwh} kWh (type: {type(consumption_kwh).__name__})")
print(f"  Cost per kWh: ${cost_per_kwh} (type: {type(cost_per_kwh).__name__})")
print(f"  Days: {days} (type: {type(days).__name__})")
print()

# Calculations
total_cost = consumption_kwh * cost_per_kwh
daily_average = consumption_kwh / days

print("Calculated results:")
print(f"  Total cost: ${total_cost:.2f}")
print(f"  Daily average: {daily_average:.2f} kWh/day")
print()

# Creating a report (mixing types correctly)
report = f"""
Energy Usage Report
-------------------
Customer: {customer_id}
Period: {days} days
Total Consumption: {consumption_kwh} kWh
Average Daily Consumption: {daily_average:.2f} kWh
Cost per kWh: ${cost_per_kwh}
Total Cost: ${total_cost:.2f}
"""
print(report)

# ============================================================================
# SECTION 9: KEY TAKEAWAYS
# ============================================================================
print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print()
print("✅ INTEGER: Whole numbers without decimals (e.g., 5, -3, 0)")
print("✅ FLOAT: Numbers with decimals (e.g., 3.14, -0.5, 2.0)")
print("✅ STRING: Text enclosed in quotes (e.g., \"Hello\", 'Python')")
print()
print("⚠️  IMPORTANT RULES:")
print("   • Division (/) always returns a float, even for whole numbers")
print("   • Cannot directly add/subtract numbers and strings")
print("   • Use type() to check variable types")
print("   • Use int(), float(), str() to convert between types")
print("   • Use f-strings for mixing types in output")
print()
print("=" * 70)
print("DATA TYPES TUTORIAL COMPLETE!")
print("=" * 70)
print()

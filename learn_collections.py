"""
Understanding Python Collections - Lists, Tuples, and Dictionaries
===================================================================
This script demonstrates Python's core collection data structures.
Understanding these structures is essential for organizing and manipulating data.

Purpose: Learn lists, tuples, and dictionaries through practical examples
Author: Prime Knights Team
Date: February 27, 2026
"""

print("=" * 70)
print("PYTHON COLLECTIONS: LISTS, TUPLES, AND DICTIONARIES")
print("=" * 70)
print()

# ============================================================================
# SECTION 1: WORKING WITH LISTS
# ============================================================================
print("SECTION 1: WORKING WITH PYTHON LISTS")
print("-" * 70)
print("Lists are ORDERED and MUTABLE collections")
print()

# Creating lists
print("1.1 Creating Lists")
print("-" * 40)

# List with energy consumption values
energy_consumption = [120.5, 135.2, 98.7, 142.0, 115.3]
print(f"Energy consumption (kWh): {energy_consumption}")

# List with customer names
customers = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"Customer names: {customers}")

# List with mixed data types (though not always recommended)
mixed_data = [100, "Active", 45.5, True]
print(f"Mixed data: {mixed_data}")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")
print()

# Accessing list elements
print("1.2 Accessing List Elements")
print("-" * 40)

print(f"First customer: {customers[0]}")
print(f"Third customer: {customers[2]}")
print(f"Last customer: {customers[-1]}")
print(f"Second to last: {customers[-2]}")
print()

# List slicing
print("1.3 List Slicing")
print("-" * 40)

print(f"First three customers: {customers[0:3]}")
print(f"Last two customers: {customers[-2:]}")
print(f"All except first: {customers[1:]}")
print(f"All except last: {customers[:-1]}")
print()

# Modifying lists (Lists are MUTABLE)
print("1.4 Modifying List Elements")
print("-" * 40)

print(f"Original list: {customers}")
customers[1] = "Robert"
print(f"After changing index 1: {customers}")
print()

# Adding elements
print("1.5 Adding Elements to Lists")
print("-" * 40)

# Using append() - adds to the end
customers.append("Frank")
print(f"After append('Frank'): {customers}")

# Using insert() - adds at specific position
customers.insert(2, "Grace")
print(f"After insert(2, 'Grace'): {customers}")

# Using extend() - adds multiple items
customers.extend(["Henry", "Isabel"])
print(f"After extend(['Henry', 'Isabel']): {customers}")
print()

# Removing elements
print("1.6 Removing Elements from Lists")
print("-" * 40)

print(f"Current list: {customers}")

# Using remove() - removes specific value
customers.remove("Grace")
print(f"After remove('Grace'): {customers}")

# Using pop() - removes by index and returns value
removed = customers.pop(3)
print(f"After pop(3) - removed '{removed}': {customers}")

# Using pop() without index - removes last item
last_item = customers.pop()
print(f"After pop() - removed '{last_item}': {customers}")
print()

# List operations
print("1.7 List Operations")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Count of 3: {numbers.count(3)}")
print()

# Iterating over lists
print("1.8 Iterating Over Lists")
print("-" * 40)

daily_consumption = [125.5, 130.2, 118.7, 145.0, 122.3]
print("Daily energy consumption:")
for day, consumption in enumerate(daily_consumption, start=1):
    print(f"  Day {day}: {consumption} kWh")
print()

# List comprehension (bonus)
print("1.9 List Comprehension (Creating lists efficiently)")
print("-" * 40)

# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")
print()

# ============================================================================
# SECTION 2: WORKING WITH TUPLES
# ============================================================================
print("SECTION 2: WORKING WITH PYTHON TUPLES")
print("-" * 70)
print("Tuples are ORDERED and IMMUTABLE collections")
print()

# Creating tuples
print("2.1 Creating Tuples")
print("-" * 40)

# Tuple with coordinates
location = (40.7128, -74.0060)
print(f"Location (lat, lon): {location}")

# Tuple with customer data
customer_record = ("CUST001", "Alice Johnson", 35, "Premium")
print(f"Customer record: {customer_record}")

# Tuple with single element (note the comma!)
single_element = (42,)
print(f"Single element tuple: {single_element}")

# Tuple without parentheses (still valid)
rgb_color = 255, 128, 0
print(f"RGB color: {rgb_color}")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
print()

# Accessing tuple elements
print("2.2 Accessing Tuple Elements")
print("-" * 40)

print(f"Customer ID: {customer_record[0]}")
print(f"Customer name: {customer_record[1]}")
print(f"Customer age: {customer_record[2]}")
print(f"Last element: {customer_record[-1]}")
print()

# Tuple slicing
print("2.3 Tuple Slicing")
print("-" * 40)

data = (10, 20, 30, 40, 50, 60)
print(f"Full tuple: {data}")
print(f"First three: {data[0:3]}")
print(f"Last two: {data[-2:]}")
print()

# Immutability demonstration
print("2.4 Tuples are IMMUTABLE (Cannot be changed)")
print("-" * 40)

print(f"Original tuple: {location}")
print("Attempting to modify tuple...")

try:
    location[0] = 50.0  # This will raise an error
except TypeError as e:
    print(f"❌ ERROR: {e}")
    print("✅ This is expected! Tuples cannot be modified.")
print()

# Tuple operations
print("2.5 Tuple Operations")
print("-" * 40)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Concatenation: {tuple1 + tuple2}")
print(f"Repetition: {tuple1 * 3}")
print(f"Length: {len(tuple1)}")
print(f"Count of 2: {tuple1.count(2)}")
print(f"Index of 3: {tuple1.index(3)}")
print()

# Tuple unpacking
print("2.6 Tuple Unpacking")
print("-" * 40)

coordinates = (10.5, 20.3, 30.7)
x, y, z = coordinates
print(f"Original tuple: {coordinates}")
print(f"Unpacked values: x={x}, y={y}, z={z}")

# Swapping values using tuples
print("\nSwapping values:")
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")
print()

# When to use tuples
print("2.7 When to Use Tuples")
print("-" * 40)

# Fixed data that shouldn't change
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday")
print(f"Days of week: {DAYS_OF_WEEK}")

# Return multiple values from functions
def get_min_max_avg(numbers):
    """Returns min, max, and average as a tuple"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

values = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = get_min_max_avg(values)
print(f"\nFor values {values}:")
print(f"  Min: {min_val}, Max: {max_val}, Avg: {avg_val:.2f}")
print()

# ============================================================================
# SECTION 3: WORKING WITH DICTIONARIES
# ============================================================================
print("SECTION 3: WORKING WITH PYTHON DICTIONARIES")
print("-" * 70)
print("Dictionaries store data as KEY-VALUE PAIRS")
print()

# Creating dictionaries
print("3.1 Creating Dictionaries")
print("-" * 40)

# Customer information
customer = {
    "id": "CUST001",
    "name": "Alice Johnson",
    "age": 35,
    "membership": "Premium",
    "active": True
}
print("Customer dictionary:")
for key, value in customer.items():
    print(f"  {key}: {value}")
print()

# Energy consumption by month
monthly_consumption = {
    "January": 150.5,
    "February": 135.2,
    "March": 120.8,
    "April": 110.3
}
print(f"Monthly consumption: {monthly_consumption}")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print()

# Accessing dictionary values
print("3.2 Accessing Dictionary Values")
print("-" * 40)

print(f"Customer name: {customer['name']}")
print(f"Customer age: {customer['age']}")
print(f"Customer membership: {customer['membership']}")
print()

# Safe access using get()
print("3.3 Safe Access Using get()")
print("-" * 40)

print(f"Customer email (using get): {customer.get('email', 'Not provided')}")
print(f"Customer name (using get): {customer.get('name')}")
print()

# Attempting unsafe access
print("Attempting to access non-existent key:")
try:
    print(customer['email'])
except KeyError as e:
    print(f"❌ ERROR: Key {e} not found")
    print("✅ Use .get() method for safe access!")
print()

# Modifying dictionaries
print("3.4 Modifying Dictionary Values")
print("-" * 40)

print(f"Before: {customer}")
customer['age'] = 36
print(f"After updating age: {customer}")
print()

# Adding new key-value pairs
print("3.5 Adding New Key-Value Pairs")
print("-" * 40)

customer['email'] = "alice.johnson@example.com"
customer['phone'] = "+1-555-0123"
print("After adding email and phone:")
for key, value in customer.items():
    print(f"  {key}: {value}")
print()

# Removing key-value pairs
print("3.6 Removing Key-Value Pairs")
print("-" * 40)

print(f"Before removal: {list(customer.keys())}")
removed_value = customer.pop('phone')
print(f"After pop('phone') - removed: {removed_value}")
print(f"Current keys: {list(customer.keys())}")

# Using del
del customer['age']
print(f"After del customer['age']: {list(customer.keys())}")
print()

# Dictionary methods
print("3.7 Dictionary Methods")
print("-" * 40)

energy_data = {
    "solar": 45.5,
    "wind": 30.2,
    "hydro": 15.8,
    "coal": 8.5
}

print(f"Full dictionary: {energy_data}")
print(f"Keys: {list(energy_data.keys())}")
print(f"Values: {list(energy_data.values())}")
print(f"Items: {list(energy_data.items())}")
print(f"Length: {len(energy_data)}")
print(f"'solar' in dictionary: {'solar' in energy_data}")
print(f"'nuclear' in dictionary: {'nuclear' in energy_data}")
print()

# Iterating over dictionaries
print("3.8 Iterating Over Dictionaries")
print("-" * 40)

print("Energy generation by source:")
for source, amount in energy_data.items():
    print(f"  {source.capitalize()}: {amount} MW")
print()

print("Keys only:")
for source in energy_data.keys():
    print(f"  {source}")
print()

print("Values only:")
for amount in energy_data.values():
    print(f"  {amount} MW")
print()

# Nested dictionaries
print("3.9 Nested Dictionaries")
print("-" * 40)

customers_db = {
    "CUST001": {
        "name": "Alice Johnson",
        "consumption": 150.5,
        "tier": "Premium"
    },
    "CUST002": {
        "name": "Bob Smith",
        "consumption": 120.3,
        "tier": "Standard"
    },
    "CUST003": {
        "name": "Charlie Brown",
        "consumption": 180.7,
        "tier": "Premium"
    }
}

print("Customer database:")
for cust_id, details in customers_db.items():
    print(f"\n{cust_id}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
print()

# Accessing nested values
print(f"Customer CUST002's name: {customers_db['CUST002']['name']}")
print(f"Customer CUST003's consumption: {customers_db['CUST003']['consumption']} kWh")
print()

# ============================================================================
# SECTION 4: CHOOSING THE RIGHT DATA STRUCTURE
# ============================================================================
print("SECTION 4: CHOOSING THE RIGHT DATA STRUCTURE")
print("-" * 70)
print()

print("4.1 When to Use LISTS")
print("-" * 40)
print("✅ Ordered collection of items")
print("✅ Need to modify, add, or remove elements")
print("✅ Elements accessed by numerical index")
print("✅ Duplicate values are allowed")
print("\nExamples:")
print("  • Daily temperature readings: [22.5, 23.1, 21.8, 24.0]")
print("  • Customer orders in sequence")
print("  • Task queue that needs processing")
print()

print("4.2 When to Use TUPLES")
print("-" * 40)
print("✅ Ordered collection that should NOT change")
print("✅ Protect data from accidental modification")
print("✅ Use as dictionary keys (lists can't be keys)")
print("✅ Return multiple values from functions")
print("\nExamples:")
print("  • Geographic coordinates: (40.7128, -74.0060)")
print("  • RGB color values: (255, 128, 0)")
print("  • Database record: ('CUST001', 'Alice', 35)")
print("  • Configuration settings")
print()

print("4.3 When to Use DICTIONARIES")
print("-" * 40)
print("✅ Key-value relationships")
print("✅ Need to look up values by meaningful keys")
print("✅ Model real-world entities with attributes")
print("✅ Fast lookups by key")
print("\nExamples:")
print("  • Customer info: {'name': 'Alice', 'age': 35}")
print("  • Configuration settings by name")
print("  • Counting occurrences: {'apple': 5, 'banana': 3}")
print("  • API responses with named fields")
print()

print("4.4 Comparison Summary")
print("-" * 40)

comparison = """
╔══════════════╦═══════════╦═══════════╦═════════════╗
║   Feature    ║   List    ║   Tuple   ║ Dictionary  ║
╠══════════════╬═══════════╬═══════════╬═════════════╣
║   Ordered    ║    Yes    ║    Yes    ║  No (3.7+)  ║
║   Mutable    ║    Yes    ║    No     ║     Yes     ║
║   Indexed    ║  0,1,2... ║  0,1,2... ║  Key-based  ║
║  Duplicates  ║  Allowed  ║  Allowed  ║ Keys unique ║
║    Syntax    ║    []     ║    ()     ║     {}      ║
╚══════════════╩═══════════╩═══════════╩═════════════╝
"""
print(comparison)
print()

# ============================================================================
# SECTION 5: PRACTICAL ENERGY ANALYTICS EXAMPLE
# ============================================================================
print("SECTION 5: PRACTICAL EXAMPLE - ENERGY ANALYTICS")
print("-" * 70)
print()

# Combining all three data structures
print("5.1 Combined Usage Example")
print("-" * 40)

# List of daily consumption values
daily_readings = [125.5, 130.2, 118.7, 145.0, 122.3, 135.8, 128.9]

# Tuple for fixed metadata
meter_info = ("METER-001", "Industrial", "Building A")

# Dictionary for customer details
customer_profile = {
    "id": "CUST001",
    "name": "TechCorp Industries",
    "meter_id": meter_info[0],
    "meter_type": meter_info[1],
    "location": meter_info[2],
    "daily_readings": daily_readings
}

print("Customer Profile:")
print(f"  Customer: {customer_profile['name']} ({customer_profile['id']})")
print(f"  Meter: {customer_profile['meter_id']}")
print(f"  Type: {customer_profile['meter_type']}")
print(f"  Location: {customer_profile['location']}")
print()

print("Weekly Analysis:")
readings = customer_profile['daily_readings']
total = sum(readings)
average = total / len(readings)
peak = max(readings)
lowest = min(readings)

print(f"  Total consumption: {total:.2f} kWh")
print(f"  Average daily: {average:.2f} kWh")
print(f"  Peak usage: {peak:.2f} kWh")
print(f"  Lowest usage: {lowest:.2f} kWh")
print()

print("Daily breakdown:")
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
for day, reading in zip(days, readings):
    status = "🔴 High" if reading > average else "🟢 Normal"
    print(f"  {day}: {reading:>6.2f} kWh {status}")
print()

# ============================================================================
# SECTION 6: KEY TAKEAWAYS
# ============================================================================
print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print()

print("📋 LISTS [...]")
print("   • Ordered, mutable collections")
print("   • Use when data needs to change")
print("   • Access by index: my_list[0]")
print("   • Methods: append(), remove(), pop(), insert()")
print()

print("📌 TUPLES (...)")
print("   • Ordered, immutable collections")
print("   • Use when data should NOT change")
print("   • Access by index: my_tuple[0]")
print("   • Good for fixed records and coordinates")
print()

print("🔑 DICTIONARIES {...}")
print("   • Key-value pairs")
print("   • Use for labeled/named data")
print("   • Access by key: my_dict['key']")
print("   • Methods: get(), keys(), values(), items()")
print()

print("⚡ BEST PRACTICES:")
print("   • Choose the structure that matches your needs")
print("   • Use tuples for data that shouldn't change")
print("   • Use dictionaries for named attributes")
print("   • Use lists for sequences that grow/shrink")
print("   • Use .get() for safe dictionary access")
print()

print("=" * 70)
print("COLLECTIONS TUTORIAL COMPLETE!")
print("=" * 70)
print()

print("✅ Next Steps:")
print("   1. Run this script to see all examples")
print("   2. Modify examples to test your understanding")
print("   3. Create your own collections for your use case")
print("   4. Record a 2-minute video demonstrating:")
print("      • List operations and modification")
print("      • Tuple immutability behavior")
print("      • Dictionary key-value access")
print("      • Explanation of when to use each")
print()

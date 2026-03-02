"""
Learn Loops - Using for and while Loops for Iterative Data Processing

This module demonstrates:
1. Using for loops for iteration
2. Using while loops for condition-based repetition
3. Controlling loop flow with break and continue
4. Avoiding infinite loops

Author: Prime Knights Team
Date: March 2, 2026
"""


def section_separator(title):
    """Print a section separator for better readability"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


# ==============================================================================
# SECTION 1: USING FOR LOOPS FOR ITERATION
# ==============================================================================

def demonstrate_for_loops():
    """
    Learn how for loops work.
    - Iterate over a range of numbers
    - Iterate over a list or collection
    - Observe loop execution order
    - Use loop variables meaningfully
    """
    section_separator("SECTION 1: Using for Loops for Iteration")
    
    # Example 1.1: Iterating over a range of numbers
    print("Example 1.1: Iterating over a range (0 to 4)")
    for i in range(5):
        print(f"  Iteration {i}: Current number is {i}")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 1.2: Iterating over a range with start and end
    print("Example 1.2: Iterating over a range (1 to 10)")
    for num in range(1, 11):
        print(f"  Number: {num}", end="  ")
        if num % 5 == 0:
            print()  # New line every 5 numbers
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 1.3: Iterating over a list of energy sources
    print("Example 1.3: Iterating over a list of energy sources")
    energy_sources = ["Solar", "Wind", "Hydro", "Nuclear", "Geothermal"]
    
    for source in energy_sources:
        print(f"  Energy source: {source}")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 1.4: Using enumerate to get both index and value
    print("Example 1.4: Using enumerate for index and value")
    energy_consumption = [120, 145, 98, 167, 134]  # kWh values
    
    for index, consumption in enumerate(energy_consumption):
        print(f"  Day {index + 1}: {consumption} kWh consumed")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 1.5: Iterating with a step value
    print("Example 1.5: Iterating with a step value (every 2nd number)")
    for i in range(0, 20, 2):
        print(f"  Even number: {i}", end="  ")
    print("\n")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 1.6: Processing data with for loop
    print("Example 1.6: Processing temperature data")
    temperatures = [22.5, 24.0, 19.8, 23.2, 25.1]
    total_temp = 0
    
    for temp in temperatures:
        total_temp += temp
        print(f"  Current temperature: {temp}°C, Running total: {total_temp}°C")
    
    average_temp = total_temp / len(temperatures)
    print(f"\n  Average temperature: {average_temp:.2f}°C")


# ==============================================================================
# SECTION 2: USING WHILE LOOPS FOR CONDITION-BASED REPETITION
# ==============================================================================

def demonstrate_while_loops():
    """
    Learn how while loops work.
    - Write a condition-controlled loop
    - Update loop variables correctly
    - Stop loops intentionally
    - Understand when while is appropriate
    """
    section_separator("SECTION 2: Using while Loops for Condition-Based Repetition")
    
    # Example 2.1: Basic while loop with counter
    print("Example 2.1: Basic while loop - counting from 0 to 4")
    counter = 0
    while counter < 5:
        print(f"  Counter value: {counter}")
        counter += 1  # Important: update the loop variable
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 2.2: While loop for accumulation
    print("Example 2.2: Accumulating energy consumption until threshold")
    daily_consumption = [25, 30, 28, 35, 40, 45, 50]
    total_consumption = 0
    day = 0
    threshold = 150  # kWh
    
    while total_consumption < threshold and day < len(daily_consumption):
        total_consumption += daily_consumption[day]
        day += 1
        print(f"  Day {day}: Total consumption = {total_consumption} kWh")
    
    print(f"\n  Reached threshold on day {day} with {total_consumption} kWh")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 2.3: While loop for user validation simulation
    print("Example 2.3: Input validation (simulated)")
    attempts = 0
    max_attempts = 3
    valid_input = False
    
    # Simulating inputs
    simulated_inputs = [15, -5, 25]  # negative value should be rejected
    
    while attempts < max_attempts and not valid_input:
        value = simulated_inputs[attempts]
        print(f"  Attempt {attempts + 1}: Received value = {value}")
        
        if value >= 0:
            print(f"  ✓ Valid input accepted: {value}")
            valid_input = True
        else:
            print(f"  ✗ Invalid input (negative value)")
            attempts += 1
    
    if not valid_input:
        print(f"\n  Maximum attempts reached. Using default value.")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 2.4: Countdown loop
    print("Example 2.4: Countdown from 10")
    countdown = 10
    while countdown > 0:
        print(f"  {countdown}...", end=" ")
        countdown -= 1
    print("Liftoff! 🚀\n")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 2.5: While loop for finding a condition
    print("Example 2.5: Finding first occurrence above threshold")
    sensor_readings = [12, 15, 18, 22, 28, 35, 40]
    threshold = 30
    index = 0
    
    while index < len(sensor_readings) and sensor_readings[index] <= threshold:
        print(f"  Reading {index + 1}: {sensor_readings[index]} (below threshold)")
        index += 1
    
    if index < len(sensor_readings):
        print(f"\n  Found: Reading {index + 1} = {sensor_readings[index]} (above {threshold})")
    else:
        print(f"\n  No readings above {threshold} found")


# ==============================================================================
# SECTION 3: CONTROLLING LOOP FLOW
# ==============================================================================

def demonstrate_loop_control():
    """
    Manage loop execution safely.
    - Use break to exit loops early
    - Use continue to skip iterations
    - Avoid unnecessary or confusing logic
    - Keep loop flow readable
    """
    section_separator("SECTION 3: Controlling Loop Flow")
    
    # Example 3.1: Using break to exit early
    print("Example 3.1: Using break - Stop when error detected")
    sensor_data = [45, 52, 48, -999, 51, 47]  # -999 indicates sensor error
    
    print("Processing sensor data...")
    for index, reading in enumerate(sensor_data):
        if reading == -999:
            print(f"  ✗ Error detected at position {index}. Stopping processing.")
            break  # Exit the loop immediately
        print(f"  ✓ Valid reading {index + 1}: {reading}")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 3.2: Using continue to skip iterations
    print("Example 3.2: Using continue - Skip invalid data")
    temperature_data = [22.5, -999, 24.0, None, 23.8, -999, 25.2]
    valid_temperatures = []
    
    print("Processing temperature data (skipping invalid entries)...")
    for temp in temperature_data:
        if temp is None or temp == -999:
            print(f"  ⊘ Skipping invalid data: {temp}")
            continue  # Skip to next iteration
        
        valid_temperatures.append(temp)
        print(f"  ✓ Valid temperature: {temp}°C")
    
    print(f"\n  Collected {len(valid_temperatures)} valid readings")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 3.3: Break in while loop
    print("Example 3.3: Break in while loop - Search for target value")
    energy_data = [120, 145, 167, 189, 203, 215]
    target = 189
    position = 0
    found = False
    
    while position < len(energy_data):
        current_value = energy_data[position]
        print(f"  Checking position {position}: {current_value}", end="")
        
        if current_value == target:
            print(" ← Found!")
            found = True
            break  # Exit once found
        else:
            print()
        
        position += 1
    
    if found:
        print(f"\n  Target {target} found at position {position}")
    else:
        print(f"\n  Target {target} not found")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 3.4: Continue in while loop
    print("Example 3.4: Continue in while loop - Process only even indices")
    values = [10, 20, 30, 40, 50, 60]
    index = 0
    
    while index < len(values):
        if index % 2 != 0:  # Skip odd indices
            print(f"  Skipping index {index}")
            index += 1
            continue
        
        print(f"  Processing index {index}: value = {values[index]}")
        index += 1
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 3.5: Nested loops with control
    print("Example 3.5: Nested loops - Find first pair that sums to target")
    numbers = [2, 4, 6, 8, 10]
    target_sum = 14
    found_pair = False
    
    for i in range(len(numbers)):
        if found_pair:
            break  # Exit outer loop if found
        
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                print(f"  Found pair: {numbers[i]} + {numbers[j]} = {target_sum}")
                found_pair = True
                break  # Exit inner loop
    
    if not found_pair:
        print(f"  No pair found that sums to {target_sum}")


# ==============================================================================
# SECTION 4: AVOIDING INFINITE LOOPS
# ==============================================================================

def demonstrate_infinite_loop_prevention():
    """
    Understand common pitfalls.
    - Identify causes of infinite loops
    - Ensure loop conditions change
    - Test loops with small examples
    - Stop execution safely if needed
    """
    section_separator("SECTION 4: Avoiding Infinite Loops")
    
    # Example 4.1: Common infinite loop mistake (FIXED)
    print("Example 4.1: WRONG - What causes an infinite loop")
    print("❌ MISTAKE: Forgetting to update the counter")
    print("   Code: while counter < 5:")
    print("           print(counter)")
    print("           # FORGOT: counter += 1")
    print("   Result: counter stays 0, loop never ends!\n")
    
    print("✅ CORRECT: Always update loop variables")
    counter = 0
    iterations = 0
    max_iterations = 5  # Safety limit for demonstration
    
    while counter < 5 and iterations < max_iterations:
        print(f"   Counter: {counter}")
        counter += 1  # MUST update the loop variable
        iterations += 1
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 4.2: Unreachable condition (FIXED)
    print("Example 4.2: WRONG - Condition that never becomes false")
    print("❌ MISTAKE: Condition that can't be satisfied")
    print("   Code: count = 10")
    print("         while count > 0:")
    print("           count += 1  # WRONG: makes it worse!")
    print("   Result: count keeps growing, never reaches 0!\n")
    
    print("✅ CORRECT: Make sure loop progresses toward exit condition")
    count = 10
    while count > 0:
        print(f"   Count: {count}")
        count -= 1  # CORRECT: decreasing toward 0
    print("   Done!\n")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 4.3: Adding a safety limit
    print("Example 4.3: Using a safety counter to prevent infinite loops")
    print("TIP: Add a maximum iteration counter for complex conditions\n")
    
    value = 1
    max_iterations = 100  # Safety limit
    iteration_count = 0
    
    while value < 1000 and iteration_count < max_iterations:
        value *= 2  # Double the value each time
        iteration_count += 1
        print(f"   Iteration {iteration_count}: value = {value}")
    
    if iteration_count >= max_iterations:
        print(f"\n   ⚠ Reached safety limit of {max_iterations} iterations")
    else:
        print(f"\n   Completed successfully in {iteration_count} iterations")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 4.4: Testing with small examples
    print("Example 4.4: Test loops with small datasets first")
    print("TIP: Test with 3-5 items before running on large datasets\n")
    
    # Small test first
    test_data = [1, 2, 3]
    print("Testing with small dataset:")
    for item in test_data:
        print(f"   Processing: {item}")
    print("   ✓ Test passed\n")
    
    # Now safe to use with larger data
    print("Now applying to larger dataset:")
    larger_data = list(range(1, 11))
    for item in larger_data:
        print(f"   Processing: {item}", end="  ")
        if item % 5 == 0:
            print()  # New line every 5 items
    
    print("\n" + "-" * 70 + "\n")
    
    # Example 4.5: Ensuring boolean conditions change
    print("Example 4.5: Boolean conditions must be able to change")
    print("TIP: If using a boolean flag, ensure it can be set to False\n")
    
    processing = True
    items = ["item1", "item2", "item3", "STOP", "item4"]
    index = 0
    
    while processing and index < len(items):
        current_item = items[index]
        print(f"   Processing: {current_item}")
        
        if current_item == "STOP":
            processing = False  # Change the boolean condition
            print("   Stop signal received!")
        
        index += 1
    
    print("\n   Loop exited safely")
    
    print("\n" + "-" * 70 + "\n")
    
    # Summary
    print("SUMMARY: Preventing Infinite Loops")
    print("  1. Always update loop variables (counter += 1)")
    print("  2. Ensure conditions progress toward exit")
    print("  3. Use safety counters for complex logic")
    print("  4. Test with small datasets first")
    print("  5. Make sure boolean flags can change")
    print("  6. Use break when appropriate for early exit")


# ==============================================================================
# BONUS: PRACTICAL DATA PROCESSING EXAMPLES
# ==============================================================================

def bonus_practical_examples():
    """
    Apply iteration to simple data scenarios.
    Real-world examples of loop usage in data processing.
    """
    section_separator("BONUS: Practical Data Processing Examples")
    
    # Example B.1: Calculate statistics from a list
    print("Example B.1: Calculate min, max, and average")
    energy_readings = [145, 167, 132, 189, 156, 174, 198]
    
    total = 0
    minimum = energy_readings[0]
    maximum = energy_readings[0]
    
    for reading in energy_readings:
        total += reading
        if reading < minimum:
            minimum = reading
        if reading > maximum:
            maximum = reading
    
    average = total / len(energy_readings)
    
    print(f"  Data: {energy_readings}")
    print(f"  Minimum: {minimum} kWh")
    print(f"  Maximum: {maximum} kWh")
    print(f"  Average: {average:.2f} kWh")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example B.2: Filter and transform data
    print("Example B.2: Filter and transform data")
    temperatures_fahrenheit = [68, 72, 65, 75, 70, 73]
    temperatures_celsius = []
    
    print("Converting Fahrenheit to Celsius (only if >= 70°F):")
    for temp_f in temperatures_fahrenheit:
        if temp_f >= 70:
            temp_c = (temp_f - 32) * 5 / 9
            temperatures_celsius.append(temp_c)
            print(f"  {temp_f}°F → {temp_c:.1f}°C")
        else:
            print(f"  {temp_f}°F (skipped - below threshold)")
    
    print(f"\nFiltered result: {[f'{t:.1f}' for t in temperatures_celsius]}°C")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example B.3: Group and count
    print("Example B.3: Count occurrences by category")
    energy_sources = ["Solar", "Wind", "Solar", "Hydro", "Wind", "Solar", "Nuclear"]
    counts = {}
    
    for source in energy_sources:
        if source in counts:
            counts[source] += 1
        else:
            counts[source] = 1
    
    print("Energy source frequencies:")
    for source, count in counts.items():
        print(f"  {source}: {count} occurrences")
    
    print("\n" + "-" * 70 + "\n")
    
    # Example B.4: Running calculations
    print("Example B.4: Calculate running totals")
    daily_production = [120, 135, 145, 140, 155]
    running_total = 0
    
    print("Daily production with running totals:")
    for day, production in enumerate(daily_production, 1):
        running_total += production
        print(f"  Day {day}: {production} kWh (Total so far: {running_total} kWh)")
    
    print(f"\nTotal production: {running_total} kWh")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

def main():
    """
    Main function to run all demonstrations.
    """
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  LEARN LOOPS: Iterative Data Processing in Python".center(68) + "║")
    print("║" + "  Prime Knights - Applied Data Science Foundations".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    
    # Run all demonstrations
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_control()
    demonstrate_infinite_loop_prevention()
    bonus_practical_examples()
    
    # Final summary
    section_separator("COMPLETION SUMMARY")
    print("✓ Section 1: for Loops - Completed")
    print("✓ Section 2: while Loops - Completed")
    print("✓ Section 3: Loop Control (break/continue) - Completed")
    print("✓ Section 4: Infinite Loop Prevention - Completed")
    print("✓ Bonus: Practical Examples - Completed")
    print("\n" + "=" * 70)
    print("\nCongratulations! You've completed the Loops milestone.")
    print("You can now:")
    print("  • Write for loops to process sequences")
    print("  • Write while loops for condition-based repetition")
    print("  • Control loops with break and continue")
    print("  • Avoid infinite loops")
    print("  • Apply iteration to data workflows")
    print("\nNext steps: Practice with your own data and scenarios!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()

def land_development_formula(land_cost, construction_cost, potential_revenue):
    # Example formula: Revenue - (Land Cost + Construction Cost)
    profit = potential_revenue - (land_cost + construction_cost)
    return profit

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

# Example usage:
try:
    land_cost = get_float_input("Enter the cost of the land: $")
    construction_cost = get_float_input("Enter the construction cost: $")
    potential_revenue = get_float_input("Enter the potential revenue: $")

    result = land_development_formula(land_cost, construction_cost, potential_revenue)
    print(f"The estimated profit is: ${result}")
except Exception as e:
    print(f"An error occurred: {e}")

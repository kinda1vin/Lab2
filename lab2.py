def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    str_values = user_input.split(",")
    float_values = [float(value.strip()) for value in str_values] #Convert the list of strings to a list of floats
    return float_values
    
def calc_average(temps):
    if len(temps) == 0:
        return 0.0
    return sum(temps) / len(temps)

def find_min_max(temps):
    if len(temps) == 0:
        return [0, 0]
    min_temp = min(temps)
    max_temp = max(temps)
    return [int(min_temp), int(max_temp)]

def sort_temperature(temps):
    print("sort_temperature")
    return []

def calc_median_temperature(temps):
    print("calc_median_temperature")
    return 0.0

def find_medium(temps):
    temps.sort()
    length = len(temps)
    if length == 0:
        return 0.0
    if length % 2 == 0:
        return (temps[length//2 - 1] + temps[length//2]) / 2
    else:
        return temps[length//2]


#main function
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg_temp = calc_average(num_list)
    min_max_temp = find_min_max(num_list)
    median_temp = find_medium(num_list)
    
    print(f"Average temperature: {avg_temp}")
    print(f"Minimum and Maximum temperatures: {min_max_temp}")
    print(f"Median temperature: {median_temp}")

if __name__ == "__main__":
    main()
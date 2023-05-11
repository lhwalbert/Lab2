import statistics


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    sort_temperature(num_list)
    calc_average(num_list)
    find_min_max(num_list)
    calc_median_temperature(num_list)
    exit()


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():
    x = input()
    x = x.split(",")
    x_float = list(map(float, x))
    print(x_float)
    return x_float


def calc_average(num_list):
    average = sum(num_list) / len(num_list)
    print("Average: " + str(average))


def find_min_max(num_list):
    print("Lowest Temperature: " + str(min(num_list)))
    print("Highest Temperature: " + str(max(num_list)))


def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    print("Temperature sorted from lowest to highest: " + str(sorted_list))


def calc_median_temperature(num_list):
    median = statistics.median(num_list)
    print("Median: " + str(median))


if __name__ == '__main__':
    main()

def avg_diff(first_list_of_numbers: list, second_list_of_numbers: list) -> float:
    return sum(second_list_of_numbers[i] - first_list_of_numbers [i]  
            for i in range(len(first_list_of_numbers))) / len(first_list_of_numbers)
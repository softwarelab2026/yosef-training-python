def valid_input(number: str) -> bool:
    return number.isdigit() and len(number) == 5

def sum_number(number: int) -> int:
    total = 0
    while number != 0:
        total += number % 10
        number //= 10
    return total

def number_details(number: int) -> str:
    string_number = str(number)
    return f"the number is: {number}\n" \
       f"{','.join(string_number)}\n" \
       f"the sum of the number is: {sum_number(number)}"


while True:
    number_for_function = input("please enter 5 digit number: ")

    if valid_input(number_for_function):
        number_for_function = int(number_for_function)
        break

print(number_details(number_for_function))


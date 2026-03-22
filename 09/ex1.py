import sys, os

MATH_OPERATIONS = ('+', '-', '*', '//')


def valid_exercise(expression:list[str]) -> str | None:
    try:
        first_number = int(expression[0])
        operator = expression[1]
        second_number = int(expression[2])

        if operator not in MATH_OPERATIONS:
            return "not valid math operation"

        if operator == "//":
            first_number // second_number

        return None
    
    except (ZeroDivisionError):
        return "devision by zero"
    except (IndexError, ValueError):
        return "not valid exrcise"


def calculate(expression:list[str]) -> int |None:
    first_number = int(expression[0])
    operator = expression[1]
    second_number = int(expression[2])

    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "//":
        return first_number // second_number


def main():

    exercise_file = sys.argv[1]
    solution_file = sys.argv[2]
    try:
        with open(exercise_file, 'r') as ex_file:
            file_data = ex_file.read().splitlines()
            
        with open(solution_file, 'w') as solution_fo:

            for line_num, line in enumerate(file_data, start=1):
                line_splitted = line.split()
                error = valid_exercise(line_splitted)

                if error:
                    solution_fo.write(f"line: {line_num} " + error + "\n")
                else:
                    solution = calculate(line_splitted)
                    line_splitted.append("=")
                    line_splitted.append(str(solution))
                    result_line = " ".join(line_splitted)

                    solution_fo.write(result_line + "\n")

    except FileNotFoundError:
        print("file not found")
        sys.exit()

if __name__ == "__main__":
    main()
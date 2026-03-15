import sys, os

exercise_file = sys.argv[1]
solution_file = sys.argv[2]
Math_operations = ('+', '-', '*', '//')


def valid_files(file_1: str) -> bool:
    if not os.path.exists(file_1):
        return False
    return True


def valid_exercise(expression: list, line_number: int):
    if len(expression) != 3:
        return f"line {line_number}: not valid exrcise"

    first_number = expression[0]
    operator = expression[1]
    second_number = expression[2]

    if not first_number.isdigit() or not second_number.isdigit():
        return f"line {line_number}: is not a digit"

    if operator == '//' and second_number == '0':
        return f"line {line_number}: division by zero"

    if operator not in Math_operations:
        return f"line {line_number}: not valid math operation"

    return None


def calculate(expression):
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


if not valid_files(exercise_file):
    print("not valid file")
    sys.exit()


with open(exercise_file, 'r') as exercise_file:

    line_num = 1
    
    with open(solution_file, 'w') as solution_file:

        for line in exercise_file:

            line = line.split()
            error = valid_exercise(line, line_num)

            if error:
                solution_file.write(error + "\n")

            else:
                solution = calculate(line)
                line.append("=")
                line.append(str(solution))

                result_line = " ".join(line)
                solution_file.write(result_line + "\n")

            line_num += 1
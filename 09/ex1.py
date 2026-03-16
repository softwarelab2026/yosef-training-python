import sys, os

exercise_file = sys.argv[1]
solution_file = sys.argv[2]

Math_operations = ('+', '-', '*', '//')


def valid_exercise(expression, line_number):
    try:
        first_number = int(expression[0])
        operator = expression[1]
        second_number = int(expression[2])

        if operator not in Math_operations:
            return f"line {line_number}: not valid math operation"

        if operator == "//" and second_number == 0:
            return f"line {line_number}: division by zero"

        return None

    except (IndexError, ValueError):
        return f"line {line_number}: not valid exrcise"


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


try:
    with open(exercise_file, 'r') as exercise_file:

        line_num = 1

        try:
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

        except Exception:
            print("cannot open solution file")
            sys.exit()

except Exception:
    print("file not found")
    sys.exit()
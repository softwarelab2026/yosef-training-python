import sys, os

MATH_OPERATIONS = ('+', '-', '*', '//')



def valid_files(file_1: str) -> bool:
    if not os.path.exists(file_1):
        return False
    return True


def valid_exercise(expression: list[str]):
    if len(expression) != 3:
        return  "not valid exrcise"

    first_number = expression[0]
    operator = expression[1]
    second_number = expression[2]

    if not first_number.isdigit() or not second_number.isdigit():
        return "is not a digit"

    if operator == '//' and second_number == '0':
        return "division by zero"

    if operator not in MATH_OPERATIONS:
        return "not valid math operation"

    return None


def calculate(expression:list[str]) -> int:
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
    

    if not valid_files(exercise_file):
        print("not valid file")
        sys.exit()


    with open(exercise_file, 'r') as exercise_fo:
        
        with open(solution_file, 'w') as solution_fo:

            for line_num, line in enumerate(exercise_fo, start=1):

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

if __name__ == "__main__":
    main()
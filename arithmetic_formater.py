def arithmetic_arranger(problems, rslt=False):
    problems = problems

    status = True

    # Input Control

    # Firs Condition
    if len(problems) > 5:
        print('Error: Too many problems.')
        status = False

    # Second Condition
    for operation in problems:
        plus = operation.rfind('+')
        minus = operation.rfind('-')

        if plus & minus == -1:
            print("Error: Operator must be '+' or '-'.")
            status = False

    # Third & Fourth Condition
    for operation in problems:
        operand = operation.split()

        for element in operand:
            if len(element) > 4:
                print('Error: Numbers cannot be more than four digits.')
                status = False

        try:
            int(operand[0]) & int(operand[2])
        except:
            print('Error: Numbers must only contain digits.')
            status = False

    arranged_problems = str()
    # Operations
    if status == True:

        operation = int()
        line1 = list()
        line2 = list()
        br = list()
        result = list()

        for operation in problems:
            operand = operation.split()

            line1.append((5 - len(operand[0])) * " " + operand[0])

            line2.append((2 - len(operand[2])) *
                         " " + operand[1] + " " + operand[2])

            br_num = len(operand[0])

            if br_num < len(operand[1] + " " + operand[2]):
                br_num = len(operand[1] + " " + operand[2])
            br.append(br_num*"-")

            if operand[1] == "+":
                rst = int(operation[0]) + int(operand[2])
                rln = len(str(rst))

                result.append((4-rln)*" " + str(rst))

            else:
                rst = int(operation[0]) - int(operand[2])
                rln = len(str(rst))

                result.append((4-rln)*" " + str(rst))

        for i in line1:
            arranged_problems = arranged_problems + str(i)
        arranged_problems = arranged_problems + " \n"

        for i in line2:
            arranged_problems = arranged_problems + str(i) + " "
        arranged_problems = arranged_problems + " \n"
        for i in br:
            arranged_problems = arranged_problems + str(i) + " "
        arranged_problems = arranged_problems + " \n"
        if rslt == True:
            for i in result:
                arranged_problems = arranged_problems + str(i) + " "
            arranged_problems = arranged_problems + " \n"

    return arranged_problems


print(arithmetic_arranger(
    ["32 * 698", "3801 - 2", "45 + 43", "123 + 49"], True))

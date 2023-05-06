if input('Two Factor?(y/n): ') == 'y':
    digits = [*input('Input Two Factor: ')]
    digits = [eval(c) for c in digits]
    code = []
    hold = digits[4] + digits[5]
    hold = hold + int(input('#Batteries: '))
    code.append(hold%20)
    hold = digits[0] + digits[1]
    hold = hold + int(input('#Solved Modules: '))
    code.append(hold%20)
    code.append((code[0] + code[1])%20)
    input(code)
else:
    code = []
    hold2 = int(input('#Solved Modules: '))
    hold = hold2 + int(input('Last # Serial: '))
    hold = hold + int(input('#Batteries: '))
    code.append(hold%20)
    hold = int(input('#Modules: '))
    hold = hold + hold2
    code.append(hold%20)
    code.append((code[0] + code[1])%20)
    input(code)
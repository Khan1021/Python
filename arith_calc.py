import re


def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = {'top': [], 'bottom': [], 'line': [], 'res': []}

  for problem in problems:
    parts = problem.split()

    firstNumber = parts[0]
    operator = parts[1]
    secondNumber = parts[2]

    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if not (firstNumber.isdigit() and secondNumber.isdigit()):
      return "Error: Numbers must only contain digits."

    if len(firstNumber) > 4 or len(secondNumber) > 4:
      return "Error: Numbers cannot be more than four digits."

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = "-" * length
    res = str(eval(problem)).rjust(length)

    arranged_problems['top'].append(top)
    arranged_problems['bottom'].append(bottom)
    arranged_problems['line'].append(line)
    arranged_problems['res'].append(res)

  arranged_string = ('    '.join(arranged_problems['top']) + '\n' +
                     '    '.join(arranged_problems['bottom']) + '\n' +
                     '    '.join(arranged_problems['line']))

  if solve:
    arranged_string += '\n' + '    '.join(arranged_problems['res'])

  return arranged_string

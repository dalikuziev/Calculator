from emoji import logo

print(logo)
number1 = int(input("birinchi sonni kiriting: "))
print("+\n-\n*\n/\n^")
operator = input("qanday amalni bajarmoqchisiz: ")
number2 = int(input("ikkinchi sonni kiriting: "))

def amal(number1, operator, number2):
  if operator == "+":
    return number1 + number2
  elif operator == "-":
    return number1 - number2
  elif operator == "*":
    return number1 * number2
  elif operator == "/":
    return number1 / number2
  elif operator == "^":
    return number1 ** number2
print(f"{number1} {operator} {number2} = {amal(number1, operator, number2)}")
while True:
  continue_calc = input("Kalkulyatordan chiqib ketish uchun exit deb yozing\nAmalni davom ettirasizmi yes/no: ").lower()
  if continue_calc == "exit":
    break
  if continue_calc == "yes":
    number1 = amal(number1, operator, number2)
    operator = input("qanday amalni bajarmoqchisiz: ")
    number2 = int(input("ikkinchi sonni kiriting: "))
  else:
    print(logo)
    number1 = int(input("birinchi sonni kiriting: "))
    operator = input("qanday amalni bajarmoqchisiz: ")
    number2 = int(input("ikkinchi sonni kiriting: "))
  print(f"{number1} {operator} {number2} = {amal(number1, operator, number2)}")

def Calculadora():
  print("Calculadora")
  while True:
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      print("Resultado: ", num1 + num2)
    elif escolha == "2":
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      print("Resultado: ", num1 - num2)
    elif escolha == "3":
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      print("Resultado: ", num1 * num2)
    elif escolha == "4":
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      print("Resultado: ", num1 / num2)
    elif escolha == "5":
      break
    else:
      print("Opção inválida")
  print("Fim do programa")
Calculadora()
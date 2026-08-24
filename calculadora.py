print("=== CALCULADORA ===")
print("Digite uma conta, exemplo: 2+2")
print("Digite 'sair' para encerrar")

while True:
    conta = input("\nConta: ")

    if conta.lower() == "sair":
        print("Calculadora encerrada!")
        break

    try:
        resultado = eval(conta)
        print("Resultado:", resultado)

    except:
        print("Erro: digite uma conta válida!")

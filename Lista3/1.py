"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido."""

while True:
    nota = float(input("Digite um numero entre 0 e 10: "))

    if 0 <= nota <= 10:
        print(f"Numero = {nota:.1f}")
        break
    else:
        print("Numero invalido, digite um entre 0 e 10. ")

import os 

Idade = int(input("Digite sua idade:\n"))
total = float(input("Digite o valor total dos produtos:\n"))

os.system('clear')

if(Idade>=18):
    print("Você recebeu um desconto!")
    desconto = total * 0.1
    final = total - desconto
    print(f"O desconto foi de R${desconto:.2f} e o total é de R${final:.2f}")
else:
    print(f"Infelizmente você não possui direito ao desconto e o seu valor final é de R${total:.2f}")


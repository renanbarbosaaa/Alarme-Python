porta = janela = "F"  
alarme = False

porta = input("informe se a porta está aberta ou fechada: ")
janela = input("informe se a janela está aberta ou fechada: ")

alarme = porta == "A" or janela == "A"

mensagem = "ALARME DISPARADO - " + str(alarme)

print(mensagem)
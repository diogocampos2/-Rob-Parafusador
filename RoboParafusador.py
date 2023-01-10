def menosemais(tarefas: list):
	indice = 7
	valordavez = 0
	instrucaotarefa = []
	quantidademenosinst = 8
	quantidademaisinst = 0
	menosinst = 0
	maisinst = 0
	for i in tarefas:
		valordavez = i
		while i >= 1:
			resto = i % 2
			if resto == 1:
				instrucaotarefa.append(resto)
				i = i // 2
				indice = indice - 1
			else:  
				i = i // 2
				indice = indice - 1
		if len(instrucaotarefa) >= quantidademaisinst:
			quantidademaisinst = len(instrucaotarefa)
			maisinst = valordavez
		if len(instrucaotarefa) <= quantidademenosinst:
			quantidademenosinst = len(instrucaotarefa)
			menosinst = valordavez
		instrucaotarefa.clear()
	print(f"A instrucao que exigiu menos tarefas simultaneas do robo foi a {menosinst}: {quantidademenosinst} tarefas.")
	print(f"A instrucao que exigiu mais tarefas simultaneas do robo foi a {maisinst}: {quantidademaisinst} tarefas.")

#==================================================================================================================================

def contagem(inst: list):
	print(f"1. parafusar capo: {inst[7]}.")
	print(f"2. parafusar tampa do porta-malas: {inst[6]}.")
	print(f"3. parafusar eixos: {inst[5]}.")
	print(f"4. parafusar rodas: {inst[4]}.")
	print(f"5. parafusar motor: {inst[3]}.")
	print(f"6. parafusar portas: {inst[2]}.")
	print(f"7. parafusar chassi: {inst[1]}.")
	print(f"8. parafusar assoalho: {inst[0]}.")

	#pegando a tarefa mais realizada
	i = 0
	maior = 0
	posmaior = 0
	funcoes = ["assoalho", "chassi", "portas", "motor", "rodas", "eixos", "tampa do porta-malas", "capô"]
	while i < len(inst):
		if inst[i] > maior:
			maior = inst[i]
			posmaior = i
		i = i + 1

	#em caso de empate
	contador = 0
	menorcodigo = 0
	for i in inst:
		if i == maior:
			contador = contador + 1
	if contador > 1:
		i = 0
		while i < len(inst):
			if inst[i] == maior:
				menorcodigo = i
			i = i + 1
		print(f"A tarefa mais realizada foi parafusar {funcoes[menorcodigo]}: {maior} vezes.")
	else:
		print(f"A tarefa mais realizada foi parafusar {funcoes[posmaior]}: {maior} vezes.")

	#pegando a tarefa menos realizada
	menos = 0
	posmenor = 0
	while i < len(inst):
		if inst[i] <= menos:
			menos = inst[i]
			posmenor = i
		i = i + 1
        
	#em caso de empate
	contador = 0
	menorcodigo = 0
	for i in inst:
		if i == menos:
			contador = contador + 1
	if contador > 1:
		i = 0
		while i < len(inst):
			if inst[i] == menos:
				menorcodigo = i
			i = i + 1
		print(f"A tarefa menos realizada foi parafusar {funcoes[menorcodigo]}: {menos} vezes.")
	else:
		print(f"A tarefa menos realizada foi parafusar {funcoes[posmenor]}: {menos} vezes.")

#==================================================================================================================================

def instrucao(binario):
	i = 0
	while i < len(binario):
		if binario[i] == 0:
			inst[i] = inst[i] + 0
		elif binario[i] == 1:
			inst[i] = inst[i] + 1	

		i = i + 1
#==================================================================================================================================

def binario(n):
	indice = 7
	binario = [0] * 8
	while n >= 1:
		resto = n % 2  
		n = n // 2
		binario[indice] = resto
		indice = indice - 1
	instrucao (binario)

#==================================================================================================================================

def main():
	tarefas = []
	while True:
		n = int(input())
		if n == 0:
			contagem(inst)
			menosemais(tarefas)
			break
		else:
			tarefas.append(n)
			binario(n)
inst = [0] * 8	
main()    
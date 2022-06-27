# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word # A palavra
		self.missed_letters = [] # Lista para as letras erradas
		self.guessed_letters = [] #Lista para as letras certas
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if (letter in self.word) and (letter not in self.guessed_letters):
			self.guessed_letters.append(letter) #Insere a letra na lista de letras certas
		elif (letter not in self.word) and (letter not in self.missed_letters):
			self.missed_letters.append(letter) #Insere a letra na lista de letras erradas
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6) # O jogo termina quando o usário acerta a palavra ou ele erra as 6 tentativas
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word(): # Se não tiver _, venceu o jogo
			return True
		return False # Caso contrário, está perdendo
		
	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = '' # Definição de um objeto com espaço vazio
		for letter in self.word:
			if letter not in self.guessed_letters: # Se a letra não estiver dentro da lista de letras corretas
				rtn += '_' # Preenche com um _
			else:
				rtn += letter # Se estiver correto, preenche com a letra
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self): # Permite a interação com o usuário
		print (board[len(self.missed_letters)]) # Busca o índice a partir do len para analisar o tamanho da lista
		print ('\nPalavra: ' + self.hide_word()) # Imprime palavra e chama a análise da letra na lista
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines() # Lê uma única linha
        return bank[random.randint(0,len(bank))].strip()

# Método Main - Execução do Programa
def main():

	# Objeto - criação da instância do Hagman
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over(): 
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
words = 'aro|clara|patata|brillo'
letter = 'a'
palabras = words.split('|')
letter_counter = {}


for palabra in palabras:
    contador = palabra.count(letter)

    letter_counter[palabra] = contador
    
print(letter_counter)

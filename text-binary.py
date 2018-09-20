# Programa que convierte texto a binario y viceversa

# Base binaria para descifrar mensajes binarios a texto
binary_base = [1, 2, 4, 8, 16, 32, 64, 128]


def cypher(message):
    """
    metodo que separa cada letra de un texto
    convierte cada letra del texto en binario
    junta los binarios en la lista cypher_words
    y retorna la lista cypher_words concatenada
    :param message: texto a convertir
    :return: texto en binario concatenado
    """
    cypher_words = []
    for letter in message:
        # format(value, format_spec) // 'b' = binaria
        # ord = representacion Unicode de un caracter
        cypher_letter = format(ord(letter), 'b')
        cypher_words.append(cypher_letter)

    # join = str.join(sequence)
    return ' '.join(cypher_words)


def decipher(message):
    """
    metodo que obtiene un texto en binario
    y lo convierte en un string
    :param message: Texto en binario
    :return: Cadena de texto concatenada
    """
    # Crea una lista con los binarios, separacion (" ")
    words = message.split(' ')
    decipher_message = []
    # Separando cada item de la lista
    for word in words:
        word = str(word)
        sumatory = 0
        """
        Cada item esta compuesto de 8 caracteres, unicamente 1 y 0
        Los binarios se leen de derecha a izquierda, por eso enumerate(word[::-1])
        Solo los caracteres "1" se suman de acuerdo a su base binaria: binary_base
        """
        for value, letter in enumerate(word[::-1]):
            if int(letter) == 1:
                sumatory += binary_base[value]
        # La sumatoria es convertida a String
        # con el comando chr obtienes el caracter de un Unicode
        # EJM: chr(97) = 'a' / chr(98) = 'b' /
        decipher_letter = chr(sumatory)
        decipher_message.append(decipher_letter)

    # uniendo la lista de caracteres descifrados en un solo string
    return "".join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe un mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)
        elif command == 'd':
            message = str(input('Escribe un mensaje: '))
            decipher_message = decipher(message)
            print('')
            print(decipher_message)
        elif command == 's':
            exit()
            print('salir')
        else:
            print('¡Comando no encontrado!')


print('M E N S A J E S  C I F R A D O S')
run()
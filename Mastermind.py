import cv2
import random

def creacionLogo():
    img = cv2.imread('Ficheros necesarios/mastermind_logorigin.png')

    texto = 'Equipo 6'
    posicion = (105, 55)
    font = cv2.FONT_HERSHEY_DUPLEX
    tama_letra = 2
    color_letra = (29, 152, 248)
    grosor_letra = 2

    cv2.putText(img, texto, posicion, font, tama_letra, color_letra, grosor_letra)

    texto2 = '1DAM Curso 2023/24'
    posicion2 = (65, 310)
    font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    tama_letra2 = 1.05
    color_letra2 = (37, 40, 219)
    grosor_letra2 = 2

    cv2.putText(img, texto2, posicion2, font2, tama_letra2, color_letra2, grosor_letra2)

    cv2.imwrite("textoIMG.jpg", img)
    return


def num_aleatorio():
    # Generar secuencia numérica
    combinacion = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return combinacion


def pal_aleatoria():
    # Obtener palabra aleatoria del archivo palabras.dat
    with open("Ficheros necesarios/palabras.dat", "rb") as file:
        palabras = file.readlines()
        combinacion = random.choice(palabras).decode().strip()
    return combinacion


def ocultar_texto_en_imagen():
    # Solicitar al usuario el tipo de combinación a generar
    tipo_combinacion = int(input("Seleccione el tipo de combinación a generar (1: Números, 2: Palabra): "))

    if tipo_combinacion == 1:
        combinacion = num_aleatorio()
    elif tipo_combinacion == 2:
        combinacion = pal_aleatoria()
    else:
        print("Opción no válida. Debe seleccionar 1 o 2.")
        return
    print(f"Combinación generada y ocultada: {combinacion}")


    # Cargar la imagen
    img2 = cv2.imread("textoIMG.jpg")

    # Convertir el texto a binario
    pal_binario = ''.join(format(ord(caracter), '08b') for caracter in combinacion)

    # Obtener las dimensiones de la imagen
    alto, ancho, canales = img2.shape

    # Variable para seguir la posición del bit en el texto a ocultar
    bit_pos = 0

    # Iterar sobre los píxeles de la imagen
    for i in range(alto):
        for j in range(ancho):
            for k in range(canales):
                if bit_pos < len(pal_binario):
                    # Reemplazar el bit menos significativo con el bit del texto
                    img2[i, j, k] = img2[i, j, k] & ~1 | int(pal_binario[bit_pos])
                    bit_pos += 1

    # Guardar la nueva imagen
    cv2.imwrite("textoIMG.jpg", img2)


def verificarPalabraAgregada(codigo_imagen):
    # Verificar si se ha añadido la palabra al código de la imagen
    patron = "Combinación generada y ocultada:"
    return patron in codigo_imagen


def juegoMastermind():
    # Solicitar al usuario el tipo de combinación a generar
    tipo_combinacion = int(input("Seleccione el tipo de combinación a generar (1: Números, 2: Palabra): "))

    print('\n\t\tAPLICACIÓN MASTERMIND')
    print('\n\tSe ha recuperado la combinación')
    nick = input('\n\tTu nickname, por favor: ')
    print(f'\n\t¡Comienza el juego para {nick}!\n')

    if tipo_combinacion == 1:
        combinacion = num_aleatorio()
        resultado = ''
        print('\t\t¡Tienes 4 intentos!')
        print('\t\t\t¡Comenzamos!\n')
        print('\tPropuesto\t\t\tResultado\n')
        propuesto = input('Escribe el número propuesto: ')
        for pos_numero in range(len(propuesto)):
            numero = propuesto[pos_numero]
            if propuesto[pos_numero] == combinacion[pos_numero]:
                resultado += ' ◯ '

            elif str(numero) in combinacion:
                resultado += ' - '

            else:
                resultado += ' x '
        print(resultado + '\n')



    elif tipo_combinacion == 2:
        combinacion = pal_aleatoria()
        resultado = ''
        print('\t\t¡Tienes 7 intentos!')
        print('\t\t\t¡Comenzamos!\n')
        print('\tPropuesto\t\t\tResultado\n')
        propuesto = input('Escribe la palabra propuesta: ')
        for pos_letra in range(len(propuesto)):
            letra = propuesto[pos_letra]
            if propuesto[pos_letra] == combinacion[pos_letra]:
                resultado += ' ◯ '

            elif str(letra) in combinacion:
                resultado += ' - '

            else:
                resultado += ' x '
        print(resultado + '\n')
    return


def rankingRecord():
    # Implementar la lógica del ranking de récords
    # (Esta parte del código está pendiente de implementar)
    return


def informePartidas():
    # Implementar la generación del informe de partidas en PDF
    # (Esta parte del código está pendiente de implementar)
    return


def menu():
    print("\n\t\t\tAPLICACIÓN MASTERMIND\n")

    bucle = True
    while bucle:
        print("\t\t1) Creación del logo de equipo\n"
              "\t\t2) Generación y ocultado de la combinación\n"
              "\t\t3) Juego Mastermind\n"
              "\t\t4) Ranking de récords\n"
              "\t\t5) Informe de las partidas (PDF)\n"
              "\t\t6) Salir\n")
        opcion = int(input("\t\tOpción: "))
        print()
        if opcion == 1:
            creacionLogo()
        elif opcion == 2:
            ocultar_texto_en_imagen()
        elif opcion == 3:
            juegoMastermind()
        elif opcion == 4:
            rankingRecord()
        elif opcion == 5:
            informePartidas()
        elif opcion == 6:
            bucle = False


if __name__ == '__main__':
    menu()

import cv2
import random
import time
import pickle

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
    print(f"Combinación generada y ocultada: {combinacion} \n")


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
    global tiempo_inicial, tiempo_final
    tipo_combinacion = int(input("Seleccione el tipo de combinación a generar (1: Números, 2: Palabra): "))

    print('\n\t\tAPLICACIÓN MASTERMIND')
    print('\n\tSe ha recuperado la combinación')
    nick = input('\n\tTu nickname, por favor: ')
    print(f'\n\t¡Comienza el juego para {nick}!\n')

    if tipo_combinacion == 1:
        combinacion = num_aleatorio()
        print('\t\t¡Tienes 4 intentos!')
        print('\t\t\t¡Comenzamos!\n')
        intentos_max = 4
        intento = 0
        final = ''
        while intento < intentos_max:
            tiempo_inicial = time.time()
            propuesto = input('Escribe el número propuesto: ')
            intento += 1
            if len(propuesto) == 5:
                resultado = ''
                for pos_numero in range(len(propuesto)):
                    numero = propuesto[pos_numero]
                    if propuesto[pos_numero] == combinacion[pos_numero]:
                        resultado += ' ◯ '

                    elif str(numero) in combinacion:
                        resultado += ' - '

                    else:
                        resultado += ' x '

                print(resultado + '\n')
                final = final + '\n\t  ' + propuesto + '\t\t\t ' + resultado

                if resultado == ' ◯  ◯  ◯  ◯  ◯ ':
                    print('\tPropuesto\t\t\tResultado')
                    print(final)

                    print('\n\t¡Has adivinado la combinación!')
                    print(f'\t\t\t¡En {intento} intentos!')
                    volver_jugar = input('\n\t\t¿Volvemos a jugar (S/N)? ')

                    if volver_jugar == 'S' or volver_jugar == 's':
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('Fin del juego')
                    else:
                        print('Tienes que escribir S (Sí) o N (No)')

                    tiempo_final = time.time()
                    tiempo = tiempo_final - tiempo_inicial
                    rankingRecord(nick, intento, tiempo)
                    break
                elif intento == 4 and resultado != ' ◯  ◯  ◯  ◯  ◯ ':
                    print('\tPropuesto\t\t\tResultado')
                    print(final)

                    print('\n\t\t¡Has agotado los intentos!')

                    volver_jugar = input('\n\t\t¿Volvemos a jugar (S/N)? ')

                    if volver_jugar == 'S' or volver_jugar == 's':
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('Fin del juego')
                    else:
                        print('Tienes que escribir S (Sí) o N (No)')
                    break
            else:
                print('El número tiene que tener 5 dígitos')
                intento -= 1




    elif tipo_combinacion == 2:
        combinacion = pal_aleatoria()
        print('\t\t¡Tienes 7 intentos!')
        print('\t\t\t¡Comenzamos!\n')
        intentos_max = 7
        intento = 0
        final = ''
        while intento < intentos_max:
            tiempo_inicial = time.time()
            propuesto = input('Escribe la palabra propuesta: ')
            intento += 1
            if len(propuesto) == 8:
                resultado = ''
                for pos_numero in range(len(propuesto)):
                    numero = propuesto[pos_numero]
                    if propuesto[pos_numero] == combinacion[pos_numero]:
                        resultado += ' ◯ '

                    elif str(numero) in combinacion:
                        resultado += ' - '

                    else:
                        resultado += ' x '

                print(resultado + '\n')
                final = final + '\n\t' + propuesto + '\t' + resultado

                if resultado == ' ◯  ◯  ◯  ◯  ◯ ':
                    print('\tPropuesto\t\t\tResultado')
                    print(final)

                    print('\n\t¡Has adivinado la combinación!')
                    print(f'\t\t\t¡En {intento} intentos!')
                    volver_jugar = input('\n\t\t¿Volvemos a jugar (S/N)? ')

                    if volver_jugar == 'S' or volver_jugar == 's':
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('Fin del juego')
                    else:
                        print('Tienes que escribir S (Sí) o N (No)')

                    tiempo_final = time.time()
                    tiempo = tiempo_final - tiempo_inicial
                    rankingRecord(nick, intento, tiempo)
                    break
                elif intento == 7 and resultado != ' ◯  ◯  ◯  ◯  ◯ ':
                    print('\tPropuesto\t\t\tResultado')
                    print(final)

                    print('\n\t\t¡Has agotado los intentos!')

                    volver_jugar = input('\n\t\t ¿Volvemos a jugar (S/N)? ')

                    if volver_jugar == 'S' or volver_jugar == 's':
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('Fin del juego')
                    else:
                        print('Tienes que escribir S (Sí) o N (No)')
                    break
            else:
                print('La palabra tiene que tener 7 letras')
                intento -= 1
    return


def rankingRecord(fnick, fintento, ftiempo):
    f = open("ranking.dat", 'rb')
    ranking = pickle.load(f)
    jugador = {'Nombre': fnick, 'Tiempo': ftiempo, 'Intentos': fintento}
    ranking.append(jugador)
    ranking_archivo = ranking[:10]
    f = open("ranking.dat", 'wb')
    pickle.dump(ranking_archivo, f)
    f.close()
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

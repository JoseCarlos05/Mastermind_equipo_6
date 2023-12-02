import cv2
import random
import time
import pickle
from stegano import lsb
import os

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

    cv2.imwrite("textoIMG.png", img)
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


def ocultar_mensaje_en_imagen():
    if os.path.exists("textoIMG_ocultado.png"):
        os.remove("textoIMG_ocultado.png")
    tipo_combinacion = int(input("Seleccione el tipo de combinación a generar (1: Números, 2: Palabra): "))
    if tipo_combinacion == 1:
        combinacion = num_aleatorio()
        ocultado = lsb.hide("textoIMG.png", combinacion)
        ocultado.save("textoIMG_ocultado.png")
        print("\nCombinación generada y ocultada\n")
    elif tipo_combinacion == 2:
        combinacion = pal_aleatoria()
        ocultado = lsb.hide("textoIMG.png", combinacion)
        ocultado.save("textoIMG_ocultado.png")
        print("\nCombinación generada y ocultada\n")
    else:
        print('Tienes que elegir entre las opciones (1: Números, 2: Palabra): ')
    return


def verificarPalabraAgregada(codigo_imagen):
    # Verificar si se ha añadido la palabra al código de la imagen
    patron = "Combinación generada y ocultada:"
    return patron in codigo_imagen


def juegoMastermind():
    # Solicitar al usuario el tipo de combinación a generar
    global tiempo_inicial, tiempo_final
    print('\n\t\tAPLICACIÓN MASTERMIND')
    print('\n\tSe ha recuperado la combinación')
    nick = input('\n\tTu nickname, por favor: ')
    print(f'\n\t¡Comienza el juego para {nick}!\n')
    combinacion = lsb.reveal("textoIMG_ocultado.png")

    if len(combinacion) == 5:
        combinacion = lsb.reveal("textoIMG_ocultado.png")
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
                        print('\n')
                        ocultar_mensaje_en_imagen()
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('\nFin del juego')
                    else:
                        print('\nTienes que escribir S (Sí) o N (No)')

                    tiempo_final = time.time()
                    tiempo = tiempo_final - tiempo_inicial
                    hora = time.strftime("%H:%M:%S", time.localtime())
                    fecha = time.strftime("%Y-%m-%d", time.localtime())
                    actualizar_rankingRecord(nick, intento, tiempo, hora, fecha)
                    break
                elif intento == 4 and resultado != ' ◯  ◯  ◯  ◯  ◯ ':
                    print('\tPropuesto\t\t\tResultado')
                    print(final)

                    print('\n\t\t¡Has agotado los intentos!')

                    volver_jugar = input('\n\t\t¿Volvemos a jugar (S/N)? ')

                    if volver_jugar == 'S' or volver_jugar == 's':
                        ocultar_mensaje_en_imagen()
                        juegoMastermind()
                    elif volver_jugar == 'N' or volver_jugar == 'n':
                        print('Fin del juego')
                    else:
                        print('Tienes que escribir S (Sí) o N (No)')
                    break
            else:
                print('El número tiene que tener 5 dígitos')
                intento -= 1




    elif len(combinacion) == 8:
        combinacion = lsb.reveal("textoIMG_ocultado.png")
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
                    hora = time.strftime("%H:%M:%S", time.localtime())
                    fecha = time.strftime("%Y-%m-%d", time.localtime())
                    actualizar_rankingRecord(nick, intento, tiempo, hora, fecha)
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


def actualizar_rankingRecord(fnick, fintento, ftiempo, fhora, ffecha):
    f = open("ranking.dat", 'rb')
    try:
        ranking = pickle.load(f)
    except EOFError:
        ranking = list()
    f.close()
    jugador = {'Nombre': fnick, 'Tiempo': ftiempo, 'Intentos': fintento, 'Hora': fhora, 'Fecha': ffecha}
    ranking.append(jugador)
    ranking_archivo = ranking[:10]
    f = open("ranking.dat", 'wb')
    pickle.dump(ranking_archivo, f)
    f.close()
    return


def rankingRecord():
    f = open("ranking.dat", 'rb')
    try:
        ranking = pickle.load(f)
    except EOFError:
        ranking = list()
        print('Todavía no hay registros de partidas jugadas.')
    f.close()
    ranking10 = sorted(ranking, key=lambda x: (x['Intentos'], x['Tiempo']))
    print('Top 10 jugadores: ')
    for jugadores in ranking10:
        print('El jugador %s consiguió a las %s del dia %s adivinar la combianción en %s intentos y %s segundos.' % (jugadores['Nombre'], jugadores['Hora'], jugadores['Fecha'], jugadores['Intentos'], jugadores['Tiempo']))
    print()


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
            ocultar_mensaje_en_imagen()
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

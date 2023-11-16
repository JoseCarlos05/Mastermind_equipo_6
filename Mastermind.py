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


def generacionOcultado():
    # Solicitar al usuario el tipo de combinación a generar
    tipo_combinacion = int(input("Seleccione el tipo de combinación a generar (1: Números, 2: Palabra): "))

    if tipo_combinacion == 1:
        # Generar secuencia numérica
        combinacion = ''.join(str(random.randint(0, 9)) for _ in range(5))
    elif tipo_combinacion == 2:
        # Obtener palabra aleatoria del archivo palabras.dat
        with open("Ficheros necesarios/palabras.dat", "rb") as file:
            palabras = file.readlines()
            combinacion = random.choice(palabras).decode().strip()
    else:
        print("Opción no válida. Debe seleccionar 1 o 2.")
        return

    print(f"Combinación generada y ocultada: {combinacion}")
    return combinacion


def ocultadoPalabra():

    return


def verificarPalabraAgregada(codigo_imagen):
    # Verificar si se ha añadido la palabra al código de la imagen
    patron = "Combinación generada y ocultada:"
    return patron in codigo_imagen


def juegoMastermind():
    print('\n\t\tAPLICACIÓN MASTERMIND')
    print('\n\tSe ha recuperado la combinación')
    nick = input('\n\t\tTu nickname, por favor: ')
    print(f'\n\t¡Comienza el juego para {nick}!')
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
            generacionOcultado()
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

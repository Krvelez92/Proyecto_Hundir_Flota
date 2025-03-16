##########################################
#####          LIBRERIAS             #####
##########################################

import numpy as np
import random
import time

##########################################
#####          FUNCIONES             #####
##########################################

''' 
Resumen:

Creación de Tableros y Barcos:
    - crear_tablero(tamaño:tuple=(10,10))
    - crear_barco(eslora:int)
    - crear_barco_aleatorio(eslora:int)
    - colocar_barco(barco:list, tablero, eslora:int, flota_barcos:list, funcion)
    - llenar_tablero(flota:dict, tablero, funcion)

Interacción del Juego:
    - imprimir(tablero_user, tablero_enemigo_v)
    - disparar(casilla:tuple, tablero, tablero_v, flota:list)
    - validacion_tablero(tablero)

 Ejecución del Juego:
    - iniciar_juego(flota:dict={3:2, 2:3, 1:4})
    - turno_user(tablero_enemigo, tablero_enemigo_v, tablero_user, flota_enemigo:list)
    - turno_enemigo(tablero_user, tablero_enemigo_v, flota_user:list)
    - juego(flota:dict={3:2, 2:3, 1:4})

'''
#----------------------------------------------------------------------------------------------------------------------------------

def crear_tablero(tamaño:tuple=(10,10)):
    ''' 
    Esta función crear los tablero iniciales para el juego.

    Input:
        tamaño: tupla

    Output:
        tablero: array
    '''
    tablero = np.full(tamaño, '~') 
    return tablero

#----------------------------------------------------------------------------------------------------------------------------------

def crear_barco(eslora:int):
    ''' 
    Esta es una función que crea los barcos de forma manual.

    Input:
        eslora: int
    
    Output:
        barco: list
    '''
    # Input Usuario primera posicion del barco
    barco = input(f'Ingresa la posición inicia de tu barco eslora {eslora}.\nRecuerda el formato a seguir: ejemplo --> 0,1  ').strip()
    try:
        barco =  list(barco.split(','))
        barco = [tuple([int(x) for x in barco])]
    except:
        print(f'El formato ingresado no es el correcto vuelve a intentarlo.')
        barco = input(f'Ingresa la posición inicia de tu barco eslora {eslora}.\nRecuerda el formato a seguir: ejemplo --> 0,1  ').strip()
        barco =  list(barco.split(','))
        barco = [tuple([int(x) for x in barco])]

    # Input Usuario orientacion del barco
    posicion = input('Ingresa la orientación del barco. Los valores posibles son: Norte, Sur, Este y Oeste. Elige uno y escribelo.  ').lower().strip()
    posicion = posicion.lower().strip()

    # Rellenar barco segun su eslora.
    while len(barco) < eslora:
        fila, columna = barco[-1] 

        # NORTE
        if posicion == "norte":
            fila = fila - 1
            if fila >= 0 and fila <= 9:
                barco.append((fila, columna))
            else:
                barco.clear()
                print(f'Error la ubicación inicial del barco segun su eslora {eslora} y su orientacion esta fuera de tablero.')
                barco = crear_barco(eslora)

        # SUR        
        elif posicion == "sur":
            fila = fila + 1
            if fila >= 0 and fila <= 9:
                barco.append((fila, columna))
            else:
                barco.clear()
                print(f'Error la ubicación inicial del barco segun su eslora {eslora} y su orientacion esta fuera de tablero.')
                barco = crear_barco(eslora)
        
        # ESTE 
        elif posicion == "este":
            columna = columna + 1
            if columna >= 0 and columna <= 9:
                barco.append((fila, columna))
            else:
                barco.clear()
                print(f'Error la ubicación inicial del barco segun su eslora {eslora} y su orientacion esta fuera de tablero.')
                barco = crear_barco(eslora)
        
        # OESTE 
        elif posicion == "oeste":
            columna = columna - 1
            if columna >= 0 and columna <= 9:
                barco.append((fila, columna))
            else:
                barco.clear()
                print(f'Error la ubicación inicial del barco segun su eslora {eslora} y su orientacion esta fuera de tablero.')
                barco = crear_barco(eslora)            
               
        else:
            barco.clear()
            print('Esta orientación no existe')
            barco = crear_barco(eslora)

    return barco

#----------------------------------------------------------------------------------------------------------------------------------

def crear_barco_aleatorio(eslora:int):
    ''' 
    Esta es una función que crea los barcos de forma aleatoria.

    Input:
        eslora: int
    
    Output:
        barco_aleatorio: list
    '''
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    barco_aleatorio = [(fila, columna)]

    orientacion = random.choice(['norte', 'sur', 'este', 'oeste'])

    while len(barco_aleatorio) < eslora:
        # NORTE
        if orientacion == "norte":
            fila = fila - 1
            if fila >= 0 and fila <= 9:
                barco_aleatorio.append((fila, columna))
            else:
                barco_aleatorio.clear()
                barco_aleatorio = crear_barco_aleatorio(eslora)   

        # SUR
        elif orientacion == "sur":
            fila = fila + 1
            if fila >= 0 and fila <= 9:
                barco_aleatorio.append((fila, columna))
            else:
                barco_aleatorio.clear()
                barco_aleatorio = crear_barco_aleatorio(eslora)  

        # ESTE
        elif orientacion == "este":
            columna = columna + 1
            if columna >= 0 and columna <= 9:
                barco_aleatorio.append((fila, columna))
            else:
                barco_aleatorio.clear()
                barco_aleatorio = crear_barco_aleatorio(eslora) 

        else:
            columna = columna - 1
            if columna >= 0 and columna <= 9:
                barco_aleatorio.append((fila, columna))
            else:
                barco_aleatorio.clear()
                barco_aleatorio = crear_barco_aleatorio(eslora) 

    return barco_aleatorio

#----------------------------------------------------------------------------------------------------------------------------------

def colocar_barco(barco:list, tablero, eslora:int, flota_barcos:list, funcion, tipo_usuario:str):
    ''' 
    Esta es una función que coloca los barcos en el tablero y valida si se superpone.

    Input:
        barco: list
        tablero: array
        eslora: int
        flota_barcos: list
        funcion
        tipo_usuario: str
    
    Output:
        tablero: array
    '''
    #Validamos primero si las casillas ya existen en el tablero
    for casilla in barco:
        if tablero[casilla] == '~':
            continue
        else:
            print(f'El barco, se superpone con otro barco ya creado, vuelve a intertarlo.')
            flota_barcos.remove(barco)
            nuevo_barco = funcion(eslora)
            flota_barcos.append(nuevo_barco)
            return colocar_barco(nuevo_barco, tablero, eslora, flota_barcos, funcion, tipo_usuario)
    
    #Rellenamos la casillas con los nuevos barcos
    if tipo_usuario == 'user':
        for casilla in barco:
            tablero[casilla] = 'O'
        print(barco)
        print('\n')
        print(tablero)
        print('-'*115)
        print('\n')
    else:
        for casilla in barco:
            tablero[casilla] = 'O'
    return tablero
#----------------------------------------------------------------------------------------------------------------------------------

def llenar_tablero(flota:dict, tablero, funcion, tipo_usuario):
    ''' 
    Esta es una función llena todo el tablero con la flota dada.

    Input:
        flota: dict
        tablero: array
        funcion
        tipo_usuario: str
    
    Output:
        flota_barcos: list
    '''
    flota_barcos = []
    for num, eslora in flota.items():
        for rep in range(num):
            barco = funcion(eslora)
            flota_barcos.append(barco)
            colocar_barco(barco, tablero, eslora, flota_barcos, funcion, tipo_usuario)
        
    return flota_barcos

#----------------------------------------------------------------------------------------------------------------------------------

def imprimir(tablero_user, tablero_enemigo_v):
    ''' 
    Esta es una función imprime los tableros del usuario y del enemigo.

    Input:
        tablero_user: array
        tablero_enemigo_v: array
    
    Output:
        None   
    '''
    print('\t\t\tHundir la Flota')
    print('*'*115)
    print('\n')
    print(f"{'':<3} {'User':^15} {'':<14} {'Enemigo':^30}")  
    print('-' * 23 + ' '*16 + '-' * 20)  
    columnas = "  " + " ".join(str(i) for i in range(10))
    print(" " + columnas + " " * 15 + columnas)

    for i in range(len(tablero_user)): 
        fila_usuario = f"{i:<2} " + " ".join(tablero_user[i]) 
        fila2 = " ".join(tablero_enemigo_v[i])
        print(f'{fila_usuario:<35}    {fila2:<35}')

#----------------------------------------------------------------------------------------------------------------------------------

def disparar(casilla:tuple, tablero, tablero_v, flota:list):
    ''' 
    Esta es una función que dispara en los tableros tanto para el usuario como la maquina.

    Input:
        casilla: tuple
        tablero: array
        tablero_v: array
        flota: list

    Output:
        valor: str
    '''
    try:
        tablero[casilla] in tablero

        #If de tocado tiene una validacion para saber si se ha hundido.
        if tablero[casilla] == 'O':
            valor = 'X'
            tablero[casilla] = valor
            tablero_v[casilla] = valor
            for barco in flota:
                for j in barco:
                    if j == casilla:
                        lista = []
                        for parte in barco:
                            if tablero[parte] == 'X':
                                lista.append('X')
                        for parte in barco:
                            if len(lista) == len(barco):
                                valor = 'Z'
                                tablero[parte] = valor
                                tablero_v[parte] = valor
            if tablero[casilla] == 'X':
                print('Tocado, vuelve a disparar.')
            else:            
                print('Hundido, vuelve a disparar.')

        elif tablero[casilla] == 'X':
            valor = "¡OH NO! Ya habias disparado aquí, pierdes tu turno."    

        elif tablero[casilla] == 'Z':
            valor = "¡OH NO! Ya habias disparado aquí, pierdes tu turno."

        elif tablero[casilla] == 'A':
            valor = "¡OH NO! Ya habias disparado aquí, pierdes tu turno."

        else:
            print('Agua')
            valor = 'A'
            tablero[casilla]  = valor
            tablero_v[casilla]  = valor          
    except:
        valor = "¡OH NO! Te has salido del tablero, pierdes tu turno."
    return valor

#----------------------------------------------------------------------------------------------------------------------------------

def validacion_tablero(tablero):
    ''' 
    Funcion para validar si sigue el juego o no.

    Input:
        tablero: array
    
    Output:
        bool
    '''
    for lis in tablero:
        if 'O' in lis:
            return True
    return False

#----------------------------------------------------------------------------------------------------------------------------------

def iniciar_juego(flota:dict={3:2, 2:3, 1:4}):
    ''' 
    Esta es una función para iniciar el juego donde ser crean los tablero del usuario y del enemigo.

    Input:
        flota: dict
    
    Output:
        None   
    '''
    tablero_user = crear_tablero()
    tablero_enemigo = crear_tablero()
    tablero_enemigo_v = crear_tablero()

    tipo_tablero = input('¿Que prefieres: 1-Crear tu propio tablero o 2-Que se genere de forma aleatoria? Elige entre 1 o 2. ').strip()
    if tipo_tablero == '1':
        print('Creando Tablero Usuario')
        print('*'*115)
        print('\n')
        flota_usuario = llenar_tablero(flota, tablero_user, crear_barco, 'user')
    else:
        print('Creando Tablero Usuario')
        print('*'*115)
        print('\n')
        flota_usuario = llenar_tablero(flota, tablero_user, crear_barco_aleatorio, 'user')

    print('\n')
    print('Creando Tablero Enemigo')
    print('*'*115)
    print('\n')
    flota_enemigo = llenar_tablero(flota, tablero_enemigo, crear_barco_aleatorio, 'enemigo')
    print('\n')
    time.sleep(2)
    imprimir(tablero_user, tablero_enemigo_v), 
    return tablero_user, tablero_enemigo, tablero_enemigo_v, flota_usuario, flota_enemigo

#----------------------------------------------------------------------------------------------------------------------------------

def turno_user(tablero_enemigo, tablero_enemigo_v, tablero_user, flota_enemigo:list):
    ''' 
    Funcion que genera el disparo del usuario

    Input:
        tablero_enemigo: array
        tablero_enemigo_v: array
        tablero_user: array
        flota_enemigo: list
    
    Output:
        disparo: str
    '''
    casilla_disparo = input('Es tu turno, elige una casilla para disparar ¡Vamos a por el enemigo!\nRecuerda el formato a seguir: ejemplo --> 0,1  ').strip()
    casilla =  list(casilla_disparo.split(','))
    casilla = tuple([int(x) for x in casilla])
    disparo = disparar(casilla, tablero_enemigo, tablero_enemigo_v, flota_enemigo)
    print('\n')
    print(casilla, disparo)
    print('\n')
    imprimir(tablero_user, tablero_enemigo_v)
    print('\n')
    print('-'*115)
    return disparo

#----------------------------------------------------------------------------------------------------------------------------------

def turno_enemigo(tablero_user, tablero_enemigo_v, flota_user:list):
    ''' 
    Funcion que genera el disparo del enemigo

    Input:
        tablero_user: array
        tablero_enemigo_v: array
        flota_user: list
    
    Output:
        disparo: str
    '''
    puntos = []

    for index, fila in enumerate(tablero_user):
        for j, i in enumerate(fila):
            if i == 'X':
                puntos.append((index, j))

    if len(puntos) > 0 :
        for punto in puntos:
            posibles_mov = [(punto[0], punto[1]-1), (punto[0], punto[1]+1), (punto[0]+1, punto[1]), (punto[0]-1, punto[1])]
            posibles_mov_real = []

            for i in posibles_mov:
                if (i[0] >= 0 and i[0] <= 9)  and (i[1] >= 0 and i[1] <= 9):
                    if tablero_user[i] == '~' or tablero_user[i] == 'O':
                        posibles_mov_real.append(i)
            if len(posibles_mov_real) != 0 :
                casilla = random.choice(posibles_mov_real) 

    else:
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        casilla = (fila, columna)

    disparo = disparar(casilla, tablero_user, tablero_user, flota_user)
    print('\n')
    print(casilla, disparo)
    print('\n')
    imprimir(tablero_user, tablero_enemigo_v)
    print('\n')
    print('-'*115)
    return disparo
#----------------------------------------------------------------------------------------------------------------------------------

def juego(flota:dict={3:2, 2:3, 1:4}):
    ''' 
    Función que ejecuta todo el juego en conjunto. 

    Input:
        flota:dict
    
    Output:
        None
    '''
    tablero_user, tablero_enemigo, tablero_enemigo_v, flota_usuario, flota_enemigo = iniciar_juego(flota)
    print('\n')
    print('\n')

    # print(flota_enemigo)

    # print(flota_usuario)

    while validacion_tablero(tablero_user) and validacion_tablero(tablero_enemigo):
        time.sleep(2)
        disparo = turno_user(tablero_enemigo, tablero_enemigo_v, tablero_user, flota_enemigo)
        time.sleep(2)
    
        while disparo == 'X' or disparo == 'Z':
            if not (validacion_tablero(tablero_user) and validacion_tablero(tablero_enemigo)):
                break
            else: 
                time.sleep(2)
                disparo = turno_user(tablero_enemigo, tablero_enemigo_v, tablero_user, flota_enemigo)
                time.sleep(2)
    
        if not (validacion_tablero(tablero_user) and validacion_tablero(tablero_enemigo)):
            break
    
        print('Turno de tu Enemigo!')
        print('\n')
        time.sleep(2)
        disparo = turno_enemigo(tablero_user, tablero_enemigo_v, flota_usuario)
        time.sleep(2)
        
        while disparo == 'X' or disparo == 'Z':
            if not (validacion_tablero(tablero_user) and validacion_tablero(tablero_enemigo)):
                break
            else:
                disparo = turno_enemigo(tablero_user, tablero_enemigo_v, flota_usuario)
                time.sleep(1)
    
        if not (validacion_tablero(tablero_user) and validacion_tablero(tablero_enemigo)):
            break
    
    print('Tu turno!!!')
    print('\n')

    # Evaluar el resultado final
    if validacion_tablero(tablero_user):
        print('Has ganado!\n')
        print("      *****      ")
        print("    *       *    ")
        print("   *  O   O  *   ")
        print("  *     ^     *  ")
        print("  *   \\___/   *  ")
        print("   *         *   ")
        print("    *_______*    ")
    else:
        print('Has perdido, lo siento.\n')
        print("      *****      ")
        print("    *       *    ")
        print("   *  O   O  *   ")
        print("  *     ^     *  ")
        print("  *   /___\\   *  ")
        print("   *         *   ")
        print("    *_______*    ")
    print('\n')
    jugar_de_nuevo = input('¿Quieres jugar de nuevo S/N? ')
    if jugar_de_nuevo.upper().strip() == 'S':
        print('\n')
        juego(flota)    
##########################################
#####              MAIN              #####
##########################################

import utils as u
import time

print(
'¡Bienvenido a Hundir la Flota! \n\nPrepárate para una emocionante batalla naval donde la estrategia y la puntería serán clave para la victoria.\nEn este juego, tendrás que localizar y hundir la flota enemiga antes de que tu oponente hunda la tuya. \nReglas del juego: \n\n- Cada jugador tiene una cuadrícula (10X10) donde coloca sus barcos (6) en posiciones estratégicas. \n- Los barcos pueden ocupar varias casillas y pueden estar dispuestos horizontal o verticalmente.\n- En cada turno, podrás disparar a una coordenada de la cuadrícula enemiga.\n- Si aciertas en una casilla ocupada por un barco enemigo, será un ¡Tocado!. Si fallas, será agua.\n- Gana el jugador que logre hundir todos los barcos del oponente primero.\n\n¿Listo para la batalla?\n\n')


print("        |    |    |        ")
print("       )_)  )_)  )_)       ")
print("      )___))___))___)\\    ")
print("     )____)____)_____)\\   ")
print("   _____|____|____|____\\__ ")
print("   \\                   /   ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print('Iniciemos!!')
print('\n')
time.sleep(2)

flota = {2:3}

u.juego(flota)


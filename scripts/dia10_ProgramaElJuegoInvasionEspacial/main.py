import pygame
import random
import math

from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear y establecer tamaño de pantalla. Se inidica en píxeles dentro de una tupla
screen = pygame.display.set_mode((800, 600))

# Añadir música de fondo
mixer.music.load('resources/dia10_ProgramaElJuegoInvasionEspacial/MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Personalizar pantalla. Cambiar título de la pantalla
pygame.display.set_caption('Invasión espacial')

# Cambiar icono de la pantalla
icono = pygame.image.load('resources/dia10_ProgramaElJuegoInvasionEspacial/ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('resources/dia10_ProgramaElJuegoInvasionEspacial/fondo.jpg')

# Crear jugador. Para colocarlo se resta el tamaño del icono
img_jugador = pygame.image.load('resources/dia10_ProgramaElJuegoInvasionEspacial/cohete.png')

# Posición inicial del jugador
posicion_jugador_x = 368
posicion_jugador_y = 500
posicion_cambio_jugador_x = 0
posicion_cambio_jugador_y = 0

# Crear imagen enemigo
img_enemigo = []
# Se define posicion aleatoria para el enemigo
posicion_enemigo_x = []
posicion_enemigo_y = []
posicion_cambio_enemigo_x = []
posicion_cambio_enemigo_y = []
cantidad_enemigos = 8

# Crear varios enemigos
for e in range(cantidad_enemigos): 
    img_enemigo.append(pygame.image.load('resources/dia10_ProgramaElJuegoInvasionEspacial/enemigo.png'))
    posicion_enemigo_x.append(random.randint(0, 736))
    posicion_enemigo_y.append(random.randint(50, 200))
    posicion_cambio_enemigo_x.append(0.5)
    posicion_cambio_enemigo_y.append(50)

# Crear bala
img_bala = pygame.image.load('resources/dia10_ProgramaElJuegoInvasionEspacial/bala.png')

# Se define posicion aleatoria para la bala
posicion_bala_x = 0
posicion_bala_y = 500
posicion_cambio_bala_x = 0
posicion_cambio_bala_y = 1
visibilidad_bala = False

# Construir posicion del jugador. Se le añaden parámetros para poder mover al jugador
def posicionar_jugador_pantalla(movimiento_x, movimiento_y):
    screen.blit(img_jugador, (movimiento_x, movimiento_y))

# Construir posicion del enemigo. 
def posicionar_enemigo_pantalla(movimiento_x, movimiento_y, enemigo):
    screen.blit(img_enemigo[enemigo], (movimiento_x, movimiento_y))

# Construir disparar bala
def disparar_bala(posicion_x, posicion_y): 
    global visibilidad_bala
    visibilidad_bala = True
    screen.blit(img_bala, (posicion_x + 16, posicion_y + 10))
    
# Puntuje:
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32) # Se indica la fuente y el tamaño que vienen incluídas en pygame
posicion_puntaje_x = 10 
posicion_puntaje_y = 10 

# Funcion para mostrar puntaje
def mostrar_puntaje(x, y): 
    texto = fuente.render(f'Puntos: {puntaje}', True, (255, 255, 255)) # Imprimir por pantalla el texto del puntaje
    screen.blit(texto, (posicion_puntaje_x, posicion_puntaje_y))
    
# Detectar colisiones
def existe_colision(x1, y1, x2, y2): 
    distancia = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    if distancia < 27:
        return True
    else: 
        return False

# Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40) 
def texto_final(): 
    texto = fuente_final.render('GAME OVERE', True, (255, 255, 255))
    screen.blit(texto, (60, 200)) # Posición al centro de la pantalla

# Loop del juego
# Eventos: Cualquier acción con la pantalla 
ejecucion = True
while ejecucion:
    
    # Cambiar fondo de pantalla
    screen.blit(fondo, ((0, 0)))   
    # Evento quit: cerrar la ventana
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            ejecucion = False
        
        # Valor X negativo se mueve hacia la izquierda. Valor X positivo se mueve hacia la derecha
        # posicion_jugador_x -= 0.1
        # Valor Y negativo moviemiento hacia arriba. Valor Y positivo movimiento hacia abajo
        # posicion_jugador_y -= 0.1
        # Controlar movimiento por la pantalla. Programar evento en el que el jugador presiona una letra
        # KEYDOWN: Verifica si la tecla ha sido presionada
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('El jugador mueve hacia la izquierda ... ')
                posicion_cambio_jugador_x = -0.3
            if event.key == pygame.K_RIGHT:
                print('El jugador mueve hacia la derecha ... ')
                posicion_cambio_jugador_x = 0.3
            if event.key == pygame.K_SPACE:
                if visibilidad_bala == False: 
                    # Reproducir el sonido del disparo
                    sonido_bala = mixer.Sound('resources/dia10_ProgramaElJuegoInvasionEspacial/bala.png')
                    sonido_bala.play()
                    print('El jugador dispara ... ')
                    posicion_bala_x = posicion_jugador_x
                    disparar_bala(posicion_bala_x, posicion_bala_y)
                    
        # KEYUP: Verifica si la tecla ha sido soltada
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('El jugador se detiene ... ')
                posicion_cambio_jugador_x = 0
                
    # Actualizar la posición del jugador
    posicion_jugador_x += posicion_cambio_jugador_x
    
    # Movimiento jugador. Limitar pantalla
    if posicion_jugador_x <= 0:
        posicion_jugador_x = 0
    elif posicion_jugador_x >= 736: 
        posicion_jugador_x = 736
        
    # Actualizar la posicion del enemigo
    for e in range(cantidad_enemigos):
        if posicion_enemigo_y[e] > 500: 
            for k in range(cantidad_enemigos):
                posicion_enemigo_y[k] = 1000
            texto_final()
            break 
        posicion_enemigo_x[e] += posicion_cambio_enemigo_x[e]
        # Movimiento enemigo. Limitar pantalla
        if posicion_enemigo_x[e] <= 0:
            posicion_cambio_enemigo_x[e] = 1
            posicion_enemigo_y[e] += posicion_cambio_enemigo_y[e]
        elif posicion_enemigo_x[e] >= 736: 
            posicion_cambio_enemigo_x = -1
            posicion_enemigo_y[e] += posicion_cambio_enemigo_y[e]
        # Colision
        colision = existe_colision(posicion_enemigo_x[e], posicion_enemigo_y[e], posicion_bala_x, posicion_bala_y)
        if colision: 
            sonido_colision = mixer.Sound('resources/dia10_ProgramaElJuegoInvasionEspacial/Golpe.mp3')
            sonido_colision.play()
            posicion_bala_y = 500
            visibilidad_bala = False
            puntaje += 1
            posicion_enemigo_x[e] = random.randint(0, 736)
            posicion_enemigo_y[e] = random.randint(50, 200)
        
        posicionar_enemigo_pantalla(posicion_enemigo_x[e], posicion_enemigo_y[e], e)
        
    # Movimiento bala
    if posicion_bala_y <= -64:
        posicion_bala_y = 500
        visibilidad_bala = False
    if visibilidad_bala: 
        disparar_bala(posicion_bala_x, posicion_bala_y)
        posicion_bala_y -= posicion_cambio_bala_y

    posicionar_jugador_pantalla(posicion_jugador_x, posicion_jugador_y)
    
    # Mostrar puntaje en la pantalla
    mostrar_puntaje(posicion_puntaje_x, posicion_puntaje_y)
    
    # Actualizar pantalla
    pygame.display.update()
            


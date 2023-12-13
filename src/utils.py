import subprocess

import os

# Configura la variable de entorno para no mostrar mensaje en la pantalla
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '0'  

import pygame
import time


def reproducir_sonido(ruta_sonido, volumen, bucle=False):


    # Cargo el modulo de pygame y los recursos
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_sonido)

    if bucle: 
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()

    pygame.mixer.music.set_volume(volumen)

    # Esperar hasta que la música termine de reproducirse
    while pygame.mixer.music.get_busy():
        time.sleep(1)


#--------------------------

title = "ML!"
mensaje= 'Optimización de hiperparametros lista!'


ruta_icono = "/home/tr4shhh/Desktop/Proyects/Icons/appimagekit-Play.svg"
ruta_sonido = "/home/tr4shhh/Desktop/Proyects/assets/notificaciones_sounds/Alarms/(LG) Tick_Tock.ogg"

def sendmessage(titulo=title, message=mensaje, volumen=1, sonido=ruta_sonido,icono_path=ruta_icono):
    
    # Muestra la notificacion en pantalla
    subprocess.Popen(['notify-send',titulo, message,'-i', icono_path])

    # Hace un sonido de advertencia
    reproducir_sonido(sonido,volumen)

    return




# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:58:35 2021

@author: JAB
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

archivo = 'prueba.wav'
muestreo, sonido = waves.read(archivo)
print('frecuencia de muestreo: ', muestreo)
print('dimensiones de matriz: ', np.shape(sonido))
print('datos de sonido: ')
print(sonido)
# Toda la señal
# inicia = 1000
# termina = 8050

# inicia = 29500
# termina = 39800

# inicia = 56100
# termina = 65100

inicia = 81500
termina = 92500


# Extraer el tiempo de muestreo
dt = 1/muestreo
# Construir el intervalo de tiempo cada dt muestras
t = np.arange(inicia*dt,termina*dt,dt)
# Verificar la cantidad de muestras
muestras = len(t)
# Señal en dos canales, elegir uno
canal = 0
fragmento = sonido[inicia:inicia+muestras, canal]

# Gráfica analógica de sonido
plt.plot(t,fragmento)
plt.xlabel('t segundos')
plt.ylabel('sonido(t)')
plt.show()
# Gráfica discreta de sonido
n = np.arange(inicia,inicia+muestras,1)
plt.stem(n,fragmento)
plt.xlabel('n')
plt.ylabel('sonido[n]')
plt.show()
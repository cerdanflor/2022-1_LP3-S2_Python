# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:43:36 2022

@author: UPEU
"""

archivo=open("archivo de prueba.txt","wt")
contenido ="Linea1 hola amigos como están\nLínea2 Bienvenido a la UNTELS."
archivo.write(contenido)
archivo.close()
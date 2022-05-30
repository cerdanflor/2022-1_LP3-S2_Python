# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:03:14 2022

@author: UPEU
"""
# Importamos la librería 

import camelcase

nombre = "flor elizabeth cerdan león"
print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con camelcase.....")

# Imprimimos el nombre en formato título
# Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluímos los argumentos
# 'flor' y 'león'

cam2=camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))
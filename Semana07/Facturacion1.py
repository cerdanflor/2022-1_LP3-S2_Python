# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:16:40 2022

@author: UPEU
"""
# Dado el subtotal, calcular el IGV y el total
import financieros
subtotal=800
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")





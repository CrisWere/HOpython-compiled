import ctypes as C
import numpy as np


CLIB = C.CDLL('./libmymath.so') #Cargo la libreria dinamica

#Pruebo las distintas funciones de los archivos add_two y arrays que se encuentran en la libreria libmymath.so
print '\n'
#---------------------------------------------------------------------------------------------
print('   PRUEBA DE FUNCIONES DE add_two.c')
#---------------------------------------------------------------------------------------------

# float add_float(float a, float b);
#Defino el tipo de los argumentos y el valor de retorno de la fcion
CLIB.add_float.argtypes = (C.c_float, C.c_float)
CLIB.add_float.restype = C.c_float
#Invoco a la fcion e imprimo el resultado
datoA = 3.0
datoB = 5.0
res = CLIB.add_float(datoA, datoB)
print '\n      - add_float(%s, %s) --> return ' %(datoA, datoB), res

#---------------------------------------------------------------------------------------------

# int add_int(int a, int b);
#Defino el tipo de los argumentos y el valor de retorno de la fcion
CLIB.add_int.argtypes = (C.c_int, C.c_int)
CLIB.add_int.restype = C.c_int
#Invoco a la fcion e imprimo el resultado
datoA = 15
datoB = 10
res=CLIB.add_int(datoA, datoB)
print '\n      - add_int(%s, %s) --> return ' %(datoA, datoB), res

#---------------------------------------------------------------------------------------------

# int add_float_ref(float *a, float *b, float *c);
#Defino el tipo de los argumentos y el valor de retorno de la fcion
CLIB.add_float_ref.argtypes = (C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float))
CLIB.add_float_ref.restype = C.c_int
#Inicializo las variables 
#datoA = C.c_float(12.5)
datoA = 12.5
datoB = 21
res = C.c_float(0)
#Invoco a la fcion e imprimo el resultado
CLIB.add_float_ref(C.byref(C.c_float(datoA)), C.byref(C.c_float(datoB)), C.byref(res))
print '\n      - add_float_ref(%s, %s, %s) --> res = ' %(datoA, datoB, 'res'), res.value

#---------------------------------------------------------------------------------------------

# int add_int_ref(int *a, int *b, int *c);
#Defino el tipo de los argumentos y el valor de retorno de la fcion
CLIB.add_int_ref.argtypes = (C.POINTER(C.c_int), C.POINTER(C.c_int), C.POINTER(C.c_int))
CLIB.add_int_ref.restype = C.c_int
#Inicializo las variables 
datoA = 6
datoB = 8
res = C.c_int(0)
#Invoco a la fcion e imprimo el resultado
CLIB.add_int_ref(C.byref( C.c_int(datoA)), C.byref(C.c_int(datoB)), C.byref(res))
print '\n      - add_int_ref(%s, %s, %s) --> res = ' %(datoA, datoB, 'res'), res.value
print '\n'

#---------------------------------------------------------------------------------------------
print('   PRUEBA DE FUNCIONES DE arrays.c')
#---------------------------------------------------------------------------------------------

# int add_int_array(int *a, int *b, int *c, int n);
#Defino el valor de retorno de la fcion
CLIB.add_int_array.restype = C.c_int
#Inicializo los arreglos y el valor de tama
tama = 5
#arreglo1 = (C.c_int * tama)(1, 2,-3, 4,-5)
arreglo1 = (C.c_int * tama)(1, 2, 3, 4, 5)
arreglo2 = (C.c_int * tama)(0, 4, 2,-2, 1)
arreglo3 = (C.c_int * tama)(0, 0, 0, 0, 0)
#Invoco a la fcion e imprimo el resultado
print '\n      arreglo1 = ', [x for x in arreglo1]
print '      arreglo2 = ', [x for x in arreglo2]

CLIB.add_int_array(C.byref(arreglo1), C.byref(arreglo2), C.byref(arreglo3), C.c_int(tama))
print '\n      - add_int_ref(arre1, arre2, arre3, tama) --> arre3 = ', [x for x in arreglo3]

#---------------------------------------------------------------------------------------------

# float dot_product(float *a, float *b, int n);
#Defino el valor de retorno de la fcion
CLIB.dot_product.restype = C.c_float
#Inicializo los arreglos y el valor de tama
tama = 5
#arreglo1 = (C.c_int * tama)(1, 2,-3, 4,-5)
arreglo1 = (C.c_float * tama)(1, 2, 3, 4, 5)
arreglo2 = (C.c_float * tama)(0, 4, 2,-2, 1)
#Invoco a la fcion e imprimo el resultado
res = CLIB.dot_product(C.byref(arreglo1), C.byref(arreglo2), C.c_int(tama))
print '\n      - dot_product(arre1, arre2, tama) --> res = ', res

#---------------------------------------------------------------------------------------------
print '\n      Otra forma de trabajar arreglos con numpy'
# float dot_product(float *a, float *b, int n);
#Defino  el valor de retorno de la fcion
CLIB.dot_product.restype = C.c_float
flp = C.POINTER(C.c_float)
#Inicializo los arreglos y el valor de tama
tama = 5
#arreglo1 = (C.c_int * tama)(1, 2,-3, 4,-5)
arreglo1 = np.array([1, 2, 3, 4, 5], dtype=C.c_float)
arreglo2 = np.array([0, 4, 2,-2, 1], dtype=C.c_float)
#Invoco a la fcion e imprimo el resultado
res = CLIB.dot_product(arreglo1.ctypes.data_as(flp), arreglo2.ctypes.data_as(flp), C.c_int(tama))
print '      - dot_product(arre1, arre2, tama) --> res = ', res
print '\n'

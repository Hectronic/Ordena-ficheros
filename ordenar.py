#Version 0.2 alpha
#I haven't decide the license for this code, so temporally all rigths reserved. 

import os
import shutil
import sys

tipos = {}
desconocidos = []

    

def ordenar(extension, fichero):
    if(extension in tipos):
        tipo = tipos[extension]
        if(tipo != 'Unknow'):
            createDir(tipos[extension])
            shutil.move(fichero, os.getcwd())      
    else:
        if (extension not in desconocidos):  
            desconocidos.append(extension)

def createDir(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)   
    
def cargarTipos():
    ficheroTipos = open('tipos.txt')
    for linea in ficheroTipos.readlines():
        trozos = linea.split("-")
        tipos[trozos[0]] = (trozos[1])[0:-1]#Quita el \n
    ficheroTipos.close() 

def recorrerFicheros(dir):
    ficheros = os.listdir(dir)
    for i in range(len(ficheros)):
        fichero = dir + "/" + ficheros[i]
        print fichero
        print sys.argv[0]
        if(fichero != sys.argv[0]):
            ini = fichero.rfind('.')
            fin = len(fichero)
            if(ini != -1):
                extension = fichero[ini:fin]
                ordenar(extension, fichero)
                os.chdir(dir)   


def main():
    
    cargarTipos() 
    dir = os.getcwd()
    recorrerFicheros(dir)
    ficheroTipos = open('tipos.txt', 'a')
    for extension in desconocidos:
        print extension
        ficheroTipos.write(extension + '-' + 'Unknow\n')
    ficheroTipos.close()

main()
            
 

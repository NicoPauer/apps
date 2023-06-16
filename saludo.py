#!/usr/bin/python3
'''
   Autor: Nicolas Pauer, 15 de junio de 2023
   Mail: nicolaspauer20@gmail.com
   
	Ejemplo básico con
	una ventana que muestra un
	saludo en español e ingles.
'''
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


# Algortimos y declaraciones imortantes
saludos = {'es':'<h1 style = "color: red;">Hola, me alegra verte.</h1>', 'en':'<h1 style = "color: blue;">Hello, I happy up see you.</h1>'}
# Programa pincipal
if __name__ == '__main__':
    # Creo estructura de app grafica Qt	
		app = QApplication(sys.argv)
    # Agrego elementos graficos	
    # Ventana de 720px de ancho por 500px de alto con titulo 'Greetings'	
		ventana = QWidget()
		ventana.setWindowTitle('Greetings')
		ventana.resize(720, 500)
    # Agrego etiquetas con saludos
        
		saludo_hispano = QLabel()
		saludo_hispano.setText(saludos['es'])
        
		saludo_anglo = QLabel()
		saludo_anglo.setText(saludos['en'])
        
    # Creo contenedor para las etiquetas
		contenedor = QVBoxLayout()
    # Agrego etiquetas al contenedor, primero el universal ingles y luego el nativo español
		contenedor.addWidget(saludo_anglo)
		contenedor.addWidget(saludo_hispano)
    # Agrego contenedor a la ventana
		ventana.setLayout(contenedor)
    # Muestro ventana ya que tengo todos los elementos
		ventana.show()
    # Cierro aplicacion para que no se trave cuando se cierre la ventana
		sys.exit(app.exec_())

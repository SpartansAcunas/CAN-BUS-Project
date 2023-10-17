import serial
import time
import subprocess



archivo = open('C:\\Users\\Alfredo\\Desktop\\PCB\\DATA.txt', 'w')
serialArduino = serial.Serial("COM7", 9600)
time.sleep(1)

contador = 0  # Inicializar el contador
while True:
    data = serialArduino.readline().decode().strip()
    if "CAN Receiver" in data:
        break

while contador < 60:  # Continuar leyendo hasta que el contador alcance 59
    linea = serialArduino.readline().decode('ascii')
    #print(linea)
    archivo.write(linea)

    contador += 1  # Incrementar el contador

# Cerrar el archivo y detener la transmisión
archivo.close()
serialArduino.close()

subprocess.call(['python', 'C:\\Users\\Alfredo\\Desktop\\PCB\\Visualizador.py'])

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Crear el arreglo vacío
data = np.empty((0, 11), dtype=object)

fig, ax = plt.subplots(figsize=(18, 9))

# Abrir el archivo de texto
with open('C:\\Users\\Alfredo\\Desktop\\PCB\\DATA.txt', 'r') as f:
    # Leer todas las líneas
    lines = f.readlines()
    # Recorrer las líneas del archivo
    for line in lines:
        # Verificar si la línea contiene el ID 0x316
        if 'packet with id 0x316' in line:
            palabras = line.split()
            valores_hex = [palabras[2], palabras[4], palabras[6], palabras[8], palabras[10], palabras[12], palabras[14], palabras[16]]
            hex_string = ' '.join(valores_hex)
            id = '0x316'
            length = line.split('and length')[1].strip().split()[0]
            row = np.array([id, hex_string, length, 'NaN' , 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'], dtype=object)
            data = np.vstack((data, row))

        # Verificar si la línea contiene el ID 0x329
        elif 'packet with id 0x329' in line:
            palabras = line.split()
            valores_hex = [palabras[2], palabras[4], palabras[6], palabras[8], palabras[10], palabras[12], palabras[14], palabras[16]]
            hex_string = ' '.join(valores_hex)
            id = '0x329'
            length = line.split('and length')[1].strip().split()[0]
            OBDACKSTND = palabras[2]
            TEMENG = palabras[4]
            MAF = palabras[6]
            CONFIG = palabras[8]
            BRAKEACT = palabras[10]
            TPS = palabras[12]
            PVAVCAN = palabras[14]
            ENGVOLT = palabras[16]
            row = np.array([id, hex_string, length, OBDACKSTND, TEMENG, MAF, CONFIG, BRAKEACT, TPS, PVAVCAN, ENGVOLT], dtype=object)
            data = np.vstack((data, row))

        else:
            if 'CAN Receiver' in line:
                plt.title('CAN Receiver')
            elif 'CAN bus with ECU/EMS started successfully!' in line:
                plt.suptitle('CAN bus with the ECU/EMS started successfully!')
            else:
                continue

# Crear la tabla
headers = ['ID', 'Data', 'Length', 'OBD_standard', 'TempRefrigerante', 'Aire', 'Configuraciones', 'Frenado', 'TPS', 'PV_AV_CAN', 'Tension Bat']
#table_data = [headers] + data.tolist()
table_data = [headers] + data[0:].tolist()  # Excluir la segunda fila
tabla = ax.table(cellText=table_data, loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(7)
tabla.scale(1, 2)
print(table_data)
ax.axis('off')
plt.tight_layout()
plt.show()

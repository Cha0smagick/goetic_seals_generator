import matplotlib.pyplot as plt
import numpy as np

# Definir las medidas del sello y la geometría sagrada
radius_outer = 1.0
radius_inner = 0.6
circle_center = (0.0, 0.0)

# Crear un arreglo de ángulos para dibujar la circunferencia
theta = np.linspace(0, 2 * np.pi, 100)

# Calcular las coordenadas de los puntos en la circunferencia exterior e interior
x_outer = circle_center[0] + radius_outer * np.cos(theta)
y_outer = circle_center[1] + radius_outer * np.sin(theta)

x_inner = circle_center[0] + radius_inner * np.cos(theta)
y_inner = circle_center[1] + radius_inner * np.sin(theta)

# Crear una figura y dibujar los elementos
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar el relleno entre los círculos
ax.fill_between(theta, radius_inner, radius_outer, color='white')

# Pedir al usuario un nombre
name = input("Ingrese su nombre: ")

# Transformar el nombre a caracteres hebreos
name_hebrew = ""
hebrew_conversion = {
    'A': 'א',
    'B': 'ב',
    'C': 'ג',
    'D': 'ד',
    'E': 'ה',
    'F': 'ו',
    'G': 'ז',
    'H': 'ח',
    'I': 'ט',
    'J': 'י',
    'K': 'כ',
    'L': 'ל',
    'M': 'מ',
    'N': 'נ',
    'O': 'ס',
    'P': 'ע',
    'Q': 'פ',
    'R': 'צ',
    'S': 'ק',
    'T': 'ר',
    'U': 'ש',
    'V': 'ת',
    'W': 'ך',
    'X': 'ם',
    'Y': 'ן',
    'Z': 'ף',
}

for char in name:
    char_upper = char.upper()
    if char_upper in hebrew_conversion:
        name_hebrew += hebrew_conversion[char_upper]
    else:
        name_hebrew += char

# Agregar el nombre en hebreo
angle = np.linspace(0, 2 * np.pi, len(name_hebrew), endpoint=False)
for char, ang in zip(name_hebrew, angle):
    x = circle_center[0] + (radius_inner + (radius_outer - radius_inner) / 2) * np.cos(ang)
    y = circle_center[1] + (radius_inner + (radius_outer - radius_inner) / 2) * np.sin(ang)
    ax.text(x, y, char, fontsize=48, ha='center', va='center', rotation=ang * 180 / np.pi + 90)

# Dibujar las circunferencias exterior e interior
ax.plot(x_outer, y_outer, color='black')
ax.plot(x_inner, y_inner, color='black')

# Dibujar el octágono dentro del círculo interno
octagon_points = []
num_sides = 8
angle_step = 2 * np.pi / num_sides
for i in range(num_sides):
    angle = i * angle_step
    x = circle_center[0] + radius_inner * np.cos(angle)
    y = circle_center[1] + radius_inner * np.sin(angle)
    octagon_points.append((x, y))
    ax.plot([x, circle_center[0]], [y, circle_center[1]], color='black')  # Conectar con líneas al centro

# Conectar todas las puntas del octágono con líneas
for i in range(num_sides):
    x1, y1 = octagon_points[i]
    for j in range(i + 1, num_sides):
        x2, y2 = octagon_points[j]
        ax.plot([x1, x2], [y1, y2], color='black')

# Ajustar los límites de los ejes para que el sello sea visible correctamente
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Eliminar los ejes y etiquetas para obtener un diseño limpio
ax.axis('off')

# Mostrar el sello en la ventana de visualización
plt.show()

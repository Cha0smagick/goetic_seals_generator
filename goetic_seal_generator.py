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

# Transformar el nombre a caracteres hebreos y obtener los valores numéricos cabalísticos
name_hebrew = ""
numerical_values = []
hebrew_conversion = {
    'A': ('א', 1),
    'B': ('ב', 2),
    'C': ('ג', 3),
    'D': ('ד', 4),
    'E': ('ה', 5),
    'F': ('ו', 6),
    'G': ('ז', 7),
    'H': ('ח', 8),
    'I': ('ט', 9),
    'J': ('י', 10),
    'K': ('כ', 20),
    'L': ('ל', 30),
    'M': ('מ', 40),
    'N': ('נ', 50),
    'O': ('ס', 60),
    'P': ('ע', 70),
    'Q': ('פ', 80),
    'R': ('צ', 90),
    'S': ('ק', 100),
    'T': ('ר', 200),
    'U': ('ש', 300),
    'V': ('ת', 400),
    'W': ('ך', 500),
    'X': ('ם', 600),
    'Y': ('ן', 700),
    'Z': ('ף', 800),
}

for char in name:
    char_upper = char.upper()
    if char_upper in hebrew_conversion:
        hebrew_char, value = hebrew_conversion[char_upper]
        name_hebrew += hebrew_char
        numerical_values.append(value)
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

# Generar una figura aleatoria en el centro del círculo interno
figure_points = []
num_sides = len(numerical_values)
angle_step = 2 * np.pi / num_sides
random_angles = np.random.rand(num_sides) * 2 * np.pi
polygon_angles = []  # Almacenar los ángulos generados para el polígono

for i, angle in enumerate(random_angles):
    value = numerical_values[i % len(numerical_values)]
    max_radius = radius_inner * value / 100
    if max_radius > radius_inner:
        max_radius = radius_inner
    x = circle_center[0] + max_radius * np.cos(angle)
    y = circle_center[1] + max_radius * np.sin(angle)
    figure_points.append((x, y))
    ax.plot([x, circle_center[0]], [y, circle_center[1]], color='white')  # Conectar con líneas al centro
    polygon_angles.append(angle)  # Almacenar el ángulo generado

# Conectar todas las puntas de la figura aleatoria con líneas
for i in range(num_sides):
    x1, y1 = figure_points[i]
    for j in range(i + 1, num_sides):
        x2, y2 = figure_points[j]
        ax.plot([x1, x2], [y1, y2], color='white')

# Crear el polígono con los ángulos generados
polygon_points = []
for angle in polygon_angles:
    x = circle_center[0] + radius_inner * np.cos(angle)
    y = circle_center[1] + radius_inner * np.sin(angle)
    polygon_points.append((x, y))

# Conectar todas las puntas del polígono con líneas
for i in range(num_sides):
    x1, y1 = polygon_points[i]
    x2, y2 = polygon_points[(i + 1) % num_sides]
    ax.plot([x1, x2], [y1, y2], color='black')

# Ajustar los límites de los ejes para que el sello sea visible correctamente
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Eliminar los ejes y etiquetas para obtener un diseño limpio
ax.axis('off')

# Mostrar el sello en la ventana de visualización
plt.show()

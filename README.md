### Opción 1: Formato Markdown (Copiar y Pegar)

```markdown
# Instrucciones de Ejecución y Simulación

Sigue estos pasos para compilar el entorno y ejecutar la simulación de navegación autónoma.

## 🛠️ Instalación y Compilación

**1. Clonar el repositorio**
```bash
git clone <https://github.com/jerimore/Nav_Autonoma_RobotDiferencial_RAMMEL.git>

```

**2. Acceder al directorio de trabajo**

```bash
cd ~/Nav_Autonoma_RobotDiferencial_RAMMEL/
```
**3. Construir el paquete**
Utilizamos `colcon` con la opción de enlaces simbólicos para reflejar cambios en Python sin recompensar:

```bash
colcon build --symlink-install

```

**4. Configurar el entorno (Source)**

```bash
source install/setup.bash

```

---

## 🚀 Ejecución de la Simulación

**5. Lanzar el entorno de navegación**
Ejecuta el siguiente comando para iniciar Gazebo ("Mundo Prueba") y RViz con la configuración de Nav2:

```bash
ros2 launch nav_bot navigation.launch.py

```

<img width="810" height="586" alt="Lanzamiento de simulación" src="https://github.com/user-attachments/assets/02861c3c-86b1-4350-99c8-f3214b660490" />

### Inicialización del Robot

**6. Estimación de la Pose Inicial (2D Pose Estimate)**
Una vez abiertos RViz y Gazebo, es crucial sincronizar la posición del robot.

* **Nota:** Asegúrate de que el mapa en RViz y el mundo en Gazebo tengan la misma orientación.
* Utiliza la herramienta **2D Pose Estimate** en RViz para indicar dónde está el robot y hacia dónde mira.

**Herramienta 2D Pose Estimate:**
<img width="1920" height="1080" alt="Herramienta 2D Pose Estimate" src="https://github.com/user-attachments/assets/0501ab76-b5ab-4659-8706-e78f2c864154" />

**Vista del Mundo en Gazebo:**
<img width="1920" height="1080" alt="Mundo Gazebo" src="https://github.com/user-attachments/assets/0df58dab-c910-4f31-9818-447e6ab2ccd6" />

**Verificación de Estado:**
Confirma que no existan errores en el panel izquierdo de RViz (*Displays*) ni en el estado de Nav2.
<img width="1271" height="1017" alt="Estado RViz" src="https://github.com/user-attachments/assets/049d5c02-c18e-4e68-9ce0-1e4eb29efe54" />

---

## 🎮 Modos de Operación

Tienes tres opciones para controlar el robot:

1. **Teleoperación:** Usando el paquete `teleop_twist_keyboard`.
2. **Navegación por GUI:** Usando *Nav2 Goal*.
3. **Navegación por Script:** Ejecutando una misión automática en Python.

### Opción A: Navegación mediante RViz (Nav2 Goal)

Utiliza la herramienta **Nav2 Goal** en la barra superior de RViz para establecer un objetivo en el mapa.

**Ejemplo de uso:**
<img width="1271" height="1017" alt="Nav2 Goal Ejemplo" src="https://github.com/user-attachments/assets/144b6b1a-8d63-4105-aae7-fb5eea856823" />

**Resultado esperado:**
El robot planificará la ruta y se orientará hacia el punto indicado por la flecha.
<img width="1271" height="1017" alt="Resultado Nav2" src="https://github.com/user-attachments/assets/fa502e62-5932-4ef6-8195-6815ee2bd005" />

### Opción B: Ejecutar Script de Navegación Autónoma

Este script envía al robot a una secuencia de puntos predefinidos (Punto A -> Espera 3s -> Punto B).

1. Abre una **nueva terminal**.
2. Navega a la carpeta del repositorio.
3. Configura el entorno nuevamente:
```bash
source install/setup.bash

```


4. Ejecuta el script de misión:
```bash
python3 mision_autonoma.py

```



<img width="817" height="582" alt="Ejecución Script" src="https://github.com/user-attachments/assets/eba0d24b-d17a-4f26-b8b6-41efb4fbe704" />

**Resultado de la misión:**
Verás en la consola el progreso del desplazamiento. En la simulación, el robot navegará automáticamente al Punto A, esperará 3 segundos y continuará hacia el Punto B.

<img width="1835" height="856" alt="Resultado Script" src="https://github.com/user-attachments/assets/cae7fd7d-325c-4b4c-ad7d-4a4c86277163" />

```

-----

### Cambios principales realizados:

1.  **Bloques de Código:** Puse todos los comandos dentro de bloques \`\`\`bash ... \`\`\`. Esto hace que se vean como código real en GitHub y añade un botón automático de "copiar" para el usuario.
2.  **Jerarquía:** Usé títulos (`##`) y negritas para separar claramente la fase de **Instalación** de la de **Ejecución**.
3.  **Claridad en "Source":** Cambié "hacer referencia source" por "Configurar el entorno", que es más estándar, aunque mantuve el comando `source`.
4.  **Flujo lógico:** Agrupé la verificación de errores y la inicialización (`2D Pose Estimate`) antes de presentar las opciones de movimiento, ya que son prerrequisitos para cualquiera de las opciones.

```

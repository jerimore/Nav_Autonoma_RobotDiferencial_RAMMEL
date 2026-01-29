# 🤖 NavBot: Navegación Autónoma con ROS 2 Jazzy y Gazebo Harmonic

![ROS 2](https://img.shields.io/badge/ROS_2-Jazzy-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-FF6F00?style=for-the-badge&logo=gazebo&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

Este proyecto implementa una simulación completa de un robot móvil de tracción diferencial. Integra **SLAM** (Simultaneous Localization and Mapping) para la generación de mapas y el stack **Nav2** para la navegación autónoma, evasión de obstáculos y planificación de rutas.

## ✨ Características Principales
* **Simulación Física Realista:** Robot modelado en URDF/Xacro con propiedades inerciales y físicas.
* **Sensores Simulados:** Lidar 2D (Ray Sensor) y Odometría precisa mediante plugin `DiffDrive`.
* **Mapeo:** Generación de mapas de ocupación estáticos usando `slam_toolbox` en modo asíncrono.
* **Navegación Inteligente:** Uso de Nav2 para ir de un Punto A a un Punto B esquivando obstáculos estáticos y dinámicos.
## 🛠 Prerrequisitos
Asegúrate de tener instalado lo siguiente en Ubuntu 24.04:

* **ROS 2 Jazzy Jalisco**
* **Gazebo Harmonic**
* **Paquetes de Navegación y Simulación:**
  ```bash
  sudo apt update
  sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox ros-jazzy-ros-gz-sim \
  ros-jazzy-teleop-twist-keyboard ros-jazzy-xacro \
  ros-jazzy-nav2-simple-commander

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

🔧 Errores Comunes
Error: "No map received" en RViz

Causa 1: Política de QoS incorrecta.

Solución: En RViz, ve a las propiedades del Tópico Map y cambia Durability Policy a Transient Local.

Causa 2: En caso de haber ejecutado la simulacion con un nuevo mapa, asegurarse de realizar una Sesión de Mapeo (SLAM).
Solucion 2: ¡Exacto! Ese es el "eslabón perdido". Si acabas de crear el mundo (`mi_mundo.sdf`), **Nav2 no puede funcionar todavía** porque no tiene el mapa (`.yaml` y `.pgm`) de ese lugar nuevo.

El error "No map received" es lógico: Nav2 está buscando un archivo que aún no existe.

Vamos a crearlo ahora mismo. Olvida el archivo `navigation.launch.py` por un momento. Tienes que hacer una **Sesión de Mapeo** (SLAM).

Sigue estos 4 pasos para generar el YAML:

### Paso 1: Abre tu Nuevo Mundo

Lanza la simulación asegurándote de que cargue tu archivo `.sdf` nuevo:
```bash
# Terminal 1
ros2 launch nav_bot sim.launch.py

```
### Paso 2: Inicia el Mapeador (SLAM)
Usa `slam_toolbox` para dibujar el mapa en vivo.

```bash
# Terminal 2
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True

```
*En RViz, deberías ver cómo el mapa empieza a aparecer (gris/blanco) alrededor del robot.*

### Paso 3: Explora!
El mapa no se hace solo. Tienes que mover el robot por **todo** tu mundo nuevo para que el láser lo registre.

```bash
# Terminal 3
ros2 run teleop_twist_keyboard teleop_twist_keyboard

```
*Conduce hasta que tu mundo se vea completo y nítido en RViz.*
### Paso 4: Genera el YAML (El paso que faltaba)
Una vez que el mapa se vea bien en RViz, ejecuta este comando para guardarlo en tu disco:
```bash
# Terminal 4
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/src/nav_bot/maps/mapa_nuevo
```
**¡Listo!** Ahora sí tienes el archivo `mapa_nuevo.yaml` y `mapa_nuevo.pgm`.
Ahora puedes cerrar todo y volver a ejecutar tu archivo maestro `navigation.launch.py` (asegurándote de haber actualizado la ruta dentro del archivo para que apunte a este `mapa_nuevo.yaml`).


Error: El robot no detecta obstáculos (Lidar no visible)
Causa: Falta el plugin de sensores en el mundo SDF.
Solución: Asegúrate de que tu archivo .sdf incluye <plugin name='gz::sim::systems::Sensors' ...>.

Error: El mapa no carga al iniciar navigation.launch.py

Causa: El archivo .yaml no se encuentra.

Solución: Verifica que el nombre del mapa en navigation.launch.py coincida con el archivo en la carpeta maps/ y que hayas recompilado con colcon build.



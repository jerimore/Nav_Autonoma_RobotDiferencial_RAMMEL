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
## 🔧 Solución de Problemas Comunes (Troubleshooting)

### 🔴 Error: "No map received" en RViz

Este error puede deberse a dos causas principales. Verifica cuál es tu caso:

**Causa 1: Configuración de QoS incorrecta en RViz**
* **Solución:** En el panel izquierdo de RViz, despliega las propiedades del elemento **Map**. Busca la opción **Topic** -> **Durability Policy** y cámbiala a `Transient Local`.

**Causa 2: Mapa inexistente para un nuevo mundo**
* **Diagnóstico:** Si estás usando un mundo nuevo (`.sdf`) pero no has generado su mapa correspondiente (`.yaml` y `.pgm`), Nav2 no tendrá referencia para navegar.
* **Solución:** Debes realizar una sesión de mapeo (SLAM) antes de navegar. Sigue estos pasos:

    1.  **Lanza la simulación con tu mundo:**
        ```bash
        ros2 launch nav_bot sim.launch.py
        ```
    2.  **Inicia SLAM Toolbox (Mapeo en vivo):**
        ```bash
        ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
        ```
    3.  **Explora el entorno:**
        Mueve el robot por toda el área para escanear los obstáculos.
        ```bash
        ros2 run teleop_twist_keyboard teleop_twist_keyboard
        ```
    4.  **Guarda el mapa:**
        Cuando el mapa en RViz esté completo, guárdalo:
        ```bash
        ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/src/nav_bot/maps/mapa_nuevo
        ```
    > **Nota:** Recuerda actualizar tu archivo `navigation.launch.py` para que apunte a `mapa_nuevo.yaml` antes de volver a lanzar la navegación.

---

### 🔴 Error: El robot no detecta obstáculos (Lidar no visible)

* **Causa:** Falta el plugin de sensores en el archivo de descripción del mundo (`.sdf`).
* **Solución:** Abre tu archivo `.sdf` y asegúrate de que el bloque `<world>` incluya el siguiente plugin:
    ```xml
    <plugin name='gz::sim::systems::Sensors' filename='gz-sim-sensors-system'>
        <render_engine>ogre2</render_engine>
    </plugin>
    ```

---

### 🔴 Error: El mapa no carga al iniciar `navigation.launch.py`

* **Causa:** Ruta del archivo incorrecta o falta de compilación.
* **Solución:**
    1.  Verifica que el nombre del archivo en `navigation.launch.py` coincida exactamente con el archivo en la carpeta `maps/`.
    2.  Asegúrate de que los cambios se hayan reflejado en la carpeta `install` recompilando el paquete:
        ```bash
        colcon build --symlink-install
        source install/setup.bash
        ```



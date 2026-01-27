```markdown
NavBot: Navegación Autónoma con ROS 2 Jazzy y Gazebo Harmonic

![ROS 2](https://img.shields.io/badge/ROS_2-Jazzy-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-FF6F00?style=for-the-badge&logo=gazebo&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

Proyecto de simulación de un robot móvil diferencial que integra **SLAM** (con `slam_toolbox`) y el stack completo **Nav2** para navegación autónoma, evasión de obstáculos y planificación de rutas en **Gazebo Harmonic**.

Tabla de Contenidos

- [Características Principales](#-características-principales)
- [Prerrequisitos](#-prerrequisitos)
- [Instalación](#-instalación)
- [ Guía de Uso: Navegación Autónoma](#-guía-de-uso-navegación-autónoma)
  - [Paso 1: Iniciar la simulación](#paso-1-iniciar-la-simulación)
  - [Paso 2: Inicializar la localización](#paso-2-inicializar-la-localización)
  - [Método 1: Control manual con RViz](#método-1-control-manual-con-rviz)
  - [Método 2: Misiones autónomas por script Python](#método-2-misiones-autónomas-por-script-python)
- [ Generación de Nuevos Mapas (SLAM)](#-generación-de-nuevos-mapas-slam)
- [ Solución de Problemas Comunes](#-solución-de-problemas-comunes)
- [Autor](#autor)

Características Principales

- Simulación física realista en Gazebo Harmonic (robot diferencial con URDF/Xacro)
- Sensores simulados: LIDAR 2D + odometría vía plugin `DiffDrive`
- Mapeo con `slam_toolbox` (modo online async)
- Navegación autónoma completa con **Nav2** (planificación global/local, recuperación, evasión dinámica)
- Soporte para misiones programadas en Python usando `nav2_simple_commander`

Prerrequisitos

Ubuntu 24.04 + ROS 2 Jazzy Jalisco + Gazebo Harmonic instalados.

Instala los paquetes necesarios:

```bash
sudo apt update
sudo apt install -y \
  ros-jazzy-navigation2 ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox ros-jazzy-nav2-simple-commander \
  ros-jazzy-ros-gz ros-jazzy-ros-gz-bridge ros-jazzy-ros-gz-sim \
  ros-jazzy-teleop-twist-keyboard ros-jazzy-xacro
```

**Nota:** `ros-jazzy-ros-gz-bridge` es **obligatorio** para comunicar ROS 2 con Gazebo Harmonic (tópicos como `/scan`, `/odom`, etc.).

##  Clonar

1. Clona el repositorio en tu workspace:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/TU_USUARIO/nav_bot.git
```

2. Compila:

```bash
cd ~/ros2_ws
colcon build --symlink-install
```

3. Configura el entorno (agrega esto a tu `~/.bashrc` si lo deseas):

```bash
source ~/ros2_ws/install/setup.bash
```

##  Guía de Uso: Navegación Autónoma

### Paso 1: Iniciar la simulación

Ejecuta el launch principal (abre Gazebo, Nav2 y RViz):

```bash
ros2 launch nav_bot navigation.launch.py
```

Espera 10–20 segundos hasta que todo cargue completamente.

### Paso 2: Inicializar la localización (muy importante)

El robot aparece sin localización inicial → debes indicarle dónde está.

En RViz:
- Haz clic en **"2D Pose Estimate"** (barra superior)
- Haz clic en el mapa ≈ donde ves el robot en Gazebo
- Arrastra la flecha para indicar hacia dónde apunta el frente del robot

Éxito = aparecerá una nube de partículas verdes alrededor del robot.

### Método 1: Control manual con RViz

- Haz clic en **"Nav2 Goal"** (barra superior)
- Haz clic en el mapa + arrastra para definir posición y orientación deseada
- El robot planificará y ejecutará la trayectoria automáticamente

### Método 2: Misiones autónomas por script Python

Ideal para secuencias programadas (ir a A → esperar → ir a B, etc.).

Asegúrate de que:
- La simulación esté corriendo
- El robot esté localizado (paso 2)

Ejecuta en una terminal nueva:

```bash
python3 ~/ros2_ws/src/nav_bot/scripts/mision_autonoma.py
```

Edita las coordenadas dentro del script según necesites.

## 🗺 Generación de Nuevos Mapas (SLAM)

Para crear un mapa nuevo de cualquier mundo:

1. Lanza la simulación básica (sin Nav2):

```bash
ros2 launch nav_bot sim.launch.py
```

2. Inicia SLAM Toolbox:

```bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

3. Teleopera el robot para explorar:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

4. Guarda el mapa (recomendado – evita errores QoS):

Opción A – Más estable (usa servicio):

```bash
# Terminal 1: lanza el servidor saver
ros2 run nav2_map_server map_saver_server

# Terminal 2: llama al servicio
ros2 service call /map_saver/save_map nav2_msgs/srv/SaveMap "{map_url: '~/ros2_ws/src/nav_bot/maps/mi_mapa_nuevo'}"
```

Opción B – CLI directo (puede fallar por QoS en Jazzy):

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/src/nav_bot/maps/mi_mapa_nuevo
```

**Si falla con "DURABILITY_QOS_POLICY" o "Failed to spin map subscription":**
- En RViz → selecciona el topic `/map` → cambia **Durability Policy** a **Transient Local**
- Vuelve a intentar

5. (Opcional) Edita el `.yaml` generado y verifica que el campo `image:` apunte correctamente al `.pgm`

## Solución de Problemas Comunes

- **"No map received" en RViz**  
  → En las propiedades del topic `/map` cambia **Durability Policy** a **Transient Local**

- **No se ven datos de `/scan` o el robot no evita obstáculos**  
  → Verifica que tu launch incluya el bridge (`ros_gz_bridge`) y que el plugin de sensores esté en el modelo SDF del robot

- **Error al guardar mapa con map_saver_cli (QoS DURABILITY)**  
  → Usa la opción con `map_saver_server` + service call (ver arriba) o fuerza Transient Local en RViz

- **El mapa no carga en navigation.launch.py**  
  → Verifica que el nombre del archivo .yaml coincida exactamente con el parámetro en el launch y haz `colcon build` nuevamente

- **Gazebo no publica tópicos a ROS**  
  → Asegúrate de tener instalado y corriendo `ros-jazzy-ros-gz-bridge`

## Autor

**Jeremy S (Jeremy Rivera Moreira)**  
Ingeniería en Mecatronica / Espol 
Proyecto de simulación y navegación autónoma · 2025–2026  




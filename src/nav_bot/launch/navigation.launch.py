import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Configuración de Directorios
    pkg_nav_bot = get_package_share_directory('nav_bot')
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')

    # Ruta al mapa que acabamos de mover
    map_file = os.path.join(pkg_nav_bot, 'maps', 'mapa_mundo_prueba.yaml')

    # Ruta a los parámetros de Nav2 (Usaremos los por defecto de momento)
    nav2_params = os.path.join(pkg_nav2_bringup, 'params', 'nav2_params.yaml')

    # 2. Incluir nuestra simulación (Gazebo + Robot)
    # Nota: Asegúrate de que 'sim.launch.py' es el nombre correcto de tu archivo anterior
    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav_bot, 'launch', 'sim.launch.py')
        ),
        # Importante: Si tu sim.launch.py ya abre RViz, aquí podríamos tener duplicados.
        # Por ahora asumimos que sim.launch.py NO abre RViz configurado para Nav2.
    )

    # 3. Incluir Nav2 Bringup (El cerebro de la navegación)
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'map': map_file,
            'params_file': nav2_params,
            'autostart': 'true',  # Arranca automáticamente el ciclo de vida
        }.items()
    )

    # 4. Lanzar RViz preconfigurado para Nav2 (Opcional pero recomendado)
    # Nav2 trae una configuración de RViz muy buena por defecto.
    rviz_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'rviz_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'namespace': '',
            'use_namespace': 'False',
        }.items()
    )

    return LaunchDescription([
        sim_launch,
        nav2_launch,
        rviz_cmd
    ])

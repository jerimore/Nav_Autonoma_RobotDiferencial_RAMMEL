import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_nav_bot = get_package_share_directory('nav_bot')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # 1. Incluir el Robot State Publisher (rsp.launch.py)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav_bot, 'launch', 'rsp.launch.py')
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )
   
    # Definir la ruta al archivo del mundo (Corregido espacios vs tabs aquí)
    world_path = os.path.join(pkg_nav_bot, 'worlds', 'mundo_prueba.sdf')

    # 2. Iniciar Gazebo Harmonic con nuestro mundo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world_path}'}.items()
    )

    # 3. Spawnear el robot
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', 'robot_description',
                   '-name', 'nav_bot',
                   '-z', '0.1'],
        output='screen'
    )

    # 4. Bridge (Puente ROS <-> Gazebo)
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model'
        ],
        output='screen'
    )

    slam_params_file = os.path.join(get_package_share_directory('nav_bot'), 'config', 'slam_params.yaml')

    slam_toolbox = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',  # o lifelong_slam_toolbox_node si usas lifelong
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params_file,
            {'use_sim_time': True}
        ]
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        bridge,
        slam_toolbox    
    ])  
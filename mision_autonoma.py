import time
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from geometry_msgs.msg import PoseStamped

def main():
    # 1. Iniciar ROS 2
    rclpy.init()
    nav = BasicNavigator()

    # 2. Esperar a que Nav2 esté activo
    # (Asegúrate de haber lanzado navigation.launch.py antes de correr este script)
    print("Esperando a que Nav2 esté listo...")
    # nav.waitUntilNav2Active() # Descomenta si quieres que espere automáticamente

    # DEFINIR PUNTO A
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = nav.get_clock().now().to_msg()
    
    # COORDENADAS A
    goal_pose1.pose.position.x = 0.11024327576160431
    goal_pose1.pose.position.y = 0.7243705987930298
    goal_pose1.pose.orientation.w = 1.0

    # Yendo al punto A
    print("Dirigiendome al Punto A")
    nav.goToPose(goal_pose1)

    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        # Distancia Restante
        print(f'Distancia: {feedback.distance_remaining:.2f} m')

    print("He Llegado al Punto A. Espero 5 segundos")
    time.sleep(5)

    # DEFINIR PUNTO B 
    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = nav.get_clock().now().to_msg()
    
    # COORDENADAS B
    goal_pose2.pose.position.x = 3.584080934524536 
    goal_pose2.pose.position.y = -3.270587205886841
    goal_pose2.pose.orientation.w = 1.0

    # --- IR AL PUNTO B ---
    print("Yendo al Punto B...")
    nav.goToPose(goal_pose2)

    while not nav.isTaskComplete():
        pass

    # --- RESULTADO FINAL ---
    result = nav.getResult()
    if result == TaskResult.SUCCEEDED:
        print('¡Misión Completada con Éxito!')
    elif result == TaskResult.CANCELED:
        print('Misión Cancelada')
    elif result == TaskResult.FAILED:
        print('¡La misión falló!')

    rclpy.shutdown()

if __name__ == '__main__':
    main()

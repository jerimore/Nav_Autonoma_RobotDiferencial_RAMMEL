import time
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    # 1. Iniciar ROS 2
    rclpy.init()

    # 2. Crear el objeto navegador (nuestro "Capitán")
    navigator = BasicNavigator()

    # 3. Esperar a que Nav2 esté listo (se asegura de que AMCL, mapas, etc. estén activos)
    #    NOTA: ¡Debes haber localizado el robot en RViz antes de que esto termine de cargar!
    print("Esperando a que Nav2 se active...")
    navigator.waitUntilNav2Active()

    # 4. Definir nuestro destino (Punto A)
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    
    # --- COORDENADAS (MODIFICA ESTO SEGÚN TU MAPA) ---
    goal_pose.pose.position.x = 4.262  # Metros hacia adelante
    goal_pose.pose.position.y = -1.290 # Metros a la izquierda
    goal_pose.pose.orientation.z = 0.430 # Orientación (mirando al frente)
    goal_pose.pose.orientation.w = 0.903
    # -------------------------------------------------

    # 5. ¡Enviar la orden!
    print(f"Yendo a x={goal_pose.pose.position.x}, y={goal_pose.pose.position.y}...")
    navigator.goToPose(goal_pose)

    # 6. Bucle de monitoreo (mientras el robot se mueve)
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        # Podríamos imprimir feedback.distance_remaining aquí si quisiéramos
        # print(f"Distancia restante: {feedback.distance_remaining:.2f}m")
        # Esperar un poco para no saturar la CPU
        time.sleep(1.0)

    # 7. Verificar el resultado final
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('¡Misión Cumplida! Llegamos al destino.')
    elif result == TaskResult.CANCELED:
        print('La misión fue cancelada.')
    elif result == TaskResult.FAILED:
        print('¡Misión Fallida! (¿Había un obstáculo imposible?)')

    # 8. Apagar
    exit(0)

if __name__ == '__main__':
    main()

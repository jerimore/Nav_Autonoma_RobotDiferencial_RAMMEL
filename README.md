Primer Paso: Clonar el repositorio
Segundo Paso: Acceder a nuestro repositorio con el comando cd
Tercer paso construir el paquete usando comnado: colcon build --symlink-install
Cuarto paso hacer referencia source de nuestro paquete: source install/setup.bash
Quinto Paso: Ejecutar el comando que nos permitira simular la navegacion Autonoma del Robot: ros2 launch nav_bot navigation.launch.py
<img width="810" height="586" alt="imagen" src="https://github.com/user-attachments/assets/02861c3c-86b1-4350-99c8-f3214b660490" />

Sexto Paso: Una vez abierto Rviz y nuestro mundo en Gazebo: "Mundo Prueba", podremos simular dentro del mismo la navegacion autonoma manualmente o dirigida por un comando a traves de un script de navegacion.
Nota: Asegurarse antes de empezar que el mapa en Rviz y Gazebo esten en la misma orientacion, esto con el fin de que al utilizar la herramienta 2D Estimate Pose sea mas preciso la estimacion en Rviz de nuestro robot.
Herramienta 2D Estimate Pose:
<img width="1920" height="1080" alt="Captura desde 2026-01-29 10-29-41" src="https://github.com/user-attachments/assets/0501ab76-b5ab-4659-8706-e78f2c864154" />

Mundo en Gazebo:
<img width="1920" height="1080" alt="Captura desde 2026-01-29 10-30-43" src="https://github.com/user-attachments/assets/0df58dab-c910-4f31-9818-447e6ab2ccd6" />
Verificamos que no haya errores en Rviz en el lado izquiero Displays o en Nav2:
<img width="1271" height="1017" alt="imagen" src="https://github.com/user-attachments/assets/049d5c02-c18e-4e68-9ce0-1e4eb29efe54" />

A partir de aqui tenemos tres opciones.
Utilizar el comando del paquete teleop_key para operar el robot con las teclas (u i o j k l), o realizar la navegacion autonama con objetivos utilizando la herramienta de Rviz Nav2 Goal
Ejemplo de utilizar Nav2 Goal
<img width="1271" height="1017" alt="Captura desde 2026-01-29 10-34-16" src="https://github.com/user-attachments/assets/144b6b1a-8d63-4105-aae7-fb5eea856823" />

Resultado esperado: El robot se orienta hacia el punto que dirigimos la flecha de Nav2 Goal
<img width="1271" height="1017" alt="Captura desde 2026-01-29 10-34-48" src="https://github.com/user-attachments/assets/fa502e62-5932-4ef6-8195-6815ee2bd005" />

Ejecutando el script de Nav Autonoma
Para ello necesitaremos otro terminal
Encontrarnos en nuestra carpeta de repositorio
Y realizar source de nuestro paquete 
Luego Ejecutamos la mision Autonoma con el comando: python3 mision_autonoma.py
<img width="817" height="582" alt="imagen" src="https://github.com/user-attachments/assets/eba0d24b-d17a-4f26-b8b6-41efb4fbe704" />

Como resultado: Por salida de consola podremos ver el desplazamiento de nuestro robot hacia el punto predefinido en el script, tambien en Rviz y Gazebo podemos observar como fisicamente, el robot buscara el punto A y luego de una espera de 3 segundos buscara el Punto B.
<img width="1835" height="856" alt="imagen" src="https://github.com/user-attachments/assets/cae7fd7d-325c-4b4c-ad7d-4a4c86277163" />


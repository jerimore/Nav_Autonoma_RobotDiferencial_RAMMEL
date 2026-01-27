import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'nav_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # 1. Instalar archivos de lanzamiento (.launch.py)
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        
        # 2. Instalar archivos de descripción (URDF/Xacro)
        (os.path.join('share', package_name, 'description', 'urdf'), glob('description/urdf/*.xacro')),
        
        # 3. Instalar archivos de MUNDO (SDF) 
        # ESTA ES LA LINEA NUEVA QUE NECESITAS:
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')), # <--- ¡ESTA ES LA LÍNEA QUE FALTA!
        (os.path.join('share', package_name, 'maps'), glob('maps/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeremy',
    maintainer_email='jeremy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'patrol = nav_bot.patrol:main',
        ],
    },
)

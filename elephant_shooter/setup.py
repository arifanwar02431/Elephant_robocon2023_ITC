from setuptools import setup

package_name = 'elephant_shooter'
shooter_name = 'shooter'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, shooter_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotic',
    maintainer_email='chetsokhpanha@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = elephant_shooter.client:main',
            'service = elephant_shooter.service:main',
            'can = elephant_shooter.shooter_can:main',
            'shooter = elephant_shooter.shooter:main',
            'command = elephant_shooter.shoot_command:main',
        ],
    },
)
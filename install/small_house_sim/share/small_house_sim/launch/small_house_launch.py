from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '/home/saheer/ros2_ws/gazebo_models/aws_small_house/worlds/small_house.world',
                '-s', 'libgazebo_ros_factory.so'
            ],
            output='screen'
        )
    ])


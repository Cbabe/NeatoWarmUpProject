"""Read lidar data to tell neato to avoid objects"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time
import numpy as Np
import random

class obstacle_avoider(Node):
    def __init__(self):
        self.state=0
        super().__init__('receive_laser_data')
        self.sub = self.create_subscription(LaserScan, 'scan', self.arbitor, 10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def arbitor(self, msg):
        #Collect the front scan
        front_360 = Np.array(msg.ranges)

        front_360[Np.where(front_360 ==0.0)] = 10.0

        Distance = Np.min(front_360[330:361]+ front_360[0:31])
        self.goforwards(Distance)


        
            
    def goforwards(self, Distance):
        speed_msg = Twist()
        sleep_time = 3.2

        angular_velocity = [-0.48, 0.48, -0.7, 0.7]

        if Distance > 2.5:
            speed_msg.linear.x = .1
            speed_msg.angular.z = 0.0
            self.publisher.publish(speed_msg)
        else:
            rotation_speed = random.choice(angular_velocity)
            speed_msg.linear.x = 0.0
            speed_msg.angular.z = rotation_speed
            self.publisher.publish(speed_msg)
            time.sleep(sleep_time)


         



   


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = obstacle_avoider()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()
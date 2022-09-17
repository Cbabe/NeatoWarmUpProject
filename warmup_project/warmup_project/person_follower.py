"""Read lidar data to tell neato to avoid objects"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time
import numpy as Np
import random

class person_follower(Node):
    def __init__(self):
        self.state=0
        super().__init__('receive_laser_data')
        self.sub = self.create_subscription(LaserScan, 'scan', self.arbitor, 10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def arbitor(self, msg):
        #Collect the front scan
        front_90 = Np.array(msg.ranges[315:360]+msg.ranges[0:45]) #90 degrees in front
        front_90[Np.where(front_90 ==0.0)] = 10.0
        #distance=Np.min(front_90)
        #print(distance)
        degree=Np.argmin(front_90)
        print("distance")
        print(front_90[degree])

        #gotoangle=Np.min(distanes)
        stop=0
        if front_90[degree]<0.2:
            stop=1
        
        self.goforwards(degree,stop)


            
    def goforwards(self, degree, stop):
        speed_msg = Twist()
        degree=degree-45+3
        print("degree")
        print(degree)
        sleep_time = 3.5/90.0*abs(degree)
        #print(sleep_time)
        #Stop if to close
        if stop:
            print("Reached person")
            self.publisher.publish(speed_msg)
            return
        #Turn
        elif degree <0:
            print("Turn Right")
            speed_msg.angular.z = -0.48
        elif degree >0:
            print("Turn Left")
            speed_msg.angular.z = 0.48
        self.publisher.publish(speed_msg)
        time.sleep(sleep_time)
        #Go forwards
        speed_msg = Twist()
        speed_msg.linear.x = 1.
        self.publisher.publish(speed_msg)
        time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = person_follower()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()
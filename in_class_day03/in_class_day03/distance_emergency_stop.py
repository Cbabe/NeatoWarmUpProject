"""Read lidar data to tell neato to stop"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class emergency_stop(Node):
    def __init__(self):
        super().__init__('receive_laser_data')
        self.sub = self.create_subscription(LaserScan, 'scan', self.go_forwards,10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def go_forwards(self, msg):
        
        trigger = msg.ranges[0]
        #trigger = (sum(msg.ranges[0:5])/5 + sum(msg.ranges[355:360])/5) /2
        print(trigger)
        
        speed_msg = Twist()

        if trigger <= 1 and trigger != 0.0:
            speed_msg.linear.x = 0.0
        else:
            speed_msg.linear.x = 0.1
        
        self.publisher.publish(speed_msg)


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = emergency_stop()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()

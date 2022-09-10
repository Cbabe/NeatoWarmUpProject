"""Read bump data to tell neato to stop"""

import rclpy
from rclpy.node import Node
from neato2_interfaces.msg import Bump
from geometry_msgs.msg import Twist

class emergency_stop(Node):
    def __init__(self):
        super().__init__('receive_bump_data')
        self.sub = self.create_subscription(Bump, 'bump', self.go_forwards,10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def go_forwards(self, msg):
        trigger = msg.left_front + msg.left_side + msg.right_front + msg.right_side
        print(trigger)
        
        speed_msg = Twist()

        if trigger >= 1:
            speed_msg.linear.x = 0.0
        else:
            speed_msg.linear.x = 0.2
        
        self.publisher.publish(speed_msg)


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = emergency_stop()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()

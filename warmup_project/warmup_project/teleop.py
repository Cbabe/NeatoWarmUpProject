"""Read bump data to tell neato to stop"""

import rclpy
from rclpy.node import Node
from neato2_interfaces.msg import Bump
from geometry_msgs.msg import Twist
import tty
import select
import sys
import termios

class teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        print("WASD key board: W forward, S Backward, A Turn Right, D Turn Left, Any key to stop.")
        self.go_forwards()
    
    def go_forwards(self):
        key=None
        while key != '\x03':
            #Get key value - waits until user presses key
            key = getKey()
            speed_msg = Twist()
            if key=='w':
                #Forward
                speed_msg.linear.x = 1.0
            elif key=='s':
                #Backward
                speed_msg.linear.x = -1.0
            elif key=='a':
                #Turn Right
                speed_msg.angular.z = 1.0
            elif key=='d':
                #Turn Left
                speed_msg.angular.z = -1.0
            #Publish
            self.publisher.publish(speed_msg)


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = teleop()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

def getKey():
    settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    main()

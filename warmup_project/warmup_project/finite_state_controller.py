"""Switch between teleop and square drive"""

import rclpy
from rclpy.node import Node
from neato2_interfaces.msg import Bump
from geometry_msgs.msg import Twist
import tty
import select
import sys
import termios
import time

class finite_state_controller(Node):
    def __init__(self):
        super().__init__('receive_bump_data')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        print("WASD key board: W forward, S Backward, A Turn Right, D Turn Left or 0 to enter square drive. Any key to stop.")
        self.arbit()
    
    def arbit(self):
        key=None
        while key != '\x03':
            #Get key value - waits until user presses key
            key = getKey()
            speed_msg = Twist()
            state = 1

            if key == '0' or state == 0:
                for i in range(4):
                    self.go_forwards(speed_msg)
                    self.turn_right(speed_msg)
                    self.stop_moving(speed_msg)

                if key == '9':
                    state == 1

            elif key == '9' or state == 1:

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
                elif key == '0':
                    state = 0
                #Publish
                self.publisher.publish(speed_msg)

    def go_forwards(self,speed_msg):
        #drive forward 
        speed_msg.angular.z = 0.0
        speed_msg.linear.x = 0.18
        self.publisher.publish(speed_msg)
        time.sleep(5)

    
    def turn_right(self,speed_msg):
        #Turn right
        speed_msg.linear.x = 0.0
        speed_msg.angular.z = -0.46
        self.publisher.publish(speed_msg)
        time.sleep(3.5)

    def stop_moving(self,speed_msg):
        #Set all speeds to 0
        speed_msg.linear.x = 0.0
        speed_msg.angular.z = 0.0
        self.publisher.publish(speed_msg)
        time.sleep(1)


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = finite_state_controller()   # Create our Node
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

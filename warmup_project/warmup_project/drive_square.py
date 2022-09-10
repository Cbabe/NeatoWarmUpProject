""" THis node will have the neato drive roughly in a square"""


from signal import pause
import rclpy
import time
from rclpy.node import Node
from neato2_interfaces.msg import Bump
from geometry_msgs.msg import Twist

class drive_square(Node):
    def __init__(self):
        super().__init__('drive_in_square')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        speed_msg = Twist()

        self.stop_moving(speed_msg)
        print("start")

        #leg 1
        self.go_forwards(speed_msg)
        self.turn_right(speed_msg)
        self.stop_moving(speed_msg)
        print("here")

        #leg 2
        self.go_forwards(speed_msg)
        self.turn_right(speed_msg)
        self.stop_moving(speed_msg)
        print("there")

        #leg 3
        self.go_forwards(speed_msg)
        self.turn_right(speed_msg)
        self.stop_moving(speed_msg)
        print("everywhere")

        #leg 4
        self.go_forwards(speed_msg)
        self.turn_right(speed_msg)
        self.stop_moving(speed_msg)
        print("Done.")

    
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
    node = drive_square()         # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()
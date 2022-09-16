"""Read lidar data to tell neato to follow a wall"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from visualization_msgs.msg import Marker
import time

class wall_folower(Node):
    def __init__(self):
        self.state=0
        super().__init__('receive_laser_data')
        self.sub = self.create_subscription(LaserScan, 'scan', self.arbitor, 10)
        self.vis_pub = self.create_publisher(Marker, 'visualization_marker', 10)

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
    
    def arbitor(self, msg):
        
        forward = [msg.ranges[0],msg.ranges[1],msg.ranges[359]]
        forward45=msg.ranges[310:321]
        side=msg.ranges[268:270]
        back45=msg.ranges[210:231]
        list(filter(lambda x: x != 0.0, forward))
        list(filter(lambda x: x != 0.0, forward45))
        list(filter(lambda x: x != 0.0, side))
        list(filter(lambda x: x != 0.0, back45))
        averageforward=sum(forward)/len(forward)
        averageforward45=sum(forward45)/len(forward45)
        averageside=sum(side)/len(side)
        averageback45=sum(back45)/len(back45)
        data=[averageforward,averageforward45,averageside,averageback45]

        print(data)
        print(self.state)
        if self.state==0:
            self.goforwards(averageforward)
        elif self.state==1:
            self.wallfollowing(data)
        
            
    def goforwards(self, averageforward):
        speed_msg = Twist()
        if averageforward>=0.7:
            speed_msg.linear.x = 0.3
            self.publisher.publish(speed_msg)
        else:
            speed_msg.linear.x=0.0
            speed_msg.angular.z=0.48
            self.state=1
            self.publisher.publish(speed_msg)
            time.sleep(3.2)



    def wallfollowing(self, data):
        speed_msg = Twist()
        if abs(data[1]-data[3])<0.01:
            print("Forwards")
            speed_msg.linear.x = 0.1
        elif data[1]>data[3]:
            print("Left")
            turn=abs(data[1]-data[3])
            speed_msg.linear.x = 0.1
            speed_msg.angular.z=-turn
        elif data[1]<data[3]:
            print("Right")
            turn=abs(data[1]-data[3])
            speed_msg.linear.x = 0.1
            speed_msg.angular.z=turn
        self.publisher.publish(speed_msg)


def main(args=None):
    rclpy.init(args=args)         # Initialize communication with ROS
    node = wall_folower()   # Create our Node
    rclpy.spin(node)              # Run the Node until ready to shutdown
    rclpy.shutdown()              # cleanup

if __name__ == '__main__':
    main()

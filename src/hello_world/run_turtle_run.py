#! /usr/bin/python3

import rospy
import time

from geometry_msgs.msg import Twist

rospy.init_node('splinter')

pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

msg=Twist()
msg.linear.x=1.0
msg.angular.z=1.0
while not rospy.is_shutdown():
   pub.publish(msg)
   time.sleep(1.0)


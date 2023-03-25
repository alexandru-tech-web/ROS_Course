#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(2)
val_twist = Twist()
val_twist.angular.z = 1.0

while not rospy.is_shutdown():
	pub.publish(val_twist)
	rate.sleep()


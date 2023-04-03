#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

move = Twist()

def callback(msg):

#forward
  if msg.ranges[360] > 1:
      move.linear.x = 0.5
      move.angular.z = 0.0


   if msg.ranges[360] < 1:
      move.linear.x = 0.0
      move.angular.z = 0.5
 #left if obj in right     
   if msg.ranges[0] < 1:
      move.linear.x = 0.0
      move.angular.z = 0.5
  #right if obj in left    
   if msg.ranges[719] > 1:
      move.linear.x = 0.0
      move.angular.z = -0.5

  pub.publish(move)

rospy.init_node('topic_publisher')
sub = rospy.Subscriber('/scan', LaserScan, callback) 
pub = rospy.Publisher('/cmd_vel', Twist)

rospy.spin()

#! /usr/bin/env python

import rospy
from quiz_services_pkg.srv import custommessage, custommessageResponse
from geometry_msgs.msg import Twist 


def my_callback(request):
    rospy.loginfo("Serverul este actionat")
    move.linear.x = request.side    #move in linear
    move.angular.z = -1.57          # move in angular 90* 
    move.linear.x = request.side
    move.angular.z = -1.57
    move.linear.x = request.side
    move.angular.z = -1.57
    move.linear.x = request.side
    move.angular.z = -1.57
    i = 0
    for i  in range(request.repetition):
        pub.publish(move)
        rospy.sleep(2)
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    response.success = True
    return response


move = Twist()
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
rospy.init_node('service_server') 
response = custommessageResponse()
my_service = rospy.Service('/move_square', custommessage , my_callback) 
rospy.spin()
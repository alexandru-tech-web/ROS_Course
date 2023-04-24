#! /usr/bin/env python3
import rospy
# Import the service message used by the service /trajectory_by_name
from quiz_services_pkg.srv import custommessage, custommessageRequest
import sys
# Initialise a ROS node with the name service_client
rospy.loginfo("Clientul este actionat")
rospy.init_node('service_client')
# Wait for the service client /move_in_square to be running
rospy.wait_for_service('/move_square')
# Create the connection to the service
move_direction_service = rospy.ServiceProxy('/move_square', custommessage)
# Create an object of type MoveInSquareRequest
move_direction_object = custommessageRequest()
move_direction_object.side = 5
move_direction_object.repetitions = 4
# Send through the connection the name of the request
result = move_direction_service(move_direction_object)
# Print the result given by the service called
print(result.success)
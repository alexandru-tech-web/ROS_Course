#!/usr/bin/env python

import rospy
import actionlib
from action_quiz_pkg.msg import RobAction, RobGoal
import rospy


def drone_control_client():
    # Initialize the ROS node
    rospy.init_node('drone_control_client')

    # Create an action client for the DroneControl action
    client = actionlib.SimpleActionClient('drone_control', RobAction)
    client.wait_for_server()

    # Create and populate the goal message
    goal = RobGoal()
    goal.command = "TAKEOFF"

    # Send the goal to the action server
    client.send_goal(goal)

    # Wait for the action to complete
    client.wait_for_result()

    # Get the final result of the action
    result = client.get_result()

    if result.status == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Drona sus!")
    else:
        rospy.loginfo("Drone la pamant!")


if __name__ == '__main__':
    rospy.init_node('drone_control_client')
    rospy.spin()

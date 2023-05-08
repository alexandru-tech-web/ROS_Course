#!/usr/bin/env python

import rospy
import actionlib
from action_quiz_pkg.msg import RobAction, RobGoal
import rospy


def drone_control_client():
 
    rospy.init_node('drone_control_client')


    client = actionlib.SimpleActionClient('drone_control', RobAction)
    client.wait_for_server()

 
    goal = RobGoal()
    goal.command = "TAKEOFF"


    client.send_goal(goal)

    client.wait_for_result()

 
    result = client.get_result()

    if result.status == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Drona sus!")
    else:
        rospy.loginfo("Drone la pamant!")


if __name__ == '__main__':
    rospy.init_node('drone_control_client')
    rospy.spin()

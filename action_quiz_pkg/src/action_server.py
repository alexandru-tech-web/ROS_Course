#! /usr/bin/python3

import rospy
import actionlib
from action_quiz_pkg.msg import RobAction, RobResult, RobFeedback

def drone_control_server():
   
    rospy.init_node('drone_control_server')

    
    server = actionlib.SimpleActionServer('drone_control', RobAction, execute_cb=execute_cb, auto_start=False)
    server.start()

    rospy.spin()

def execute_cb(self, goal):
    command = goal.command
    feedback = RobFeedback()

    if command == "TAKEOFF":
            while not self.server.is_preempt_requested():
                self.pub.publish("Urca")
                self.server.publish_feedback(feedback)
                self.rate.sleep()

            self.server.set_preempted()
            rospy.loginfo("DroneControlServer preempted during takeoff")
    elif command == "LAND":
            while not self.server.is_preempt_requested():
                self.pub.publish("Coboara")
                self.server.publish_feedback(feedback)
                self.rate.sleep()

            self.server.set_succeeded()
            rospy.loginfo("DroneControlServer completed landing")

    result = RobResult()

if __name__ == '__main__':
    rospy.init_node('drone_control_server')
    server = drone_control_server()
    server.start()
    rospy.spin()


















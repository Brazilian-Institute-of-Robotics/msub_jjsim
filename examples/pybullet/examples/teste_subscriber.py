#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + " data: %f", msg.data[1])
    print(msg.data[1])

if __name__ == '__main__':
    rospy.init_node('ros_bridge')
    rospy.Subscriber('/joint_state', Float64MultiArray, callback)
    rospy.spin()
    rospy.init_node('ros_bridge')

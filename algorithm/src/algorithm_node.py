#!/usr/bin/env python
import rospy
from common_msgs.msg import TimePose

def callback(msg):
    print "algorithm:", msg.timestamp.secs%40, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('algorithm_node')
sub = rospy.Subscriber('topic_msg', TimePose, callback)
rospy.spin()

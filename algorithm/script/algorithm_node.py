#!/usr/bin/env python
import rospy
from topic_custom.msg import TimePose

def callback(msg):
    print "subscribe:", msg.timestamp.secs%50, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('algorithm_node')
sub = rospy.Subscriber('topic_msg', TimePose, callback)
rospy.spin()
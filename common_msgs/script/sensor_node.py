#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from topic_custom.msg import TimePose

rospy.init_node('custom_publisher')
pub = rospy.Publisher('custom_msg', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second%2, y=second%4, theta=second%8)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%50, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()

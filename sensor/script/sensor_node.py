#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from topic_custom.msg import TimePose

rospy.init_node('sensor_node')
pub = rospy.Publisher('topic_msg', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second*2, y=second%4, theta=second+6)
    pub.publish(msg)
    print "sensor:", msg.timestamp.secs%40, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()

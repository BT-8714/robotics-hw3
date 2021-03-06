#!/usr/bin/env python
import rospy
from common_msgs.srv import AddTwoNum, AddTwoNumRequest

rospy.init_node('service_client')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', AddTwoNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 200:
    if count % 10 == 0:
        req = AddTwoNumRequest(a=count, b=count/5)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.sum
    rate.sleep()
    count += 1
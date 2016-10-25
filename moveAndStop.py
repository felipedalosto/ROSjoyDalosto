#!/usr/bin/env python

import rospy
import wx
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


def talker():

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(0.5) # 10hz
	pub.publish(Twist(Vector3(1,0,0),Vector3(0,0,0)))
	rate.sleep()
	pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,1.57)))
	rate.sleep()  

if __name__ == '__main__':
    try:
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		rospy.init_node('talker', anonymous=True)
		for i in range (3):
			talker()       	
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
    except rospy.ROSInterruptException: pass
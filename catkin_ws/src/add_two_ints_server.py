#!/usr/bin/env python
   2 
   3 from beginner_tutorials.srv import *
   4 import rospy
   5 
   6 def handle_add_two_ints(req):
   7     print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
   8     return AddTwoIntsResponse(req.a + req.b)
   9 
  10 def add_two_ints_server():
  11     rospy.init_node('add_two_ints_server')
  12     s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
  13     print "Ready to add two ints."
  14     rospy.spin()
  15 
  16 if __name__ == "__main__":
  17     add_two_ints_server()
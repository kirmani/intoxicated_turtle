#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

import rospy
from geometry_msgs.msg import Twist

def talker():
  pub = rospy.Publisher('turtlesim', Twist, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)  # 10 Hz
  while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 1.8
    rospy.loginfo("Drunk walking!!!")
    pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass

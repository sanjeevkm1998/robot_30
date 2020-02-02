#!/usr/bin/env python



import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion


import time

x=0.0
y=0.0
theta = 0.0

def newOdom(msg)
        global x
        global y
        global theta
        
        x= msg.pose.pose.position.x
        y= msg.pose.pose.position.y
        
        
        eular_from_quaternion
        
rospy.int_node("speed_controller")

sub = rospy.Subscriber("/o


#!/usr/bin/env python
import rospy 
from std_msgs.msg import String #sending strings across the nodes

def faxer(): #function faxer
    rospy.init_node("faxer", anonymous=True) #let ROS know faxer is the node, anonymous node means can do many nodes
    pub = rospy.Publisher("pigeon", String, queue_size=10) #topic is pigeon and stores 10 messages before deleting
    rate = rospy.Rate(10) #loop will run at 10Hz
    
    while not rospy.is_shutdown(): #keep running until ROS makes it stop
        message = "Happy to join the Space Concordia Robotics Division" 
        rospy.get_time() #get time at start of loop
        #rospy.loginfo(message) #message get printed to screen, to rosout and rqt_console
        pub.publish(message) #publish method from ROS to anyone connected (broadcast like a radio)
        rate.sleep() #makes the loop run at 10Hz

if __name__ == "__main__": #sets the file as main
    try:
        faxer()
    except rospy.ROSInterruptException:
        pass
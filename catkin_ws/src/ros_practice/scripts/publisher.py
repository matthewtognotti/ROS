#!/usr/bin/env python
#filename: publisher.py

import rospy
from std_msgs.msg import Float32 
from std_msgs.msg import String
import random

activelist = ["active", "inactive"]

def talker(): 
    pub0 = rospy.Publisher('topic0', Float32, queue_size=10)
    pub1 = rospy.Publisher('topic1', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(20) #20hz
    rospy.loginfo("Publisher Node has started, now publishing messages")

    while not rospy.is_shutdown():
        num = float(random.uniform(0, 10.0))
        string = str(random.choice(activelist))
        pub0.publish(num)
        pub1.publish(string)
        rate.sleep()

if __name__ == "__main__":
    try: 
        talker()
    except rospy.ROSInterruptException:
        pass


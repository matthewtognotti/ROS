#!/usr/bin/env python
#filename: subscriber.py

import rospy
from std_msgs.msg import Float32 
from std_msgs.msg import String


def callback(data):
    rospy.loginfo("Received Data: %s", data.data)    

def listener(): 
    rospy.init_node("subscriber", anonymous=True)
    rospy.Subscriber('topic0', Float32, callback)
    rospy.Subscriber('topic1', String, callback)
    rospy.spin()

if __name__ == "__main__":
    try: 
        listener()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
pub2 = rospy.Publisher('count_up', Int32, queue_size=1)
pub3 = rospy.Publisher('count_up', Int32, queue_size=1)
pub4 = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)

print("ドイツ語勉強講座！下の中から好きな言葉を選んでね。返事を返してくれるよ。")
print("1.Guten Morgen.(おはよう)\n2.Was machst du jetzt?(今何してるの？)\n3.Was ist dein Lieblingsessen?(好きな食べ物は？)\n4.Auf Wiedersehen.(さようなら)")

a = 13
b = 20
c = 28
d = 16

while not rospy.is_shutdown():
    name = input("言葉を入れてね:")

    if len(name) == 13 and name.isascii():
        pub.publish(a)
        rate.sleep()

    elif len(name) == 20 and name.isascii():
        pub2.publish(b)
        rate.sleep()

    elif len(name) == 28 and name.isascii():
        pub3.publish(c)
        rate.sleep()

    elif len(name) == 16 and name.isascii():
        pub4.publish(d)
        rate.sleep()
        break

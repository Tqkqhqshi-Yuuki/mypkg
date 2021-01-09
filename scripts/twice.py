#!/usr/bin/env python3

"""
BSD 3-Clause License
Copyright (c) 2021, Yuuki Takahashi and Ryuichi Ueda
All rights reserved.
"""

import rospy
import random
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
rate = rospy.Rate(10)

g = ["Guten Morge!","Hallo"]
i = ["Scheiße.(うんこ)", "Ich muss dich nicht unterrichten(君に教える必要はないね)", "イッヒ　フンバルト　デル　ウンコ(ドイツ語風)"]
a = ["Alles Essen, das du hasst, ist mein Favorit.(君の嫌いな食べ物全てが僕の好物さ)", "Was bedeutet es, es zu hören?(それを聞いて何の意味があるの？)"]
t = ["Tschü  ss(バイバイ)", "Wir sehen uns(またね)"]

while not rospy.is_shutdown():
    if n == 13:
        n = random.choice(g)
        print(f"re:{n}")

    elif n == 20:
        n = random.choice(i)
        print(f"re:{n}")

    elif n == 28:
        n = random.choice(a)
        print(f"re:{n}")

    elif n == 16:
        n = random.choice(t)
        print(f"re:{n}")
        break

    rate.sleep()

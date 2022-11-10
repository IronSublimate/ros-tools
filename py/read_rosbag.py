#!/usr/bin/env python3
import rosbag
import sys
import cv2
import numpy as np
from cv_bridge import CvBridge

bag = rosbag.Bag(sys.argv[1],'r')
br = CvBridge()


for topic, msg, t in bag.read_messages():
    # print(topic)
    # np_arr = np.fromstring(msg.data, np.uint8)
    # image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    image_np = br.compressed_imgmsg_to_cv2(msg)

    cv2.imshow("img",image_np)
    if cv2.waitKey(33)==27:
        break

bag.close()

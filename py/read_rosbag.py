#!/usr/bin/env python3
import rosbag
import sys
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, Image


def main():
    bag = rosbag.Bag(sys.argv[1], 'r')
    br = CvBridge()

    for topic, msg, t in bag.read_messages():
        if msg._type == CompressedImage._type:
            image_np = br.compressed_imgmsg_to_cv2(msg)
        elif msg._type == Image._type:
            image_np = br.imgmsg_to_cv2(msg)
        else:
            continue
        cv2.imshow("img", image_np)
        if cv2.waitKey(33) == 27:
            break

    bag.close()


if __name__ == '__main__':
    main()

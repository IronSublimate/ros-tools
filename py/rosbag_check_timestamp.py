#!/usr/bin/env python3
import rosbag
import sys
import numpy as np

from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import Header
from genpy import Time
from typing import List, Dict


def main():
    bag = rosbag.Bag(sys.argv[1], 'r')
    topic_times: Dict[str, List[float]] = {}

    for topic, msg, t in bag.read_messages():
        stamp: Time = msg.header.stamp
        # print(stamp.to_time())
        topic_times.setdefault(topic, []).append(stamp.to_time())

    bag.close()

    for k, v in topic_times.items():
        arr = np.array(v)
        diff = np.diff(arr)
        print("topic: ", k)
        print("    min time interval: ", min(diff))
        print("    max time interval: ", max(diff))


if __name__ == '__main__':
    main()

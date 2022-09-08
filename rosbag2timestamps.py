import numpy as np
import rosbag
import sys

def main(file):
	bag = rosbag.Bag(file)
	timestamps = np.ones(bag.get_message_count())
	ctr = 0
	for topic, msg, t in bag.read_messages(topics=['/ambf/env/cameras/default_camera/ImageData']):
		timestamps[ctr] = msg.header.stamp.to_sec()
		ctr = ctr + 1
	np.save('world_timestamps', timestamps)



if __name__ == "__main__":
	main(sys.argv[1])

import argparse

def args():
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"-v", "--video", 
		type=str, 
		required=True, 
		help="path to input video file")

	parser.add_argument(
		"-o", "--output", 
		type=str, 
		required=True, 
		help="path to output video frames")

	return parser.parse_args()
import time
import random
from PIL import Image
import io

IMAGEPATH = './database/image/image_2_{:06d}.png'
LIDARPATH = './database/pointcloud/velodyne_{:06d}.bin'

def capture_image(index):
    # Read and serialize image data
    with open(IMAGEPATH.format(index), 'rb') as image_file:
        image_data = image_file.read()
    return image_data

def capture_lidar(index):
    # Read and serialize pointcloud data
    with open(LIDARPATH.format(index), 'rb') as lidar_file:
        lidar_data = lidar_file.read()
    return lidar_data

def capture_data(index):
    while True:
        yield capture_image(index), capture_lidar(index)
        time.sleep(0.1)  # 10Hz
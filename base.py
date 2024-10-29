import numpy as np
import cv2
import open3d as o3d

pcf = "row2tree11/TestFolder/pointcloud/pointcloud_2.ply"
pcf2 = "row2tree11/TestFolder/depth_to_point/depth_to_point_2.ply"

# # Load Pointcloud
pcd1 = o3d.io.read_point_cloud(pcf)
o3d.visualization.draw_geometries([pcd1])

# Load Raw Depth Image
imagef = "/home/beck/Documents/ProjectMain/row2tree11/TestFolder/depth/depth_raw_2.png"
image = cv2.imread(imagef)

# View Raw Depth Image
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert Type
if len(image.shape) == 3:  # Check if the image is colored
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

if image.dtype != 'uint8':
    image = image.astype('uint8')

# De-Noising Attempts
# image = cv2.GaussianBlur(image,(3,3),0)
# image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)



# Depth Thresholding
# threshold = 5  
# max_assign_val = 255
# _, thresholded = cv2.threshold(image, threshold, max_assign_val, cv2.THRESH_BINARY)
# cv2.imshow("Thresholded Depth Image", thresholded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
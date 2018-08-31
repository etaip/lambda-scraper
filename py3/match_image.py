#!/usr/bin/env python

import cv2

def find_image(query_img_path, page_img_path):
    img1 = cv2.imread(query_img_path,0)          # queryImage
    img2 = cv2.imread(page_img_path,0) # trainImage

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
    # sift = cv2.SIFT()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    matched_point_indices = []
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
            matched_point_indices.append(m)

    matched_points = []
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    for m in matched_point_indices:
        point = kp2[m.trainIdx].pt
        matched_points.append(point)
        min_x = min(point[0], min_x)
        max_x = max(point[0], max_x)
        min_y = min(point[1], min_y)
        max_y = max(point[1], max_y)

    # print (min_x, min_y), (max_x, max_y)
    center_point = min_x + (max_x - min_x) / 2, min_y + (max_y - min_y) / 2

    return center_point


def main():
    query_img_path = 'query_image.png'
    page_img_path = 'page_image.png'
    center_point = find_image(query_img_path, page_img_path)
    print(center_point)


if __name__ == '__main__':
    main()

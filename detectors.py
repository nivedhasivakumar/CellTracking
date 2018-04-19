import numpy as np
import cv2

debug = 0


class Detectors(object):
    """Detectors class to detect objects in video frame
    Attributes:
        None
    """
    def __init__(self):
        """Initialize variables used by Detectors class
        """
        # self.fgbg = cv2.createBackgroundSubtractorMOG2()
        return

    def Detect(self, frame):
        """Detect objects in video frame using following pipeline
            - Convert captured frame from BGR to GRAY
            - Perform Background Subtraction
            - Detect edges using Canny Edge Detection
              http://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html
            - Retain only edges within the threshold
            - Find contours
            - Find centroids for each valid contours
        Args:
            frame: single video frame
        Return:
            centers: vector of object centroids in a frame
        """

        # # Convert BGR to GRAY
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        # if debug == 1:
        #     cv2.imshow('gray', gray)
        #
        # # Perform Background Subtraction
        # fgmask = self.fgbg.apply(gray)
        #
        # if debug == 0:
        #     cv2.imshow('bgsub', fgmask)
        #
        # # Detect edges
        # edges = cv2.Canny(fgmask, 50, 190, 3)
        #
        # if debug == 1:
        #     cv2.imshow('Edges', edges)

        # Retain only edges within the threshold
        # ret, thresh = cv2.threshold(edges, 127, 255, 0)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, 0)

        # Find contours
        # _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


        if debug == 0:
            cv2.imshow('thresh', thresh)

        centers = []  # vector of object centroids in a frame
        blob_radius_thresh = 10
        # Find centroid for each valid contours
        for cnt in contours:
            try:
                # Calculate and draw circle
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                centeroid = (int(x), int(y))
                radius = int(radius)
                if radius > blob_radius_thresh:
                    cv2.circle(frame, centeroid, radius, (0, 255, 0), 2)
                    b = np.array([[x], [y]])
                    centers.append(np.round(b))
            except ZeroDivisionError:
                pass

        # show contours of tracking objects
        # cv2.imshow('Track Bugs', frame)

        return centers

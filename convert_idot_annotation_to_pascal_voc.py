import xmltodict

with open('1.xml') as fd:
    doc = xmltodict.parse(fd.read())

import cv2

import pathlib
import os
import sys
import cv2


fname = sys.argv[1]
with open(fname) as f:
	while True:
		line = f.readline()
		path = line.split(" ")[0]
		path = "." + path[14:]
		img = cv2.imread(path)

		for rec in line.split(" ")[1:]:
			x1,y1,x2,y2,c = map(int,rec.split(","))
			img = cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)

		_, file = os.path.split(path)
		cv2.imshow(file, img)
		key = cv2.waitKey(0)  
		if key == 27:
			break
		cv2.destroyAllWindows()  
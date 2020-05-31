import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
	ret,frame = cap.read(0)
	mod = cv2.flip(frame, 0)
	cv2.rectangle(mod,(100,100), (200,200), (0,0,255),2) 
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(mod,'Lmao', (150,150), font, 4, (0,0,255), 3, cv2.FILLED)
	cv2.imshow('our frame',mod)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

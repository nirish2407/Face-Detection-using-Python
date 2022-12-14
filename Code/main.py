import cv2
import numpy as np
import Tkinter
import tkFileDialog

def detect_face_static():

	Tkinter.Tk().withdraw() # Close the root window
	in_path = tkFileDialog.askopenfilename()

	img = cv2.imread(in_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in face_rects:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

	while(1):

		cv2.imshow('Face Detector', img)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cv2.destroyAllWindows()

def detect_eyes_static():

	Tkinter.Tk().withdraw() # Close the root window
	in_path = tkFileDialog.askopenfilename()

	img = cv2.imread(in_path)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
        	roi_gray = gray[y:y+h, x:x+w]
        	roi_color = img[y:y+h, x:x+w]

	eyes = eye_cascade.detectMultiScale(roi_gray)

	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	while(1):

		cv2.imshow('Eye Detector', img)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cv2.destroyAllWindows()

def detect_nose_static():

	Tkinter.Tk().withdraw() # Close the root window
	in_path = tkFileDialog.askopenfilename()

	img = cv2.imread(in_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in nose_rects:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

	while(1):

		cv2.imshow('Nose Detector', img)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cv2.destroyAllWindows()

def detect_ears_static():

	Tkinter.Tk().withdraw() # Close the root window
    	in_path = tkFileDialog.askopenfilename()

	img = cv2.imread(in_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	left_ear = left_ear_cascade.detectMultiScale(gray, 1.3, 5)
	right_ear = right_ear_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in left_ear:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

	for (x,y,w,h) in right_ear:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

	while(1):

		cv2.imshow('Ear Detector', img)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cv2.destroyAllWindows()

def detect_face_video(type):

	if(type=="video_file"):

		Tkinter.Tk().withdraw() # Close the root window
		in_path = tkFileDialog.askopenfilename()

		cap=cv2.VideoCapture(in_path)

	if(type=="camera"):

		cap = cv2.VideoCapture(0)

	while True:
	
		ret, frame = cap.read()

		if(ret==False):
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in face_rects:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
	
		cv2.imshow('Face Detector', frame)
	
		c = cv2.waitKey(1)
		if c == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

def detect_eyes_video(type):

	if(type=="video_file"):

		Tkinter.Tk().withdraw() # Close the root window
		in_path = tkFileDialog.askopenfilename()

		cap=cv2.VideoCapture(in_path)

	if(type=="camera"):

		cap = cv2.VideoCapture(0)

	
	while True:

		ret, frame = cap.read()

		if(ret==False):
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			roi_color= frame[y:y+h, x:x+w]

			eyes = eye_cascade.detectMultiScale(roi_gray)

			for (ex,ey,ew,eh) in eyes:

				if(ey<((y+h)/4)):

					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		cv2.imshow('Eye Detector', frame)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

def detect_nose_video(type):

	if(type=="video_file"):

		Tkinter.Tk().withdraw() # Close the root window
		in_path = tkFileDialog.askopenfilename()

		cap=cv2.VideoCapture(in_path)

	if(type=="camera"):

		cap = cv2.VideoCapture(0)

	while True:

		ret, frame = cap.read()

		if(ret==False):
			break
		
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			roi_color= frame[y:y+h, x:x+w]

			nose_rects = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)

			for (x,y,w,h) in nose_rects:
				cv2.rectangle(roi_color, (x,y), (x+w,y+h), (0,255,0), 3)

		cv2.imshow('Nose Detector', frame)

		c = cv2.waitKey(1)
		if c == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

def detect_ears_video(type):

	if(type=="video_file"):

		Tkinter.Tk().withdraw() # Close the root window
		in_path = tkFileDialog.askopenfilename()

		cap=cv2.VideoCapture(in_path)

	if(type=="camera"):

		cap = cv2.VideoCapture(0)

	while True:

		ret, frame = cap.read()

		if(ret==False):
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		left_ear = left_ear_cascade.detectMultiScale(gray, 1.3, 5)
		right_ear = right_ear_cascade.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in left_ear:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

		for (x,y,w,h) in right_ear:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)

		cv2.imshow('Ear Detector', frame)

		c = cv2.waitKey(1)
	
		if c == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
left_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')

if face_cascade.empty():
	raise IOError('Unable to load the haarcascade_frontalface_alt xml file')

if eye_cascade.empty():
	raise IOError('Unable to load the eye cascade classifier xml file')

if nose_cascade.empty():
	raise IOError('Unable to load the nose cascade classifier xml file')

if left_ear_cascade.empty():
	raise IOError('Unable to load the left ear cascade classifier xml file')

if right_ear_cascade.empty():
	raise IOError('Unable to load the right ear cascade classifier xml file')

choice=0

while(choice!=4):

	choice1=0
	choice2=0
	choice3=0

	print "******Main Menu******\n"
	print "1. Detect face from static image"
	print "2. Detect face from video"
	print "3. Detect face from live video capture"
	print "4. Exit\n";

	choice=input("Enter your choice ")

	if(choice==1):

		while(choice1!=5):

			print "\n*****Static Image Menu*****"
			print "1. Detect Face"
			print "2. Detect Eyes"
			print "3. Detect Nose"
			print "4. Detect Ears"
			print "5. Exit\n"

			choice1=input("Enter your choice ")

			if(choice1==1):
				detect_face_static()

			elif(choice1==2):
				detect_eyes_static()

			elif(choice1==3):
				detect_nose_static()	
		
			elif(choice1==4):
				detect_ears_static()

			elif(choice1==5):
				print "Exiting"

			else:
				print "Invalid Choice"

	elif(choice==2):
		
		while(choice2!=5):

			print "\n*****Video Menu*****"
			print "1. Detect Face"
			print "2. Detect Eyes"
			print "3. Detect Nose"
			print "4. Detect Ears"
			print "5. Exit\n"

			choice2=input("Enter your choice ")

			if(choice2==1):
				detect_face_video("video_file")

			elif(choice2==2):
				detect_eyes_video("video_file")

			elif(choice2==3):
				detect_nose_video("video_file")	
		
			elif(choice2==4):
				detect_ears_video("video_file")

			elif(choice2==5):
				print "Exiting"

			else:
				print "Invalid Choice"

			
		 
		

	elif(choice==3):
		
		while(choice3!=5):

			print "\n*****Live Video Capture Menu*****"
			print "1. Detect Face"
			print "2. Detect Eyes"
			print "3. Detect Nose"
			print "4. Detect Ears"
			print "5. Exit\n"

			choice3=input("Enter your choice ")

			if(choice3==1):
				detect_face_video("camera")

			elif(choice3==2):
				detect_eyes_video("camera")

			elif(choice3==3):
				detect_nose_video("camera")	
		
			elif(choice3==4):
				detect_ears_video("camera")

			elif(choice3==5):
				print "Exiting"

			else:
				print "Invalid Choice"

	elif(choice==4):

		print "Thanks for using the application."

	else:

		print"Invalid Choice\n"






import cv2,glob

all_images=glob.glob("*.jpg")

detect=cv2.CascadeClassifier("fd.xml")

for image in all_images:
    image=cv2.imread(image)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces= detect.detectMultiScale(gray,1.1,5)


    for (x,y,w,h) in faces:
        final=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    

    cv2.imshow("Feel",final)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    






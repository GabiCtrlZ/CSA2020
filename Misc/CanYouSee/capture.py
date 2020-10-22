import cv2

# Opens the Video file and converts to binary
cap = cv2.VideoCapture('Can_You_See_It.mp4')
out = ''
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    b = int(frame[0][0][0])
    if b > 200:
      out += '1'
    elif b < 50:
      out += '0'
    
f = open("outfile.txt", "a")
f.write(out)
f.close()


cap.release()
cv2.destroyAllWindows()

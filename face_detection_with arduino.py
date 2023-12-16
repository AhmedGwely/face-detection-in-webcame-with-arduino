import cv2
import os
import argparse
import mediapipe as mp
import controler as cnt
#--- Read image
output_dir = os.path.join(".","output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cnt.led(0)


def face_detector_img_prossing(img,face_detection):
    
    H, W, channals = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb) # output alot of data like the bonding box and the score etc
    #print(out.detections)
    #if out.detections have an image that has no human face it will output None then it will out an error for .....
    #iteration in the next (for) - so we should make an if statment
    b = 0
    if out.detections is not None :
        b = 1
        
        for detection in out.detections :
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h = bbox.xmin , bbox.ymin, bbox.width, bbox.height #the numbers is relative numbers

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)
#--- Blur Face

            #img[y1: y1 + h,x1:x1 + w ,:] = cv2.blur(img[y1: y1 + h,x1:x1 + w ,:] ,(30,30))
            detected_img = cv2.rectangle(img,(x1,y1),(x1 + w, y1 + h),(0,255,0),6)
    return [b, img]





args = argparse.ArgumentParser()
args.add_argument("--mode",default='webcam')
args.add_argument("--filepath",default=r"E:\opencv\projects\face_anonymizer\billie.mp4")

args = args.parse_args()



#print(img.shape)
#--- Detect The Face
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:

    if args.mode in ['image']:
       img = cv2.imread(args.filepath)

       H, W, channals = img.shape  # return tuple (h , w , channal)

       img = face_detector_img_prossing(img,face_detection)

       cv2.imwrite(os.path.join(output_dir,"first_img.png"),img)
    elif args.mode in ['video'] :

        video = cv2.VideoCapture(args.filepath)
        st, frame = video.read()  #reaf only first frame .
        fbs = int(video.get(cv2.CAP_PROP_FPS))

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'MP4V'),
                                       fbs,
                                       (frame.shape[1], frame.shape[0]))

        while st:
            
            frame = face_detector_img_prossing(frame,face_detection)
            output_video.write(frame)
            st,frame = video.read() # to itrate the frames

        video.release()
        cv2.destroyAllWindows()
    elif args.mode in ['webcam']:

        cap = cv2.VideoCapture(1)
        fbs = int(cap.get(cv2.CAP_PROP_FPS))

        ret, frame = cap.read()

        while ret:
            boo, frame = face_detector_img_prossing(frame, face_detection)
            if boo == 1:
                cnt.led(1)
            else:
                cnt.led(0)
            #print(boo)
            cv2.imshow('frame', frame)
            if cv2.waitKey(30) & 0xFF == ord("x"):
                break


            ret, frame = cap.read()

        cap.release()
        cv2.destroyAllWindows()

         

cnt.led(0)

cv2.waitKey(0)


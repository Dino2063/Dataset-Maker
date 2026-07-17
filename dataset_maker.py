from pathlib import Path
import cv2
import time
import random
import string

#initialization
vid=cv2.VideoCapture(0)
p1= (170, 90)  #coord for rectangular frame
p2 = (470, 390)
counting_down=False #for image capture timedown

#resolution of webcam=(640, 480)

print("Welcome to dataset maker.Here u will have option to store images for n classes as per ur liking")
num_of_classes=int(input("Enter the number of class u would like to create\n"))
name_of_classes=[]
folder_path=Path("Webcam_recog")
format_inp=input("Which format would u like to store ur images in?Eg:jpg,png,webp....\n").lower()
image_structure=input("Which type of img would u like to save? eg: Type (G or g for gray scale) or Type (R or r for BGR scale)\n")


for i in range(num_of_classes):
   image_count=0

   name=input("Whts the name of class:"+str(i+1)+"\n")
   name_of_classes.append(name)
   class_path=folder_path/name
   class_path.mkdir(parents=True,exist_ok=True)

   print("Before we begin, there will be a gap of 5 seconds for each image pic taken and will be stored in ur respective directory.Press q or Q when ur done with ur photo count\nThis program will continously depict the number of images saved and make sure to show ur exact posture inside the rectangle border")



   start=time.time()
   while True:
      cond,frame=vid.read()
      if not cond:
         break

      if image_structure=='g' or image_structure =='G':
         frame_coloring=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      elif image_structure=='r' or image_structure=='R':
         frame_coloring=frame  #no need to change since the actual frame is already in BGR
      else:
         print("Sorry u entered the wrong key, We need to restart the process")
         break

      display_frame = frame_coloring.copy()   #to prevent timer being printed while saving
      cropped=frame_coloring[p1[1]:p2[1],p1[0]:p2[0]]

      cv2.putText(display_frame,
                     "Image_count:"+str(image_count),
                     (350,40),
                     cv2.FONT_HERSHEY_COMPLEX,
                     1,
                     (255,0,0),
                     1)

      if counting_down:
         end=time.time()
         timer=round(2.5-(end-start),2)
         cv2.putText(display_frame,
                    "Timer:"+str(timer),
                    (10,40),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255,0,0),
                    1)
       
         if end-start >= 2.5:
            random_file_name=''.join(random.choices(string.ascii_lowercase,k=5))  #millions possibility per class, so dont worry
            image_path=random_file_name+("."+format_inp)
            file_path=class_path/image_path
            print(file_path)
            save_conditon=cv2.imwrite(file_path,cropped)
            if save_conditon:
               print("Successfully saved")
               image_count+=1
            else:
               print("Image saving failed")
            
            counting_down=False


 
      cv2.rectangle(display_frame,p1,p2,(0,255,0),2)
      cv2.imshow("webcam",display_frame)
      cv2.imshow("zoomed_in",cropped)
      key = chr(cv2.waitKey(1) & 0xFF).lower()

      if key == 'q':
         cv2.destroyAllWindows()
         break
        
      if key == 'z':
         start=time.time()
         counting_down=True

   continue_choice=input("Your photoshoot of class"+str(i+1)+"has been completed\n"+"If u would like to continue ur photoshoot for other classes, (type C or c) or If u would like to end this for now, (type Z or z)\n")

   if continue_choice=='c' or continue_choice=='C':
      pass
   elif continue_choice=='Z' or continue_choice=='z':
      print("Operation ended")
      break

   else:
      print("Invalid key")
      print("Operation ended")
      break

vid.release()
cv2.destroyAllWindows()










    






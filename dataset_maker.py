from pathlib import Path
import cv2
import time as timer
import random
import string

#initialization
vid=cv2.VideoCapture(0)
p1= (170, 90)  #coord for rectangular frame
p2 = (470, 390)
counting_down=False #for image capture timedown

#resolution of webcam=(640, 480)

print("Welcome to dataset maker.Here u will have option to store images for n classes as per ur liking")
acceptable_formats=["jpg","webp","jpeg","png"]
while True:
    
    try:    
        num_of_classes=int(input("Enter the number of class u would like to create\n"))
    except ValueError:
        print("Error:")
        print("Please enter a number")  
        continue
    
    folder_path=Path("Webcam_recog")
    format_inp=input("Which format would u like to store ur images in?Eg:jpg,png,webp....\n").lower()
    if not format_inp.lower() in acceptable_formats:
        print("Sorry, this format is not an acceptable one. Redo the process\n")
        continue
    
    image_structure=input("Which type of img would u like to save? eg: Type (G or g for gray scale) or Type (R or r for BGR scale)\n")
    break












name_of_classes=[]
for i in range(num_of_classes):


   name=input("Whts the name of class:"+str(i+1)+"\n")
   name_of_classes.append(name)
   class_path=folder_path/name
   class_path.mkdir(parents=True,exist_ok=True)
   
   print("Instructionsssssssssssss \n")
   print("----------------------------")
   print("\n")

   print("Before we begin,\n This program captures 20 frames per Z click,and the images captured will automatically be stored in ur respective directory.\nPress q or Q when ur done with ur photo count\nThis program will continously depict the number of images saved and make sure to show ur exact posture inside the rectangle border")
   print("Make sure to click on the main window/webcam window or the big screen once to intitialize ur start")
   print("\n")
   print("------------------------------------")



   total_image_count=0   #total image count per class
   while True:
      cond,frame=vid.read()
      if not cond:
         break
     
     
      #image in either bgr or gray scale
      if image_structure=='g' or image_structure =='G':
         frame_coloring=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      elif image_structure=='r' or image_structure=='R':
         frame_coloring=frame  #no need to change since the actual frame is already in BGR
      else:
         print("Sorry u entered the wrong key, We need to restart the process")
         break

      cropped=frame_coloring[p1[1]:p2[1],p1[0]:p2[0]]

      cv2.putText(frame_coloring,
                     "Image_count:"+str(total_image_count),
                     (350,40),
                     cv2.FONT_HERSHEY_COMPLEX,
                     1,
                     (255,0,0),
                     1) #to show total image count per class

      if counting_down:
        end=timer.time()
        countdown=round((end-start),2)    
        cv2.putText(frame_coloring,
                    "Timer:"+str(countdown),
                    (10,40),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255,0,0),
                    1) # to show the time passed per 20 frames
        random_file_name=''.join(random.choices(string.ascii_lowercase,k=5))  #millions possibility per class, so dont worry
        image_path=random_file_name+("."+format_inp) # create image path
        file_path=class_path/image_path
        print(file_path)
        save_conditon=cv2.imwrite(file_path,cropped)
        if save_conditon:
            print("Successfully saved")
            total_image_count+=1
            frame_count+=1
        else:
            print("Image saving failed")
       
        if frame_count==20:   
            counting_down=False


 
      cv2.rectangle(frame_coloring,p1,p2,(0,255,0),2)
      cv2.imshow("zoomed_in",cropped)
      cv2.imshow("webcam",frame_coloring)
      
      key = chr(cv2.waitKey(1) & 0xFF).lower()

      if key == 'q':
          
         cv2.destroyAllWindows()
         break
        
      elif key == 'z':
         frame_count=0
         start=timer.time()
         counting_down=True
      
      else:
         pass
   
   if num_of_classes==1: #because this only runs when one class photoshoot is complete. And if the user only requested one class then theres no point in going through the trouble of asking if he wants to continue
       break

   continue_choice=input("Your photoshoot of class"+str(i+1)+"has been completed\n"+"If u would like to continue ur photoshoot for other classes, (type C or c) or If u would like to end this for now, (type Z or z)\n")

   if continue_choice.lower()=='c':
      pass
   elif continue_choice.lower()== 'z':
      print("Operation ended")
      break

   else:
      print("Invalid key")
      print("Operation ended")
      break

vid.release()
cv2.destroyAllWindows()








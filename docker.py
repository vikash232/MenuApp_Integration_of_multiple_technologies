import speech_recognition as sr
import os
import pyttsx3

pyttsx3.speak("hello vikash... welcome to your Terminal.. I am your voice assistent. please tell how may i help you...")
print("\t\t\t hey vikash welcome to my TUI that makes life simple") 



r = sr.Recognizer()

while True:
 with sr.Microphone() as source:
  pyttsx3.speak("start saying")
  print("start saying ..")
  audio = r.listen(source)
  pyttsx3.speak("I got it , plz wait ...")
  print("I got it , Please wait ...")

  ch = r.recognize_google(audio)
  print(ch)

  if (("how" in ch) and ("can"  in ch)):
   pyttsx3.speak("I have following options for you")
   print("\t\t\tI have following options for you")

   pyttsx3.speak("I can install docker")
   print("\t\t\tI can install docker")

   pyttsx3.speak("I can start docker-service")
   print("\t\t\tI can start docker-service")
  
   pyttsx3.speak("I can search docker images")
   print("\t\t\tI can search docker images")

   pyttsx3.speak("I can pull docker images")
   print("\t\t\tI can pull docker images")

   pyttsx3.speak("I can show you available docker images")
   print("\t\t\tI can show you available docker images")
   
   pyttsx3.speak("I can launch docker os for you")
   print("\t\t\tI can launch docker os for you")
   
   pyttsx3.speak("I can show you running docker os")
   print("\t\t\tI can show you running docker os")

   pyttsx3.speak("I can run commands in docker os")
   print("\t\t\tI can run commands in docker os")

   pyttsx3.speak("I can stop docker os")
   print("\t\t\tI can stop docker os")

   pyttsx3.speak("I can start docker os")
   print("\t\t\tI can start docker os") 

   pyttsx3.speak("I can delete docker os")
   print("\t\t\tI can delete docker os")

   pyttsx3.speak("I can delete docker images")
   print("\t\t\tI can delete docker images")

  elif (("install" in ch) or ("Install" in ch)) and (("docker services" in ch) or ("Docker service" in ch) or ("docker" in ch)):
         pyttsx3.speak("Starting docker services for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo systemctl start docker"')


  elif (("start" in ch)) and (("Docker services" in ch) or ("docker service" in ch) or ("docker" in ch)):
         pyttsx3.speak("Starting docker services for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo systemctl start docker"')

  elif (("search" in ch)) and (("docker images" in ch) or ("Docker images" in ch) or ("dockerimages" in ch)):
         print("Write docker image name :- " , end='')
         imagename = input()
         pyttsx3.speak("Searching docker images for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker search {}"'.format(imagename))       

  elif (("Pull" in ch) or ("pull" in ch)) and (("docker images" in ch) or ("images" in ch) or ("docker" in ch)):
         print("Write docker image name :- " , end='')
         imagename = input()
         pyttsx3.speak("Pulling docker images for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker pull {}"'.format(imagename))

  elif (("show" in ch)) and (("images" in ch)) and (("available" in ch) or ("images" in ch)  or ("docker os" in ch)):
         pyttsx3.speak("Showing available images to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker images"')

  elif (("Launch" in ch) or ("launch" in ch)) :
         print("we have following images available.....")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker images"')
         print("Write required os name for launching :- " , end='')
         OSname = input()
         pyttsx3.speak("Lauching centos in docker")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker run -itd {}"'.format(OSname))

  elif (("show" in ch)) and (("running" in ch)) and (("docker os" in ch) or ("os" in ch) or ("o s" in ch)):
         pyttsx3.speak("showing running os to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')

  elif (("show" in ch)) and (("running" in ch)) and (("docker os" in ch) or ("os" in ch) or ("o s" in ch)):
         pyttsx3.speak("showing running os to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')

  elif (("Show" in ch) or ("run" in ch)) and (("date" in ch)) and (("docker os" in ch) or ("os" in ch) or ("docker" in ch)):
         print("Choose the following OS in which you want to run a date command ...")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')
         OSname = input()
         pyttsx3.speak("showing date to you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker exec {} date"'.format(OSname))

  elif (("stop" in ch)) and (("docker os" in ch) or ("Docker os" in ch) or ("docker" in ch)):
         pyttsx3.speak("Choose the following OS in which one you want to stop ...")
         print("Choose the following OS in which one you want to stop ...")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')
         OSname = input()          
         pyttsx3.speak("Stoping docker OS for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker stop {}"'.format(OSname)) 
  
  
  elif (("start" in ch)) and (("docker os" in ch) or ("Docker os" in ch) or ("docker" in ch)):
         pyttsx3.speak("Choose the following OS in which one you want to start ...")
         print("Choose the following OS in which one you want to start ...")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')
         OSname = input()          
         pyttsx3.speak("Starting docker OS for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker start {}"'.format(OSname))

  elif (("delete" in ch)) and (("docker os" in ch) or ("Docker os" in ch) or ("docker" in ch)):
         pyttsx3.speak("Choose the following OS in which one you want to delete ...")
         print("Choose the following OS in which one you want to delete ...")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')
         OSname = input()          
         pyttsx3.speak("Deleting docker OS for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker rm -f {}"'.format(OSname))         
  
  elif (("delete" in ch)) and (("docker images" in ch) or ("Docker images" in ch) or ("images" in ch)):
         pyttsx3.speak("Choose the following image in which one you want to delete ...")
         print("Choose the following image in which one you want to delete ...")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker images"')
         OSname = input()          
         pyttsx3.speak("Deleting docker image for you")
         os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker rmi -f {}"'.format(OSname))
 
 
  elif (("close" in ch) or ("exit" in ch) or ("shoutdown" in ch)):
         pyttsx3.speak("Thankyou for using me. I am always here for you help. good bye....")
         exit()
 
  else:
         pyttsx3.speak("option not supported....Plz try again")
         print("option not supported")

  pyttsx3.speak("plz enter for continue.....")
  input("plz enter for continue.....")
  print("""         I can install docker
         I can start docker-service
         I can search docker images
         I can pull docker images
         I can show you available docker images
         I can launch docker os for you
         I can show you running docker os
         I can run commands in docker os
         I can stop docker os
         I can start docker os
         I can delete docker os
         I can delete docker images
         exit""")

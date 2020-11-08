import speech_recognition as sr
import os
import pyttsx3
import getpass
pyttsx3.speak("hello Monika... welcome Here... please tell how may i help you...")
print("hey Monika plzz tell your wanted service to run") 

r = sr.Recognizer()


while True:
 with sr.Microphone() as source:
  pyttsx3.speak("start saying")
  print("start saying ..")
  audio = r.listen(source)
  pyttsx3.speak("we got it , plz wait ...")
  print("we got it , Please wait ...")

  ch = r.recognize_google(audio)
  print(ch)

 #os.system("aws configure")
 username = input("Enter user name")
 passwd = getpass.int(input("Enter password")

 if (("how" in ch) and ("can"  in ch)):
   pyttsx3.speak("we have following options for you")
   print("we have following options for you", end="")
   print(""" launch an instance
             create a key pair
             create a security group
             create an ingress rule for security group
             create an ebs
             create s3 
             exit""")

      
   
 if ("configure" in ch):
   os.system("aws configure")  
 elif(("create" in ch) and (("generate keypair" in ch) or ("key pair" in ch):
   print("Enter a key pair name:",end = "")
   kp = input()
   os.system("aws ec2 create-key-pair --key-name {} --query "KeyMaterial" — output text > vk_key.pem”.format(kp)) 
 elif(("create" in ch) and (("generate securitygroup" in ch) or ("security group" in ch)):
   print("Enter a security group name: ",end = "")
   sgname = input()
   print("Enter a security group description : ",end = "")
   description = input()
   os.system("aws ec2 create-security-group --group-name {} --description “{}” — vpc-id vpc-de130aa4".format(sgname,description))
 elif(("create" in ch) or (("generate ingressrule" in ch) or ("ingress rule" in ch)):
   print("Enter your inbound port no.1",end='')
   portno.1 = input()
   print("Enter your inbound port no.2",end='')
   portno.2 = input()
   os.system("aws ec2 authorize-security-group-ingress — group-name vkrule — protocol tcp — port {} — cidr 0.0.0.0/0".format(portno.1))
   os.system("aws ec2 authorize-security-group-ingress — group-name vkrule — protocol tcp — port {} — cidr 0.0.0.0/0".format(portno.2))
 elif(("create" in ch) and (("createtags" in ch) or ("tags" in ch)):
   os.system("aws ec2 create-tags — resources i-0ea9eaaf6902c6e8a — tags Key=Name,Value=vk")

 elif(("launch" in ch) or ("install" in ch)) and (("instance" in ch) or ("launch instance" in ch)):
   os.system("aws ec2 run-instances --image-id ami-0947d2ba12ee1ff75 --count 1 --instance-type t2.micro --key-name vk_key --security-group-ids sg-0d1aad5f3c2cc3100 --subnet-id subnet-69df120f")
 elif(("create" in ch)) and (("ebs" in ch) or ("volume" in ch)):
   os.system("aws ec2 create-volume --availability-zone us-east-1a --volume-type gp2 --size 1")

 elif(("create" in ch)) and ("S3" in ch)) and ("Bucket" in ch)):
   bucketname = input()
   os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1".format(bucketname))

 elif (("terminate" in ch) or ("exit" in ch) or ("shoutdown" in ch)):
   exit()
   pyttsx3.speak("plz enter for continue.....")
   input("plz enter for continue.....")
 else:
         pyttsx3.speak("option not supported....Plz try again")
         print("option not supported")

 

 pyttsx3.speak("plz enter for continue.....")
 input("plz enter for continue.....")


 


 

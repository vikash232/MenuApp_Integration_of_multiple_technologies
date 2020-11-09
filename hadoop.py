import os
import getpass

print("hey welcome to my TUI that makes life simple")
print("\t\t\t--------------------------------------")

passwd = getpass.getpass("Enter your password: ")

if passwd != "redhat":
   print("Incorrect Password try again..")
   exit()

while True:
 os.system("clear")
 print("""         press 1: to start namenode
         press 2: to start datanode
         press 3: to check java running java process of namenode
         press 4: to check java running java process of datanode
         press 5: to check connected datanode from namenode
         press 7: exit""")

 print("enter your choice:- ")
 ch=input()
 if int(ch) == 1:
   os.system("hadoop-daemon.sh start namenode")
 elif int(ch) == 2:
   ip = input()
   os.system('ssh {} "hadoop-daemon.sh start datanode"'.format(ip))
 elif int(ch) == 3 :
   os.system("jps")
 elif int(ch) == 4:
   ip = input()
   os.system('ssh {} "jps"'.format(ip))
 elif int(ch) == 5 :
   os.system("hadoop dfsadmin -report")
 elif int(ch) == 6:
   exit()      
 else:
   print("option not supported")
 input("plz enter for continue.....")


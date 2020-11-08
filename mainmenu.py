import os
print("________________________________________________")
print("\n..........WELCOME.........")
print("________________________________________________")

print("\n\n.........SELECT YOUR INTREST .........")
while True:
		print("""\n 1.Hadoop
				 \n 2.AWS 
				 \n 3.Docker
				 \n 4.Linux and Networking
				 \n 5.View Team Members
				 \n 6.exit""")
		print("\n Press the No. According to your Intrest!!")
		choise = input("Enter your Choice: ")
		if(choise == "1"):
			os.system('python3 arth.py')#hadoop file
		elif(choise == "2"):
			print('hello')#AWS
		elif(choise == "3"):
			print('hello')#Docker
		elif(choise == "4"):
			print('hello')#LinuxandNetworking
		elif(choise == "5"):
			print("============")
			print("Team Members")
			print("============")
			print("""\n -> Vikash Kaushik
					\n ->Monika Poddar
					\n ->Parag Rahate
					\n ->Pooja Maurya""")
		elif(choise == "6"):
			exit()			

menu() 


#!"python.exe"
#Version Information
#Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32

#Python Library Dependencies
import os
import shutil
import sys

#Global Variable
tag_state="0";
current_tag="";

#All Function Definitions
#1. Copy Function
def f_copy(content):
	if(len(content)==7):
		source = ""+content[1].strip()+"\\"+content[5].strip()+"";
		target = ""+content[3].strip()+"";
		assert not os.path.isabs("\'"+source+"\'")
		target = os.path.join(target, "")#os.path.basename(source))
		# create the folders if not already exists
		try:
			os.makedirs(target)
		except Exception:
			pass
		# adding exception handling
		try:
			shutil.copy(source, target)
			print("Copy Successfull")
		except IOError as e:
			print("Unable to copy file. %s" % e)
		except:
			print("Unexpected error:", sys.exc_info())
	elif(len(content)<7):
		print("LOG : Missing a few Arguments")
	elif(len(content)>7):
		print("LOG : Too many Arguments")

#2. Move Function
def f_move(content):
	if(len(content)==7):
		source = ""+content[1].strip()+"\\"+content[5].strip()+"";
		target = ""+content[3].strip()+"";
		assert not os.path.isabs("\'"+source+"\'")
		target = os.path.join(target, "")#os.path.basename(source))
		# create the folders if not already exists
		try:
			os.makedirs(target)
		except Exception:
			pass
		# adding exception handling
		try:
			shutil.move(source, target)
			print("Move Successfull")
		except IOError as e:
			print("Unable to copy file. %s" % e)
		except:
			print("Unexpected error:", sys.exc_info())
	elif(len(content)<7):
		print("LOG : Missing a few Arguments")
	elif(len(content)>7):
		print("LOG : Too many Arguments")

#3. Move Directory Function
def f_mvdir(content):
	if(len(content)==5):
		source = ""+content[1].strip()+"";
		target = ""+content[3].strip()+"";
		assert not os.path.isabs("\'"+source+"\'")
		target = os.path.join(target, "")#os.path.basename(source))
		# create the folders if not already exists
		try:
			os.makedirs(target)
		except Exception:
			pass
		# adding exception handling
		try:
			shutil.move(source, target)
			print("Move Directory Successfull")
		except IOError as e:
			print("Unable to copy file. %s" % e)
		except:
			print("Unexpected error:", sys.exc_info())
	elif(len(content)<5):
		print("LOG : Missing a few Arguments")
	elif(len(content)>5):
		print("LOG : Too many Arguments")

#4. Delete File Function
def f_del(content):
	if(len(content)==3):
		dest = ""+content[1].strip()+"";
		assert not os.path.isabs("\'"+dest+"\'")
		if os.path.exists(dest):
			os.remove(dest)
			print("1 File Deleted")
		else:
			print("File not found. No File Deleted")
	elif(len(content)<3):
		print("LOG : Missing a few Arguments")
	elif(len(content)>3):
		print("LOG : Too many Arguments")

#5. Delete Folder/Remove Directory Function
def f_rmdir(content):
	if(len(content)==3):
		dest = ""+content[1].strip()+"";
		assert not os.path.isabs("\'"+dest+"\'")
		if os.path.exists(dest):
			os.rmdir(dest)
			print("Directory Deleted")
		else:
			print("Directory not found. No Directory Deleted")
	elif(len(content)<3):
		print("LOG : Missing a few Arguments")
	elif(len(content)>3):
		print("LOG : Too many Arguments")

#6. Main Function Chooser !!!Important
def main_switcher(content,line):
	global tag_state
	#print(content)
	#print("2>>"+tag_state)
	
	if(content[0]!=""):
		if(content[0].lower()=="copy" and (tag_state=="0" or tag_state=="2")):
			print(line)
			f_copy(content)
		elif(content[0].lower()=="move" and (tag_state=="0" or tag_state=="2")):
			print(line)
			f_move(content)
		elif(content[0].lower()=="mvdir" and (tag_state=="0" or tag_state=="2")):
			print(line)
			f_mvdir(content)
		elif(content[0].lower()=="del" and (tag_state=="0" or tag_state=="2")):
			print(line)
			f_del(content)
		elif(content[0].lower()=="rmdir" and (tag_state=="0" or tag_state=="2")):
			print(line)
			f_rmdir(content)
		elif(len(content)==1 and tag_state=="0"):
			#for arg in range(len(sys.argv)):
			if(len(content)==1 and len(sys.argv)<=2):	
				tag_state="1"
				#print(list(content[0])[0])
			#elif(len(content)==1 and len(sys.argv)>2):
			#	for tag in sys.argv:
			#		if(tag==content[0]):
			#			print(tag)
			#			tag_state="1"
		elif(list(content[0])[0]==":" and (tag_state=="1" or tag_state=="2")):
			#print(line)
			#print("3>>"+tag_state)
			line=line.replace(':', '', 1)
			line=line.strip()
			content=line.split("\"")
			content[0]=content[0].strip(" ")
			#print(">>>"+content)
			tag_state="2"
			main_switcher(content,line)
			
			
#PROGRAM STARTS HERE - Main
if(len(sys.argv)>1):
	f=open("Playbooks\\"+sys.argv[1],"r+");
	data=f.readlines();
	f.close();

	for line in data:
		line=line.strip()
		if(line==""):
			continue
		elif(list(line)[0]=="-"):
			current_tag=line
		if(line==""):
			continue
		elif(len(sys.argv)<=2):
			line=line.strip()
			content=line.split("\"")
			content[0]=content[0].strip(" ")
			#print(tag_state)
			#print(list(content[0]))
			if(len(list(content[0]))<1):
				continue
			if(list(content[0])[0]!=":"):
				tag_state="0"
			main_switcher(content,line)
		elif(len(sys.argv)>2):
			line=line.strip()
			if(line==""):
				continue
			content=line.split("\"")
			content[0]=content[0].strip(" ")
			for tag in sys.argv:
				if(tag==line):
					print(tag)
					tag_state="1"
					current_tag=tag;
				elif(list(content[0])[0]==":" and current_tag==tag):
					#print("1>>"+tag_state)
					#print(list(content[0]))
					tag_state="2"
					main_switcher(content,line)
					break
				elif(list(content[0])[0]!=":"):
					#print("ll")
					tag_state="0"
		
		#print(line);
		#print(len(sys.argv))
elif(len(sys.argv)<=1):
	print("ERROR : Missing a few Arguments or No Playbook Selected")
					
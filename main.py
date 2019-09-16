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

#Global Variables for Folder Compare
source_a_f=[]
source_a_d=[]
target_a_f=[]
target_a_d=[]
cmp_state="0"

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

#6. Directory/Folder Comparison Utility Source and Target
def source(s):
	global source_a_f, source_a_d, target_a_f, target_a_d
	for root, d_names, f_names in os.walk(s):
		for f_name in f_names:
			source_a_f.append(f_name)
		for d_name in d_names:
			source_a_d.append(d_name)

def target(t):
	global source_a_f, source_a_d, target_a_f, target_a_d
	for root, d_names, f_names in os.walk(t):
		for f_name in f_names:
			target_a_f.append(f_name)
		for d_name in d_names:
			target_a_d.append(d_name)
			
#7. Directory/Folder Comparison Utility Main Unit
def compare_s_t(s,t,l):
	global cmp_state, source_a_f, source_a_d, target_a_f, target_a_d
	source(s)
	target(t)
	#if(source_a_f==target_a_f and source_a_d==target_a_d):
	#	print("True")
	#if(set(source_a_f)==set(target_a_f) and set(source_a_d)==set(target_a_d)):
	#	print("True")
	statement_1="Total "+str(len(set(source_a_d).difference(target_a_d))+len(set(target_a_d).difference(source_a_d)))+" folders and "+str(len(set(source_a_f).difference(target_a_f))+len(set(target_a_f).difference(source_a_f)))+" files are unique."
	statement_2=str(len(set(source_a_d).difference(target_a_d)))+" folders and "+str(len(set(source_a_f).difference(target_a_f)))+" files from path : "+s
	statement_3=str(len(set(target_a_d).difference(source_a_d)))+" folders and "+str(len(set(target_a_f).difference(source_a_f)))+" files from path : "+t
	if(l!=""):
		f=open(l,"w+")
		f.close()
		f=open(l,"a+")
		f.write(statement_1+"\n"+statement_2+"\n"+statement_3+"\n\n1. Path : "+s+"\n\n")
		for udi_p1 in set(source_a_d).difference(target_a_d):
			f.write("Directory: "+udi_p1+"\n")
		for ufi_p1 in set(source_a_f).difference(target_a_f):
			f.write("File: "+ufi_p1+"\n")
		f.write("\n\n2. Path : "+t+"\n\n")
		for udi_p2 in set(target_a_d).difference(source_a_d):
			f.write("Directory: "+udi_p2+"\n")
		for ufi_p2 in set(target_a_f).difference(source_a_f):
			f.write("File: "+ufi_p2+"\n")
		f.close()
		
		
	print(statement_1)
	print(statement_2)
	print(statement_3)
	cmp_state="0"

#8. Delete Folder/ Directory Content Compare Function without log file
def f_cmp_logless(content):
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
			compare_s_t(source,target, "")
			print("Comparison Successfull")
		except IOError as e:
			print("Unable to compare. %s" % e)
		except:
			print("Unexpected error:", sys.exc_info())
	elif(len(content)<5):
		print("LOG : Missing a few Arguments")
	elif(len(content)>5):
		print("LOG : Too many Arguments")

#9. Delete Folder/ Directory Content Compare Function with log file
def f_cmp_wlog(content):
	if(len(content)==7):
		source = ""+content[1].strip()+"";
		target = ""+content[3].strip()+"";
		log_file= ""+content[5].strip()+"";
		assert not os.path.isabs("\'"+source+"\'")
		target = os.path.join(target, "")#os.path.basename(source))
		# create the folders if not already exists
		try:
			os.makedirs(target)
		except Exception:
			pass
		# adding exception handling
		try:
			compare_s_t(source,target,log_file)
			print("Comparison Successfull")
		except IOError as e:
			print("Unable to compare. %s" % e)
		except:
			print("Unexpected error:", sys.exc_info())
	elif(len(content)<7):
		print("LOG : Missing a few Arguments")
	elif(len(content)>7):
		print("LOG : Too many Arguments")

#10. Main Function Chooser !!!Important
def main_switcher(content,line):
	global tag_state, cmp_state
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
		elif(content[0].lower()=="cmp" and (tag_state=="0" or tag_state=="2")):
			if(len(content)==5 and cmp_state=="0"):	
				cmp_state="1"
				f_cmp_logless(content)
			elif(len(content)==7 and cmp_state=="0"):	
				cmp_state="1"
				f_cmp_wlog(content)
		elif(len(content)==1 and tag_state=="0"):
			if(len(content)==1 and len(sys.argv)<=2):	
				tag_state="1"
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
					
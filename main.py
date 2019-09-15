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
source_list=[]
target_list=[]
final_list=[]
folder_count=0
file_count=0
s_file_count=0
s_folder_count=0
t_file_count=0
t_folder_count=0
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

#6. Directory/Folder Comparison Utility child part
def source_target_cmp(source,target,state):
	global source_list, target_list
	s_t_match="0"
	for root_1, dirs_1, files_1 in os.walk(source):
		for file_s in files_1:
			#print(file_1)
			for root_2, dirs_2, files_2 in os.walk(target):
				for file_t in files_2:
					if(file_s==file_t):
						#print(file_s)
						s_t_match="1"
						break
				if(s_t_match=="0"):
					#print("$$"+file_s)
					if(state=="0"):
						source_list.append("$$"+file_s)
					elif(state=="1"):
						target_list.append("$$"+file_s)
					#s_t_match="0"
					break
				elif(s_t_match=="1"):
					s_t_match="0"
					break
		for dir_s in dirs_1:
			#print(dir)
			for root_2, dirs_2, files_2 in os.walk(target):
				for dir_t in dirs_2:
					if(dir_s==dir_t):
						#print(dir_s)
						s_t_match="1"
						break
				if(s_t_match=="0"):
					#print(">>"+dir_s)
					if(state=="0"):
						source_list.append(">>"+dir_s)
					elif(state=="1"):
						target_list.append(">>"+dir_s)
					#s_t_match="0"
					break
				elif(s_t_match=="1"):
					s_t_match="0"
					break

#7. Directory/Folder Comparison Utility Main Unit
def directory_content_comparison(s,t,l):			
	global cmp_state, source_list, target_list, final_list, folder_count, file_count, s_file_count, s_folder_count, t_file_count, t_folder_count
	source=s
	target=t
	try:
		if(l!=""):
			f=open(l,"w+")
			f.close()
	except Exception:
		pass

	source_target_cmp(source,target,"0")
	#print("========================================")
	source_target_cmp(target,source,"1")
	#print("****************************************")

	for pos_x in range(len(source_list)):
		for pos_y in range(len(target_list)):
			if(source_list[pos_x]==target_list[pos_y]):
				source_list.pop(pos_x)
				target_list.pop(pos_y)
				break
	try:
		if(l!=""):
			f=open(l,"a+")
			f.write("1. Path : "+source+"\n\n")
			f.close()
	except Exception:
		pass
		
	for s_unit in source_list:
		final_list.append(s_unit)
		try:
			if(l!=""):
				f=open(l,"a+")
				if(list(s_unit)[0]=="$" and list(s_unit)[1]=="$"):
					f.write("File: "+s_unit.replace('$', '', 2)+"\n")
				elif(list(s_unit)[0]==">" and list(s_unit)[1]==">"):
					f.write("Directory: "+s_unit.replace('>', '', 2)+"\n")
				f.close()
		except Exception:
			pass
		if(list(s_unit)[0]=="$" and list(s_unit)[1]=="$"):
			s_file_count=s_file_count+1;
		elif(list(s_unit)[0]==">" and list(s_unit)[1]==">"):
			s_folder_count=s_folder_count+1;

	try:
		if(l!=""):
			f=open(l,"a+")
			f.write("\n\n2. Path : "+target+"\n\n")
			f.close()
	except Exception:
		pass

	for t_unit in target_list:
		final_list.append(t_unit)
		try:
			if(l!=""):
				f=open(l,"a+")
				if(list(t_unit)[0]=="$" and list(t_unit)[1]=="$"):
					f.write("File: "+t_unit.replace('$', '', 2)+"\n")
				elif(list(t_unit)[0]==">" and list(t_unit)[1]==">"):
					f.write("Directory: "+t_unit.replace('>', '', 2)+"\n")
				f.close()
		except Exception:
			pass
		if(list(t_unit)[0]=="$" and list(t_unit)[1]=="$"):
			t_file_count=t_file_count+1;
		elif(list(t_unit)[0]==">" and list(t_unit)[1]==">"):
			t_folder_count=t_folder_count+1;

	for fl in final_list:
		#print(fl)
		if(list(fl)[0]=="$" and list(fl)[1]=="$"):
			file_count=file_count+1;
		elif(list(fl)[0]==">" and list(fl)[1]==">"):
			folder_count=folder_count+1;

	content_1="Total "+str(folder_count)+" folders and "+str(file_count)+" files are unique."
	content_2=str(s_folder_count)+" folders and "+str(s_file_count)+" files from path : "+source
	content_3=str(t_folder_count)+" folders and "+str(t_file_count)+" files from path : "+target
	try:
		if(l!=""):
			f=open(l,"r")
			data=f.read()
			f.close()
			f=open(l,"w+")
			f.write(content_1+"\n"+content_2+"\n"+content_3+"\n\n"+data)
			f.close()
	except Exception:
		pass

	print("Total "+str(folder_count)+" folders and "+str(file_count)+" files are unique.")
	print(str(s_folder_count)+" folders and "+str(s_file_count)+" files from path : "+source)
	print(str(t_folder_count)+" folders and "+str(t_file_count)+" files from path : "+target)
	source_list=[]
	target_list=[]
	final_list=[]
	folder_count=0
	file_count=0
	s_file_count=0
	s_folder_count=0
	t_file_count=0
	t_folder_count=0
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
			directory_content_comparison(source,target, "")
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
			directory_content_comparison(source,target,log_file)
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
					
# Rudy
Automation Tool ( Under Development )
# Rudy ~ version 1.0
* Developed using Python.
* Uses Playbooks to execute commands using RAML _(Rudy Automation Markup Language)_ script.
* Features :
  * Pre-packaged with python 3.7.4
  * Command Line Execution method :
    * \> main.py script.raml
  * All _playbooks_ need to be saved within **Playbooks** folder 
  * Basic Commands to be used inside playbooks:
    * Copy File Command :
      * RAML Syntax : 
        *  copy "source_folder_path" "destination_folder_path" "filename"
    * Move File Command :
      * RAML Syntax :
        *  move "source_folder_path" "destination_folder_path" "filename"
    * Move Directory Command :
      * RAML Syntax :
        *  mvdir "source_folder_path" "destination_folder_path" "filename"
    * Delete File Command :
      * RAML Syntax :
        *  del "filename_with_fullpath"
    * Remove Directory Command :
      * RAML Syntax :
        *  rmdir "directory_path"
  * TAG based command execution method :
    * One Playbook can have as many tags.
    * During TAG based execution only TAGs passed as command line arguments will execute.
    * Commands within TAGs are defined by concatenating a semicolon (:) as their first character.
    * Command Line Execution method :
      * \> main.py script.raml -tag_name -tag_name1 -tag_name2
    * RAML Syntax :
      > -tag_name  
      > :copy "source_folder_path" "destination_folder_path" "filename"  
      > :move "source_folder_path" "destination_folder_path" "filename"  
      > :rmdir "directory_path"  
    
    

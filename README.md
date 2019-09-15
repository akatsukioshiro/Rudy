# Rudy
Automation Tool ( Under Development )
# Rudy ~ version 1.0
* Developed using Python.
* Uses Playbooks to execute commands using RAML _(Rudy Automation Markup Language)_ script.
* Features :
  * Pre-packaged with python 3.7.4
  * Command Line Execution method :
    * __\> main.py script.raml__
  * All _playbooks_ need to be saved within **Playbooks** folder 
  * Basic Commands to be used inside playbooks:
    * Copy File Command :
      * RAML Syntax : 
        *  _copy "source_folder_path" "destination_folder_path" "filename"_
    * Move File Command :
      * RAML Syntax :
        *  _move "source_folder_path" "destination_folder_path" "filename"_
    * Move Directory Command :
      * RAML Syntax :
        *  _mvdir "source_folder_path" "destination_folder_path" "filename"_
    * Delete File Command :
      * RAML Syntax :
        *  _del "filename_with_fullpath"_
    * Remove Directory Command :
      * RAML Syntax :
        *  _rmdir "directory_path"_
    * Compare 2 Directories Command _(Unstable, IndexError noticed in some directories)_ :
      * RAML Syntax _(Basic Comparison)_ :
          *  _cmp "directory_path_1" "directory_path_2"_
      * RAML Syntax _(Comparison with detailed __log file__)_ :
          *  _cmp "directory_path_1" "directory_path_2" "log_filename_with_fullpath"_
  * TAG based command execution method :
    * One Playbook can have as many tags.
    * During TAG based execution only TAGs passed as command line arguments will execute.
    * Commands within TAGs are defined by concatenating a semicolon (:) as their first character.
    * Command Line Execution method :
      * __\> main.py script.raml -tag_name -tag_name1 -tag_name2__
    * RAML Syntax :
      > -tag_name  
      > :copy "source_folder_path" "destination_folder_path" "filename"  
      > :move "source_folder_path" "destination_folder_path" "filename"  
      > :rmdir "directory_path"  
    
    

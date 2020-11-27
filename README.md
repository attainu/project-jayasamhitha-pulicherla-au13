# JUNK FILE ORGANIZER
Basically, as a lazy programmer my desktop is full of mess and junk.
Due to the large number of files, it is a daunting task to sit and
organize each file. To make that task easy the below Python script
comes handy and all the files are organized in a well-manner within
seconds.
For using without any outside library installed, download this file and
use it
## Main functionality of this code
```
1.Organize by extension
2.Organize by size
3.Organize by Number of days
4.Re-Organize ordered file into junk file
```
### Choices appear on execution-
Depending on the Choices displayed User give desired path as first input and then choice
on the basis of choosen choice files are organized.
After Execution of program the file look like as shown in figure
Things that going to preform in the program -
```
1. Organise by extension
   by using this option user can organize their files by their file extension
   in a given folder, folder will be created according to file extension and
   finally all files will be moved to a created folder.
2. Organise by size
   by using this option user can organize their files by their file size,
   according to file sizes random folders will be created and respective
   files will be moved to them.
3. Organise by Last used/accessed date
   by using this option user can organize their files by last used date.
   random folders will be created according to files last used date and
   files will be moved to them.
4. Convert well organised file into junk file
   By using this option our organised file is converted into junk file and all
   the extra folder are get deleted.
```
### Note
If a user want junk file instead of well organised file than the
program will gone to perform that task and if user organise a file with
different type by mistake than he run the program and organise that in
there choice
### Note
if user provide wrong path than
program will ask to enter valid path for execution

### For the user who cloning the file from github
when any user who cloning the the file from github then for execution 
of the program he executes the main.py first after execution choices will
appear on the screen and on the basis of that choices the operation will 
be preformed.

#### Some important things used in project
I used many built-in libraries like- shutil for file movement,datetime to
get the date of the files,argparse for the command line parsing and
etc.
#### Further improvement:
We can design an ui for the program so a normal user can easily
interact with it. We can add more features like deleting the junk files
after a certain period of time.
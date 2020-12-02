# JUNK FILE ORGANIZER
Basically, as a lazy programmer my desktop is full of mess and junk.
Due to the large number of files, it is a daunting task to sit and
organize each file. To make that task easy the below Python script
comes handy and all the files are organized in a well-manner within
seconds.
For using without any outside library installed, download this file and
use it
## Functionality of Mycode
```
1.Organized by extension
2.Organized by size
3.Organized by Number of days
```
### Choices appear on execution-
Depending on the Choices displayed User give desired path as first input and then choice
on the basis of choosen choice files are organized.
After Execution of program the file look like as shown in figure
Things that going to preform in the program -
```
1. Organize by extension
   by using this option user can organize their files by their file extension
   in a given folder, folder will be created according to file extension and
   finally all files will be moved to a created folder.
2. Organize by size
   by using this option user can organize their files by their file size,
   according to file sizes random folders will be created and respective
   files will be moved to them.
3. Organize by Last used/accessed date
   by using this option user can organize their files by last used date.
   random folders will be created according to files last used date and
   files will be moved to them.
```
### Note
if user provide wrong path than
program will ask to enter valid path for execution

### For the user who cloning the file from github
when any user who cloning the the file from github then for execution 
of the program he executes the main.py first after execution choices will
appear on the screen and on the basis of that choices the operation will 
be preformed.

#### Some important things used in project
I used many built-in libraries like- os for file movement,datetime to
get the date of the files,argparse for the command line parsing and
etc.
#### Future improvements can be made as suchs:
We can design an ui for the program so a normal user can easily
interact with it. We can add more features like deleting the junk files
after a certain period of time.
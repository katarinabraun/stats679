# 2018-08-05, introduction 

This class will cover:  
- Rigor and reproducibility.
- Version control.    

This class will not cover:
- Specific pipelines
- R
- Stats

**We will talk a lot about documentation.**  
**Grading**, on a curve:
    10% participation
    10% peer reviews
    40% HWs
    40% final project  

## Best practice:  
1. Write code for humans. Write data for computers.
2. Don't do things manually.
3. 90% time = data cleaning. 10% time = analysis.
4. Make incremental changes. Version control.
5. Don't repeat yourself (or others).
6. Plan for mistakes = defensive coding.
7. Optimize software only after it works correctly.
8. Document design and purpose, not mechanics.
9. Collaborate.

## Introduction to the Shell  
The Shell is a programming language that is used at the terminal interface to speak to my computer.GUI vs CLI (command-line-interaface). CLI is a synonym for REPL (read-evaluate-print-loop). Everytime you click, you are not being reproducible.  
**Unix philosophy**: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface. --Doug McIlory

Commands covered today:
1. **ls** - list
2. **rm** - remove  
    Options: -r (recursively), -f (force)
3. **\*** - wildcard
4. **Echo** - repeat exactly what I entered in the command line.  
    echo $SHELL  
    /bin/bash

## Action Items  
1. Look at VS code. Do I want to use this for this course or would I rather stick with BBedit? I could also stick Xcode. For next week, make sure I am using a good text editor.  
I have VScode installed. I can use that to write/edit code. I can use bbedit to edit simple text files.
2. Look at 'good enough' practices in scientific computing.
    I downloaded this. I will add it to my bookends and post it to TCF-informatics.
3. Gary Bernhardt video - 'Unix is like a chainsaw'.  
I started watching this. However, I stopped. I don't this it's worth my time right now. I will go back to this at the end of the semester like Prof. Ane recommended.
4. Go to software carpentry introduction and do "setup" and "navigating files and directories".  
I am familiar with all of this. I also did these exercises at the actual software carpentry workshop I attended last week (last week of Aug, 2018).
5. Make sure I have a GitHub account. Figure out if I should use gmail or wisc.  
**Username = katarainabraun. Linked email = kmbraun2@gmail.com**
6. I set up and configured Git. 

# 2018-09-10, pipes and filters, configuring Git on my laptop

Notes from SW Carpentry Pipes and Filters:
- Using '>' overwrites files. Using '>>' appends the string to a file if it already exists.
- Pipe = '|'

This programming model is called “pipes and filters”. We’ve already seen pipes; a filter is a program like wc or sort that transforms a stream of input into a stream of output. Almost all of the standard Unix tools can work this way: unless told to do otherwise, they read from standard input, do something with what they’ve read, and write to standard output.

- uniq removes adjacent duplicated lines from its input.
- cat displays the contents of its inputs.
- head displays the first 10 lines of its input.
- tail displays the last 10 lines of its input.
- sort sorts its inputs.
- wc counts lines, words, and characters in its inputs.
- command > file redirects a command’s output to a file.
- first | second is a pipeline: the output of the first command is used as the input to the second.
- jobs to see the list of jobs
- & added at the end of a command to run it in the background, and get the shell back to do other things
- ps to see the list of current processes PID = process ID
- kill to send a signal to a process: like to kill it (signal 9). man kill to see other signals. kill -9 12167 to kill process # 12167.
- top to see all processes, refreshed, shows CPU and memory consumption.

**The best way to use the shell is to use pipes to combine simple single-purpose programs (filters).** :sparkles:

Save bash scripts with file extension .sh.  
Run bash scripts by typing << bash myscript.sh >>

# 2018-09-12, loops

*I decided to create two files in Visual Studio Code: (1) lecture_notes {this file} (2) programs_commands_scripts. Also, save small scripts as we go in this class.*  

The first assignment is due 9/17/18. Just do exercise 1 in the homework.
1. standard output
2. error output -- can use "2>" to redirect error message to a new file.
3. "&>" write output and error to some file.

- **ps** - shows me the processes that are going on. Each process should have it's own unique process number. You can kill something from -1 (weak) to -9 (strong).
- "&" at the end of a command can send a process to the background (return the prompt) automatically.

```
ps -u katbraun
```
allows you to see all list of processes that you started.

# 2018-09-17, regular expressions, grep and find 

- less - uses stream to view a datafile *(notes are already added to programs_commands_scripts)*

## Searching with regular expressions, grep, find 
**Grep** find things inside files, find content  
**Find** find files  

*Software Carpentry:* Finding Things. Pass on exercises, will do this at home. 
- find finds files with specific properties that match patterns. 
- grep selects ilnes in files that match patterns. 
- --help - is a flag supported by many bash commands, and programs that can be run from within Bash, to display more info on how to use these commands or programs. 
- man command displays the manual page for a given command. 
- $(command) inserts a command's output in place. Do a command substitution with $() to pass the list of files found to another command, like grep or wc: <grep xxx $(find yyy)>
- xargs - tells command line that you are typing 'arguments' and not file contents. 

Mac vs Linux has slightly different versions of grep.  
Mac - BSD tools. Linux - GNU tools. Mainly differ in how they treat 'extended' regular expressions.  
GNU version of linux commands are g(command). Eg ggrep, gls, gcat etc. 

Quotes with shell commands:  
```
echo \*.txt
```  
this expands the wildcard before running echo. 
```
echo "\*.txt"
```

*Single quotes are "very protective". Variables do not get replaced by their values.* 

**New lines:**
- \\n , \r

## Exercise in tb1.fasta  
Find all instances where characters are not A,C,T,G,a,c,t,g
Fist exclude the first line. Then find grep to find anything that is not ACTGactg.  
My code:  
```
grep -v ">gi|" tb1.fasta | grep -o --color [^A,C,T,G]
```

## Software carpetnry grep/find key points: 
1. ```find``` finds files with specific properties that match patterns. 
2. ```grep``` selects lines in files that match patterns. 
3. ```--help``` is a flag supported by most bash commands and programs that can be run from within Bash, to display more info on how to use these commands or programs. 
4. ```man command``` displays the manual page for a given command. 
5. ```$(command)``` insrts a command's output in place. 

# 2018-09-19, grep 

## Feedback/questions from assignment #1. 
- Use relative paths. 
- Document your work to be able to reproduce it yourself, because in 6 months you won't respond to emails.
- Readme: Run the script by going into this folder and running this command. 
- If I have questions in the future it is okay to open an issue on GitHub and tag Cora and/or Dr. Ane. 

Download partitionfinder_bestscheme.txt. Write a grep command to search through and see how many times we see GTR + G.  
```
grep -c "| GTR+G " partitionfinder_bestscheme.txt>
```  
68 (this is the correct answer) 

```
grep '^$' filename
``` 
this would show all of the blank lines. 

Examples at the end of the grep page are really tailored to exercise 2. Take a careful look at those. 
 
## Markdown format:  
\*italicized*  
\*\*bold**  
'inline code'  
<website link, URL>  
\[link text](URL to text)  
\![text]\(path/to/image.png)  
\# chapter 1 - level 1 header  
\## section 1.1 - level 2 header  
\### paragraph 1.1.1 - level 3 header 

chapter 1 
\=========  
section 1.1
\-----------

To get code blocks, indent with 4 spaces (or 8 spaces if within a list).  
Use 3 backticks, possibly followed by the language name:  
```r
foo <-function(x){x+1} # R function "foo", just adds 1
food(2)
```  
**To force a new line, end you line in 2 spaces**  

## Rendering a markdown file to other formats:   
Many online viewers will render markdown automatically, like github, box, dropbox, osf. In VS Code, click on the "preview" icon. 
We can also create new files: pdf, html, etc. 

## Project management:  
Within each project directory
- data (don't touch the raw data)
- scripts
- binaries, executable files (of other people's programs that you used)
- results/analysis 
- figures
- manuscript 

*Exercise:* write a one-liner to count the number of “Subsets” whose “Best Model” is GTR+G in this file: partitionfinder_bestscheme.txt (68 out of 95):  
```
grep -oc 'GTR+G ' partitionfinder_bestscheme.txt
``` 
(answer = 68)  
I put this file in: /Users/katbraun/Desktop/bds-files/partitionfinder_bestscheme

# 2018-09-24, github and git at the command line

Track versions of a project with git
 
## Git overview
- take snapshots of your project once in a while. one "commit" = one snapshots
- git stores changes bteween snapshopts, not the wole files
- git stores its data (chnages) in a .git directory
- each collaborator has the project on her/his local machine, and another remote copy of the project is on GitHub. Collaborators can "pull" from GitHub and "push" to GitHub

Each snapshop has an address and a comment: "commit address"  
```
git checkout "commit address"
```  
Additions are in green. Deletions are in red. 

The only file you might want to look at in .git/ is the configuration file - text file.  
```git add``` (to staging area, intermediate picture)  
```git diff``` (show me the difference between new version and staged area)  
```git diff --staged``` (show me the difference between staging area and previous commit)  git commit (send files in the staging area to repo)  
```git log --oneline``` (list of recent git activity), --pretty=oneline

## Commit messages:  
little message that you include with each commit made. These are very important when you are trying to recover previous version. 
Don't use: update, continued, new code, misc, edits. 
50 or fewer characters is strongly recommended. 
If more explanations are needed, add one blank line. Then your explanation paragraph. 
Informativeness - helps to recover old versions.   

## Separation of title vs paragraph.  
```git commit``` will open a text editor and then it's easier to see your new line  
-a option to add all changes in tracked file to the commit (combines add and commit)

## Looking at Git history:  
```git show``` (shows the actual content of the commit, actual differences, only the last commit)    

## Use git to move or delete tracked files  
git mv "old name" "new name"  
touch gitignore
- add text that I don't want to track 

## What files (not) to track / commit  
**Track:** scripts, text documentation, notebooks (jupyter)  
**Do not track:** 
- large files that can be reproduced by the pipeline
- large data files if they can be obtained from outside archive
- binary files 
- pdf and figures
- MS word documents (they are not plain text files)

### If you make a mistake: 
```echo "todo: ask sequencing center about adapters" > readme.md```  
```cat readme.md``` # oops  
```git status```    # git tells us how to undo our change  
```git checkout -- readme.md``` # to checkout 'readme.md' from the last commit  
```cat readme.md``` # yes!  
```git status```

### If the mistake has been staged:  
```echo "todo: ask sequencing center about adapters" > readme.md```  
```git add readme.md```  
```git status```  # again, follow git's instructions  
```git reset HEAD readme.md```  
```git status```  
```cat readme.md``` # mistake still there, but unstaged  
```git checkout -- readme.md```  
```cat readme.md``` # yes!  
```git status```

# 2018-09-26, GitHub to track and share versions   

To reverse a git directory back into a normal (non-git) directory:  
- delete the .git file

```git push```, pushes to GitHub  
```git pull```, pulls from GitHub  
```git clone```, clones a GitHub repository to your local computer  
```git merge```, merge recent changes  
```git remote -v```, tell me about any remote repositories 

Pull, will fetch and merge. 
Fetch, will fetch. c

Created an alias for this: **gl**  
```git log --abbrev-commit --graph --pretty-oneline --all --decorate```

It is very important to **pull** from GitHub often.  
Before you try to pull, commit your changes so you don't lose your work. Any change to an uncommitted file would stop the pull update. To do this:  
```
git pull origin master
```  
You can use ```git status``` to determine which files have conflicts that need to be manually resolved.  
- merge commits have 2 parents, unlike usual commits
- if you feel overwhelmed during a merge, do ```git merge --abort``` and start the various merge steps from scratch
- remember: ```git status``` gives instructions

## For next time:  
- finish and create your own github repo for your course notes, and to push your local repo there, if not done in class already
- open an issue on your github course note repo, where you tag the instructor + TA, with a comment on one particular thing that you learned in the course so far; use at least 1 markdown syntax feature when you write this github issue.
- do **shell scripts from the software carpentry: how to pass arguments to a script**
- do **“tracking a species” from the software carpentry:** combines grep, cut, pipes and script arguments usage. 

**Key points from Software Carpentry: Shell Scripts**  
- save commands in files (sually called shell scripts) for re-use. 
- `bash filename` runs the commands saved in a file 
- `$@` refers to all of a shell script's command-line arguments
- `$1`, `$2`, etc., refer to the first command-line argument, the second command-line argument, etc. 
- Place variables in quotes if the values might have spaces in them. 
- Letting users decide what fiels to process is more flexible and more consistent with built-in Unix commands.

# 2018-10-01, back to shell tools – sed, cut 

Comments from Prof Ane:  
- in your scripts, make your comments shorter
- if your script will only pull out hmax values between 0 - 9, document that in your script
- comments should be related to purpose, not mechanics
- use descriptive variable names, but don't use variable names that are too long. To avoid this issue, use a comment to describe what the variable is the first time you use it
    - st=$(...) # st = snaq time
- lines should be <80 characters in order to effectively use Git track changes

**less**
- `-S` option controls line wrapping 

**cut**
- `-f2`, `-f 1,3`, `-f1-3`
- `-c2` to cut (extract) the second character, not the second field (column)
- `-d` to change the delimiter between column fields intead of tab
- `-d ' '` for a space, `-d`, `-d ,` for a comman (CSV files)

**sort**  
- `-k` to sort by specific columns (keys). 
- `-n` to sort numerically 
- `-r` to sort in reverse order
- `-c` to check fi the file is sorted (this is fast)
- `-t` or `-t ","` to change the seperator to a comma instead of tab (default)

**Exercise:**  
Extract all the features (and counts) for gene “ENSMUSG00000033793”, from file Mus_musculus.GRCm38.75_chr1.gtf
```bash
grep "ENSMUSG00000033793" Mus_musculus.GRCm38.75_chr1.gtf | cut -f 3 | sort | uniq -c
```
- remember the uniq will only remove duplicates that are adjacent, that is why you have to sort first.  

**column**  
This is nice to view csv files on the command line screen.  
- `-s","` sets the separator to a comma instead of a tab (default)

**basename & dirname**  
- `basename` and `dirname` extract file/folder name and its path from a stinrg (the file/folder need not exist)
- `-s suffix`: to removed known suffix (like an extension)
- basename $(pwd)
- dirname $(pwd)
- basename "relative/path/to/myfile.txt"
- dirname  "relative/path/to/myfile.txt"
- basename "/absolute/path/to/myfolder"
- dirname  "/absolute/path/to/myfolder"
- dirname "myfile.txt" # current directory: .
- basename -s "txt" "relative/path/to/myfile.txt"
- basename -s "txt" "relative/path/to/myfile.txt"
- basename -s ".txt" "relative/path/to/myfile.txt"
- basename -s "le.txt" "relative/path/to/myfile.txt

**sed**  
This is a stream editor. Uses regular expressions like grep. The most important thing to learn for sed is the 'find' and 'replace' function.

Usage:  
```bash
sed s/pattern/replacement/ filename > newfile # do NOT redirect to input file!
```  
```bash
sed -i s/pattern/replacement/ filename # for in-place replacement
```  
**go through this section again and add notes here and in sripts file 


**Exercise:**  
extract the unique transcript names in the data file Mus_musculus.GRCm38.75_chr1.gtf: string after “transcript_id”.

```bash
grep -E -o 'transcript_id "\w+"' Mus_musculus.GRCm38.75_chr1.gtf |
  cut -f2 -d" " | sed 's/"//g' | sort | uniq | head
```
or
```bash
grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf |
  sed -E -n 's/.*transcript_id "([^"]+)".*/\1/p' | sort | uniq | head
```
**Message**: try to be specific, this will ensure that your code is more robust. 

**Greedy matching**: problem if we try to capture between quotes like this `"(.+)"`

- I completed the `sed` exercise for participation points on 10/01/18 

# 2018-10-03, shell scripts, if  

**For Wed 10/10 8pm**: exercise 3 of homework assignment 1, including submission via github issue  
**For Mon 10/14**: peer reviews

## Command-line arguments 

Command-line arguments stored in variables `$1`,`$2` etc.  
name of script `$#`: number of arguments  

```(head -n 2; tail -n 2) < "#1"```
- `<` redirects the standard input, and subshell between `()`: both head and tail get the standard input. 

- ```set -e``` # script terminates if any command exits with non-zero status
- ```set -u``` # terminates if any variable is unset
- ```set -o``` pipefail # terminates if command within a pipes exits unsuccessfully

Use this, called the "shebang" to tell the computer to use 'bash' in the 'bin' directory to run this script if the user doesn't input 'bash': **#!/bin/bash**. 
- would execute the script like this ```./myscript.sh filename```, instead of ```bash myscript.sh filename```

To use the above tool you still have to use "./" prior to script, UNLESS you add "./" to the $PATH. You do this by creating a link from one of the bash directories to the directory of the current file.  

**~/bin** directory: 
- create one if you don’t already have one, put your own programs there, to call them from anywhere.
- add it to your PATH variable. Do you see it when you do ```echo $PATH?```
- if not: edit your file ```~/.bash_profile```, add the line export ```PATH="$PATH:~/bin"```, run source ```~/.bash_profile``` or simply exit your shell and re-open it.

I tried going through this on my own and am still having trouble with adding the bash script to my ~/bin and running it from anywhere. **I submitted an issue to ask Prof. Ane and Cora within my course note repository on GitHub.**

**Permissions**:
- -rwxrwxrwx
- "-" means file, "D" means directory
- "r" read, "w" write, "x" execute
- first set: user
- second set: group
- third set: everyone logged onto this machine

Change permissions for script.sh to add writing permissions:  ```chmod u+x script.sh```
- `u`, `g`, `o`: user, group, other; `a` for all
- `+` or `-` to add or remove permissions 
- `r`, `w`, `x`: to read, write, execute 

## arithmetic expansion  

- Use ```(())```. integers only. 
- If you need anything elaborate, it means that you should use Python, Perl, or R.

```bash
i=3678
echo "my variables is: i=$i"
((i = i+6))
echo "I incremented i by 6: now i=$i"
((i--))
echo "I decremented i by 1: now i=$i"
((i++)); echo "I incremented i by 1: now i=$i"
((i+=1)); echo "I incremented i by 1 again: now i=$i"
((i/=5)); echo "finally, I divided i by 5: now i=$i"
echo $((i++))
echo $i # i++ executes the command and increments i after
echo $((++i))
echo $i # ++i increments i first, then executes the command
```

## if statements and checks 

| **test expressions** | meaning |
|----------------------|---------|
```-z str``` | string ```str``` is empty
```str1 = str2``` | strings ```str1```and ```str2``` are identical. different: ```str1 != str2```
```int1 -eq int2 ``` | integers ```int1``` and ```int2``` are equal. not equal: ```int1 -ne int2```
```int1 -lt int2``` | integer int1 is less than int2. greater: ```int1 -gt int2```
```int1 -le int2``` | integer int1 is less than or equal to ints. greater than or equal: ```int1 -ge int2```
```-de thing``` | ```thing``` is a directory. file: ```-f```, link: ```-h```
```-e thing``` | ```thing``` exists
```-r rile``` | ```file``` is readable, writable ```-w```, executable ```-x```
```!``` | negation
```-o```, `-a`, `!` | or, and: to separate expressions within a test `[...]` (*not* short-circuit)
`( )` | to group tests
`||`, `&&` | or, and: to separate different tests (short circuit)

**Examples**: 
```bash
if [ $i -lt 800 ] # the spaces after `[` and before `]` are REQUIRED
then
  echo "i is less than 800"
else
  echo "i is not less than 800"
fi
```

Let's test and check for at least one argument (file name), and if so, test that this file is readable: 
```bash
if [ $# -lt 1 -o ! -f $1 -o ! -r $1 ]
then
  echo "error: no argument, or no file, or file not readable"
  exit 1 # exit script with error code (1). 0 = successful exit
fi
```
- you don't need an "else" section, only a "then" section
- exit status 1 means error, exit status 0 means 'all good'

```bash
if [ $# -lt 1] || [ ! -f $1 ] || [! -r $1]
then
echo "error: no argument, or argument is not a file, or file is not readable"
exit 1 # exists script with error code (1). 0 = successful exit
fi
```

- **exit code**: 0 if successful, 1 if unsuccessful (for the shell, 0=true, 1=failse!!)
- when you check for equality with ```=``` you have to have spaces around the equal sign

# 2018-10-08, git branches

**make sure to check Canvas announcements**
Homework 1.3 is due 8p on 10/10.

**Warnings**
- do **Not** update your github repo by uploading files from the browser
- git desktop does not always let you control and see everything: prefer the command line
- do not track/commit ```.Rhistory``` files, or ```.DS_store``` files, or tmp files. 

```git checkout 832aebd -- readme.md```
- this will bring back the 832aebd version of the readme.md file
- can use the git log address = commit-sha or a tag of you made a tag for that commit 

```git checkout master -- readme.md```
- to get back to the most recent updated version of the readme.md file 

```git checkout```
- look at earlier stages of the *entire project* 

```git checkout master```
- restore the most recent version of the entire project 

## branches
Branches are very useful to easily switch back and forth between different versions. Each version can still evolve.  
Branches are like pointers. They do not hold info. Commits do. 

```git branch branch-name``` to create new branch
```git checkout branch-name``` to switch to new branch
```git branch`` list all the branches

## remote branches
We can use *remote* branches too. You could pull my changes, including the new “readme-changes” branch, and switch to it if you wanted to collaborate on this branch.

```git branch -vv``` show local and remote branches and what they are tracking  
```git push -u origin new-branch``` -u = upstream, push new branch
```git fetch --all``` get new branches from GitHub
```git merge branch``` to merge branch with master
- it is important to be on the branch "that will have the change" ... usually this means being on master 

```git branch -a``` see all remote and local branches 

After we have merged a branch back with master, it is good practice to cleanup branches that aren't being used anymore.  
```git branch -d old-branch-name```
```git fetch --prune``` fetch everything, including branch deletions 

- ```git commit --amend``` to add change the last commit message, but **do not** do this if you already pushed your change to GitHub
- ```git revert``` to revert changes. To undo the last commit ```git revert HEAD```. This would create a new commit whose actions would cancel the actions of the last commit. 
- To undo the changes of the second-to-last commit (but not the changes in the last commit), we would do: ```git revert HEAD~1```. This is safe, and much recommended if you already pushed to github the commits to be undone.
- ```git reset``` and ```git rebase``` it is best to avoid these commands because they change the history file, but these are fine to do on our own laptops prior to commiting anything 

It is not good to erase GitHub history or SHAs because it makes it really difficult to collaborate. 

## SHA checksums

**SHA** = security has algorithm  
1 byte = 8 bits, 1 nibble = 4 bits    
It's a good idea to record the SHA values of important data files as metadata (in readme file). 

```bash
$ echo "this sentence is super cool" | shasum
93aff6c8139fff6855797afc8ea7a7513ffabb6f  -
$ echo "this sentence is duper cool" | shasum
97c250becdaa49c62721478c7f82d116e1039e0e  -
```
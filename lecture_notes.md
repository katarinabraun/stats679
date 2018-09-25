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

<ps -u katbraun> allows you to see all list of processes that you started.

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
<echo \*.txt>  
this expands the wildcard before running echo. 
<echo "\*.txt">

*Single quotes are "very protective". Variables do not get replaced by their values.* 

**New lines:**
- \\n , \r

## Exercise in tb1.fasta  
Find all instances where characters are not A,C,T,G,a,c,t,g
Fist exclude the first line. Then find grep to find anything that is not ACTGactg.  
My code: <grep -v ">gi|" tb1.fasta | grep -o --color [^A,C,T,G]>

## Software carpetnry grep/find key points: 
1. <find> finds files with specific properties that match patterns. 
2. <grep> selects lines in files that match patterns. 
3. --help is a flag supported by most bash commands and programs that can be run from within Bash, to display more info on how to use these commands or programs. 
4. <man command> displays the manual page for a given command. 
5. $(command) insrts a command's output in place. 

# 2018-09-19, grep 

## Feedback/questions from assignment #1. 
- Use relative paths. 
- Document your work to be able to reproduce it yourself, because in 6 months you won't respond to emails.
- Readme: Run the script by going into this folder and running this command. 
- If I have questions in the future it is okay to open an issue on GitHub and tag Cora and/or Dr. Ane. 

Download partitionfinder_bestscheme.txt. Write a grep command to search through and see how many times we see GTR + G.  
<grep -c "| GTR+G " partitionfinder_bestscheme.txt>  
68 (this is the correct answer) 

<grep '^$' filename> this would show all of the blank lines. 

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
'''r
foo <-function(x){x+1} # R function "foo", just adds 1
food(2)
'''  
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
<grep -oc 'GTR+G ' partitionfinder_bestscheme.txt> (answer = 68)  
I put this file in /Users/katbraun/Desktop/bds-files/partitionfinder_bestscheme

# 2018-09-24, github and git at the command line

Track versions of a project with git
 
## Git overview
- take snapshots of your project once in a while. one "commit" = one snapshots
- git stores changes bteween snapshopts, not the wole files
- git stores its data (chnages) in a .git directory
- each collaborator has the project on her/his local machine, and another remote copy of the project is on GitHub. Collaborators can "pull" from GitHub and "push" to GitHub

Each snapshop has an address and a comment: "commit address"  
<git checkout "commit address">  
Additions are in green. Deletions are in red. 

The only file you might want to look at in .git/ is the configuration file - text file.  
git add (to staging area, intermediate picture)  
git diff (show me the difference between new version and staged area)  
git diff --staged (show me the difference between staging area and previous commit)  git commit (send files in the staging area to repo)  
git log --oneline (list of recent git activity), --pretty=oneline

## Commit messages:  
little message that you include with each commit made. These are very important when you are trying to recover previous version. 
Don't use: update, continued, new code, misc, edits. 
50 or fewer characters is strongly recommended. 
If more explanations are needed, add one blank line. Then your explanation paragraph. 
Informativeness - helps to recover old versions.   

## Separation of title vs paragraph.  
git commit will open a text editor and then it's easier to see your new line  
-a option to add all changes in tracked file to the commit (combines add and commit)

## Looking at Git history:  
git show (shows the actual content of the commit, actual differences, only the last commit)  
git log  
git log --pretty=oneline --abbrev-commit

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
echo "todo: ask sequencing center about adapters" > readme.md  
cat readme.md # oops  
git status    # git tells us how to undo our change  
git checkout -- readme.md # to checkout 'readme.md' from the last commit  
cat readme.md # yes!  
git status

### If the mistake has been staged:  
echo "todo: ask sequencing center about adapters" > readme.md  
git add readme.md  
git status  # again, follow git's instructions  
git reset HEAD readme.md  
git status  
cat readme.md # mistake still there, but unstaged  
git checkout -- readme.md  
cat readme.md # yes!  
git status
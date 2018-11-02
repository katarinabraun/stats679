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

# 2018-10-10 awk, parameter expansion, wget & curl

For next time: peer reviews. Look at 2 other people's homework. Will get tagged on two issues. Send the grades via canvas. Go to the issue and provide constructive feedback. Send the grades (without comments) to canvas.  

* add notes on 'some other git subcommands' from Monday's lecture  

You can search in visual code studio using regex (click on *)! This is a really cool way to quickly test whether my regular expressions are working as expected. 

## awk: quick test processing  
More powerful than sed, but can do some similar things. Good for tabular data. 

- command lines: `awk pattern { action } filename`
- pattern: expression or regexp pattern (in slashes, e.g. `/^chr\d/)`. If true or match for a given line (record): the actions are run. If no stated action: the line is printed.
- `a ~ b` true if `a` matches regexp pattern `b`. no match: `a !~ b`
- combine patterns with `&&` (and) and `||` (or)
- special patterns: BEGIN and END
- variables: `$0` for entire record (line), `$1` for first field (columns)’s value, `$2` for second field’s value, etc.
- `NR` = current record (line) number
- `NF` = number of fields (columns) on current line
- can do arithmetic operations on field values, standard comparisons (`<=`, `==` etc.)
- extra fields can be printed
- new variables can be introduced, modified, used (no $ to use them: not like shell language)
- actions: `if`, `for`, `while` statements can be used
- many built-in functions, like `exit`, `sub(regexp, replacement, string)` `substr(string, i, j)` or `split(string, array, delimiter)`
- default field (column) separator in input file: tab. For csv file: change to comma with `-F","`
- two pattern-action pairs separated by `;`
- new variable `feature` introduced: associative array. like list but indexed by keys (dictionaries in Python & Julia, hashes in Perl)
- `for` loop, new variable `k` inside.

Language for quick test-processing tasks on tabular data: `bioawk` for biological formats. There are special functions in `bioawk` for sequence data. 

**Examples**: within bds-files/chapter-07...
- action is in curly braces
- pattern is not
- everything has to be in single quotes 
- awk doesn't know about shell variables, fix for this is to pass the variable fromt the shell to awk -t=$variable as an option before single quotes 
- NR is the total number of records
- a awk array is like a python dictionary (key and value)

```bash
awk '{ print $0 }' example.bed # like cat. No pattern: defaults to true
awk '{ print $2 "\t" $3 }' example.bed # like cut -f2,3
awk '$3 - $2 > 18' example.bed # prints lines (default action) if feature length > 18 (bed 0-based)
threshold=18
awk '$3 - $2 > $threshold' example.bed        # error: $ reserved for awk fields
awk -v t=$threshold '$3 - $2 > t' example.bed # -v option: to define awk variables
awk '$1 ~ /chr1/ && $3 - $2 > 10' example.bed
awk '$1 ~ /chr2|chr3/ { print $0 "\t" $3 - $2 }' example.bed
awk 'BEGIN{ s = 0 }; { s += ($3-$2) }; END{ print "mean: " s/NR };' example.bed # mean feature length
awk 'NR >= 3 && NR <= 5' example.bed # lines 3 to 5 only
awk -F "\t" '{print NF; exit}' Mus_musculus.GRCm38.75_chr1.bed # number of columns on 1st line
grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | awk -F "\t" '{print NF; exit}' # deals with header (start with #) in gtf file
awk '/Lypla1/ { feature[$3] += 1 };
    END { for (k in feature)
    print k "\t" feature[k] }' Mus_musculus.GRCm38.75_chr1.gtf  | column -t
```

## parameter expansion  

use `${variable_name extra stuff}`

```bash
var="coolname.txt.pdf.md"
i=3678
echo "var=$var and i=$i"
echo "substrings of parameter values: ${i:1} and ${var:4:5}" # :offset:length
echo "strip from the end: ${var%.*}"  # strips shortest occurrence
echo "strip from the end: ${var%%.*}" # strips longest  occurrence
echo "strip from beginning: ${var#*.}"  # strips shortest occurrence
echo "strip from beginning: ${var##*.}" # strips longest  occurrence
echo "substitute: ${var/cool/hot}"
echo "delete:     ${var/cool}"
```

## getting data from the web: wget and curl  
`wget` can download files from the web reproducibly 

Can download files recursively: `-r`, but dangerous (aggressive). puts limits with options: 
- `-l` to limit the level, or maximum depth: `-l 1` to go only 1 link away
- `--accept-regex` to limit what's accepted using regular expression: here files whose names contain `.fasta` or `.txt`
- `nd` or `--no-directory`: to not re-create the directory hierarchy
- lots of other options, like: `--no-parent`, `-O`, `--user`, `--ask-password`, --`limit-rate`

The host may block your IP address if you are downloading too muchh too fast. to avoid: use `--limit-rate=50k` to wait 1 sec between file downloads

`curl` writes to standard output, best for one file at a time
- can use more protocols, like `sftp`
- can follows redirected pages with `--location`
- some options: `-O`, `-o`, `--limit-rate`, `-I` or `--head`: to get header only. 
- on ftp files: file size
- `-s`: silent, no progress meter, no error messages `-#`: simple progress bar, no progress meter 

# 2018-10-15, connecting to remote machine to run long jobs

Can ask to have an account on the CHTC servers. 

Edit files using nano or emacs within the ssh terminal window. 
`-nw` = no new window for your text editor. 

To avoid typing your password each time: copy the public key from your laptop (in `id_rsa.pub`) to the file `~/.ssh/authorized_keys` on the remote server. You created a key pair earlier for github, and copied your public key to your github profile.

`scp`: secure copy. Same as `cp`, but need to provide user name, machine name and full path on the remote machine. works over ssh.
slight difference between cp and scp:
`cp -r log/ target/path/` copies the content of the log/ directory
`cp -r log target/path/` copies the directory itself and its content. Do this one. 

`-p` option preserves the original time that the file was created, instead of when it was copied. 
`-r` option to recursively grab all the files within the listed directory. 

## long-running jobs: nohub

```mb mrBayes-run.nex > screenlog &```
- redirects output and errors to screenlog 
- `&` means I want the shell command to be returned 

Now, I want to run this on the stat servers, log out, log back in tomorrow to get the results.

log out: exit the terminal, all jobs started from it will be sent a “hang up” signal (SIGHUP), and killed. (recall: SIGKILL with `kill -9`, SIGINT with control-C, SIGTSTP with control-Z)
`nohup`: will catch and ignore this hang-up signal
- this means that the `nohup` will not touch the command that you indicate and that command will keep running even when you leave the server
- `nohup` doesn't work on the stats servers because these servers use an AFS which has a very strong authentication system. When I log out, I lose my token, and my permissions to write to files, so my process runs but will have an error as soon as it will want to write to or read from a file.

## tmux: terminal multiplexer

Solves several challenges, like GNU `screen`
- `tmux` sessions can be **detached** and **reattached**: detach, log out, log back in, re-attach
- **multiple windows** in a session: say one with an editor, and another for shell commands

Should I install `tmux`? I don't really ever work on remote servers other than Coltrane? What is Coltrane btw? 

**tmux keys** | **actions**
--------------|-------------
`^a d` | detach
`^a c` | create new window
`^a |` or `^a -` | splits window vertically or horizontally (depends on config file)
`a n` or `^a p` | go to next or previous window
`^a` left arrow | go to left pane. other arrows for right, top, bottom panes
`^a ?` | list all key sequences 
`^a &`, `exit` or `logout` | kill current window
`^a x` | kill current pane 

These shortcuts depends on your tmux configurations. 

## running many jobs
- high performance: one (or few) very long job(s), possibly requiring a lot of memory
- high throughput: very many job, each short (<24h). need program to distribute the jobs across very many different machines, and to get all output files back from these machines at the end.

Resources on campus: ACI (advanced computing initiative), CHTC (center for high-throughput computing) and HTCondor for job scheduling. HPC cluster "lunchbox" in Stats:d uses slurm for job scheduling. **Get a CHTC account**.

*Homework for W 10/17: install python*. I think I already have this done via conda. We are using Python 3.0, which is what I have, so I'll just doublecheck this before Wednesday. I have python 3.6.6 installed. I conda updated it on 10/15. 

# 2018-10-17, intro to python 

I'll have to find a partner to do this exercise with. 

Homework for 10/17:
- do python scw section 2: repeating actions with loops
- git branch exercise:
    - pair up with one other student in the class
    - decide which git repository to work on: classe note repo from one or the other student, say student A
    - student A goes to her/his own repository, clicks on “Settings” then “Collaborator” (github might ask for your password) then enters the gihub user name for student B, then click “Add collaborator”: to give push access to student B
    - student A: start a new branch “A”, add something to it, push the branch to github
    - student B: clone the repo on her/his laptop, start new branch “B”, add changes or new file to it, push the branch to github
    - student A: pull branch B, add changes to it, push to github
    - student B: pull branch A, add changes to it, push to github
    - student A and B: each checkout master branch, merge his/her own branch into master, push to github. The second student doing this will need to pull first.
    - both students: check the branches and merge on the repo’s network: click on “Insights” then “Network”; there should be at least 1 merge commit and labels for at least 3 branches: master, A and B.
    - open a github issue with a link to the url with the “network” view; tag the instructor & TA on this issue, give both student names.

You can run scripts in the termina from within Visual Studio Code. I am not sure if this works for Bash scripts. You can interact as if you were in the terminal as well. 

You can run commands from with shift-enter from within Visual Studio code. 

We also used iPython as well. There are helpful options in iPython with in the commandline. You can have more erros in your syntax with iPython(?) 

The other option is to use Jupyter notebook. It's nice to view (in a browser). It will contain comments in markdown format. It can contain everything within one file. The files it generates are large, but that might be okay for me. This is really nice to create a comprehensive document for publication or collaboration. 

Cecile uses fewer lines of code per cell. I wonder if that would be preferable. 

Finish both Python software carpentry exercises as well as the GitBranch exercise. 

# 2018-10-22, continuing intro to Python 

HW: two more Python sections. 

Int types vs float types. Float types have decimals.  
Dot notation: `module.function` or  `object.method`. 
Python is **0-indexed**.  
[row, column] for numpy arrays

Write a number in base 2: 
- 1
- 10
- 11
- 100
- 101
- 110
- 111
- 1000
- 111...111, 2^64 - 1

- + or - = 1 bit
- 1.234 x 10 ^ 102 = 11 bits that represent the exponent
- remaining bits can code the numbers 
*important point: integers are fundamentally distinct from floats because they are coded and interpreted differently by your computer. 

`string` vs `boolean`
- boolean = true/false, only need one bit for this, false = 0, 0.1, none. Everything else = true. 
- string  = 

`If 1` interpreted as `if true`. 
`1.0/3.0 == 1.0 - 2.0/3.0`
> `False` because these values use floats, don't test exact equality using floats 

`"%s %s hello %s" % (5, 5.8, "5")`
- convert integers to a string 
`"%d %d %d world" % (5, 5.8, int("51))`
- write digits, 5 5 51 world
- ?? 
- writes 5.00 5.80 5.1e+01

List is not the same as an array. List denoted by [stuff, in, here, is, the, list,]. Tuple = (,). Lists can be changed, tuples cannot be changed (**nonmutable**).

Get started on section 3: storing multiple values in lists, added notes in commands_scripts.md. 

Here are some more notes (GitHub was down on Monday): 

## Python basic types, syntax, loops, and lists

Basic types: 
- int `14`
- float `14.123`
- string `"hello"`
- bool (`True` or `False`)
- None, complex `3+0.5j`
- NoneType (`None`)

`int`s and `float`s are fundamentally different in how they are coded. Consequence = *never test for exact equality of `float`s. 

Can convert: `int`, `float`, `str`, `bool`. 

To store multiple elements list `[10,20]`, tuple `(10,20)`, dictionary/hash `{"blue":10, "green":20}`, set `set([10,20])`
- a list of lists is not the same as an array. `[1,2]` to create a list. 

### Mutable vs inmutable objects: 

Lists are mutable.  
Strings, numbers, tuples are inmutable.  
How `b=a` and changes to `b` can cause (or not) changes to `a`: 

```Python
a = "Darwin"
b = a
print("b=",b)
b = "Turing" # does not change a, because a has immutable value
print("now b=",b,"\nand a=",a)

a = [10,11]
b = a
b[1] = 22 # changes the value that b binds to, so changes a too
print("b=", b, "\nand a=",a)

c = [a,a] # list of lists. Not numpy array!
print(c)
a[0] = -5
print(c) # aahh!!

b = a.copy() # various alternative options
b = list(a)
import copy
a = [10,11]
b = copy.copy(a)
b[1] = 22 # changes the value that b binds to, does not change a
print("b=", b, "\nand a=",a)
```
Get around this by using a **deep copy** vs a simple(shallow copy): 
```Python
a = [[10,11],[20,21]]
print(a)
b = copy.copy(a)
b[0][0] = 50
print("b=",b,"and a=",a)
b[0] = [8,9]
print("b=",b,"and a=",a)
b = copy.deepcopy(a)
print("now b is back to a: ",b)
b[0][0] = 8
print("b=",b,"and a=",a)
```

Functions that operate on mutable objects can change them in place. 

### Syntax
`:` to end starting lines, **indentation** to define blocks. 

Important concepts:
- binding of a name
- scope of variables
- local namespace

### Conditions

`==`, `<`, `>`, `not`, `and`, `or`. 
Anything *other* than `False`, 0, `None`, empty string or empty list is considered `True` in a boolean context. 

### Tuples

Tuples are inmutable, unlike lists. Useful for
- array sizes: `(60,40)` earlier
- types of arguments to functions: like `(float, int)` for instance
- functions can return multiple objects in a tuple
- a tuple with a single value, say 6.5, is noted like this `(6.5,)`
- they come in handy for exchanges: 

```Python
left = 'L'
right = 'R'

temp = left # without tuples you can use temporary variables
left = right
right = temp
print("left =",left,"and right =",right)

left = 'L'
right = 'R'

(left, right) = (right, left) # using a tuple, we can exchange the value of these variables more easily 
print("left =",left,"and right =",right)

left, right = right, left # this works as well, it's recognized in python as a tuple 
print("now left =",left,"and right =",right)
```

### Some useful functions for lists

`.append(x)`, `.extend(x)`, `.insert(i,x)`, `.reverse()`, `.pop()`, `.sort()`, `sorted()`

```Python
odds = [1, 3, 5, 7]
print('odds before:', odds)
odds.append(11) # adds 11 to the end of our list 
print('odds after adding a value:', odds)
```

```Python
odds = [1, 3, 5, 7, 11]
del odds[0]
print('odds after removing the first element:', odds)
odds.reverse() # reverse the order of elements in the list 
print('odds after reversing:', odds)
a = odds.pop() # delete the last element from the list 
print('odds after popping last element:', odds)
print("this last element was",a)
a = odds.pop(1) # get the value that we popped capture into the variable a
print("popped element number 1 (2nd element):",a)
odds
```

```Python
odds = [1, 3, 5, 7]
primes = odds # only copying the list address, chnaging primes will change odds
primes += [2] # add to the list (primes and odds will be modified)
print('primes:', primes)
print('odds:', odds)

counts = [2, 4, 6, 8, 10]
repeats = counts * 2 # copies the list and writes each element twice 
print(sorted(repeats))    # all integers, sorts the elements of the list 
print(repeats) # unchanged
repeats.sort() # modified in place
print(repeats)
print(sorted([10,2.5,4])) # sorted will only work if the type in the list is all the same 
print(sorted(["jan","feb","mar","dec"]))  # all strings --> works
print(sorted(["jan",20,1,"dec"]))  # error b/c not all elements are the same 
```
### list comprehensive 
`[xxx for y in z]` where `z` is a collection, `y` introduces a local variable name, and `xxx` is some simple function of `y` (typically)

```Python
counts = [2, 4, 6, 8, 10]
counts + 5 # error
[num+5 for num in counts] # for each number in counts, get num+5 and then make a list of those results, this did NOT change counts 
counts
for i in range(0,len(counts)): # I don't understand why you need the 'len' part here 
    counts[i] += 5 # modifies "counts" in place
counts
```
### some useful functions for strings 

`.strip()`, `.split()`, `.replace()`, `.join()`, `.splilines()`

```Python
taxon = "Drosophila melanogaster"
genus = taxon[0:10]
print("genus:", genus)
gslist = taxon.split(' ')
print(gslist)
print("after splitting at each space: genus=",
      gslist[0],", species=",gslist[1], sep="")
print(taxon) # has not changed: immutable
print(taxon.replace(' ','_'))
print(taxon) # has not changed
```

```Python
mystring = "\t hello world\n \n"
mystring
print('here is mystring: "' + mystring + '"')
print('here is mystring.strip(): "' + mystring.strip() + '"')
print('here is mystring.rstrip(): "' + mystring.rstrip() + '"') # right strip (or tRailing) only
"     abc\n \n\t ".strip()
```

### some useful modules

numpy, time, matplotlib.pyplot, glob, re, sys, argparse

`import module` or `import module as nickname` or `from module import function1, function2`, or `from module import *`

### some useful functions/methods

`type`, `print`, `range`, `list`, `del`, `len`, `abs`, `in`, `**` for power, `+` to concatenate strings or lists

to check assumptions: `assert test_expression, "error message"`

# 2018-10-24, regular expressions in python

## simple patterns and tools 

useful functions on strings for simple things: `.strip`, `.split`, `.join`, `.replace`, `.index`, `.find`, `.count`, `.startswith`, `.endswith`, `.upper`, `.lower`,

```Python
a = "hello world"
print(a.startswith("h"))
print(a.startswith("he"))
print("h" in a)
print("low" in a)
print("lo w" in a)

print("aha".find("a")) # grep without regular expressions 
print("hohoho".find("oh"))
mylist = ["AA","BB","CC"]
"coolsep".join(mylist)

print(type(""))
print(dir(""))
```

## regular expressions 

use the **re library** and its functions `re.search`, `re.findall`, `re.sub`, `re.split` etc.
recall regular expression syntax

- `r''` to write the regular expression pattern, for “raw” strings: to read a \n as slash and an n, not as a newline character.
- multipliers are greedy by default: `*`, `+`, `?`. Add `?` to make them non-greedy
- info from match objects: `.group`, `.start`, `.end`
when pattern not found: match object is `None`: False when converted to a boolean

```Python
import glob
filenames = glob.glob('*.csv')
print(filenames)

import re
mo = re.search(r'i.*n',filenames[0]) # using the search function from the module re, the star is greedy 
print(mo)  # match object, stores much info. search: first instance only. saved the results of the object mo, found 12 matches, very greedy 
print(mo.group()) # what matched, show us what was matched
print(mo.start()) # where match starts: indexing start at 0, show us starting index
print(mo.end())   # where it ends: index *after*!, show us ending index 

mo = re.search(r'i.*?n',filenames[0]) # match not greedily, first n I will accept 
print(mo)
print(mo.group())
print(mo.start())
print(mo.end())
```
When there is not match, the matched object is None adn interpreted as False in a boolean context. 

```Python
sequences = ["ATCGGGGATCGAAGTTGAG", "ACGGCCAGUGUACN"]
for dna in sequences:
    mo = re.search(r'[^ATCG]', dna) # save search in matched object 
    if mo: # if mo contains anything, convert to true, and do the next stuffs 
        print("non-ACGT found in sequence",dna,": found", mo.group())
```

less efficient:
```Python
for dna in sequences:
    if re.search(r'[^ATCG]', dna):
        mo = re.search(r'[^ATCG]', dna)
        print("non-ACGT found in sequence",dna,": found", mo.group())

```
Finding all instances: 
```Python
print(re.findall(r'i.*n',filenames[0])) # greedy. non-overlapping matches, didn't really find all matches, only found 'inflammation' 
mo = re.findall(r'i.*?n',filenames[0])  # non-greedy, found 'in' and 'ion' 
print(mo)
mo

for f in filenames:
    if not re.search(r'^i', f): # if no match: search object interpreted as False
        print("file name",f,"does not start with i")
```
## search and replace  
`re.sub`, kinda like sed 
- capture with parentheses in the regular expression
- captured elements in `.group(1)`, `.group(2)` etc. in the match object
- recall captured elements with `\1`, `\2` etc. in a regular expression, to use them in a replacement for example

```Python
re.sub(r'^(\w)\w+-(\d+)\.csv', r'\1\2.csv', filenames[0]) # search for starting with something that's a word character, capture it, then any # of word characters, then dash, then digits 1 or more, capture it, then a real dot, then csv. replace with first letter,digit, and csv. 

for i in range(0,len(filenames)): # do the above for all filenames in place 
    filenames[i] = re.sub(r'^(\w)\w+-(\d+)\.csv', r'\1\2.csv', filenames[i])
print(filenames)

taxa = ["Drosophila melanogaster", "Homo sapiens"]
for taxon in taxa:
    mo = re.search(r'^([^\s]+) ([^\s]+)$', taxon)
    if mo:
        genus = mo.group(1) # get the first thing we captured
        species = mo.group(2) # get the second thign we captured 
        print("genus=" + genus + ", species=" + species) # put them together

print(taxon)
print(mo) # variables defined inside "for" are available outside
print(mo.start(1))
print(mo.start(2))

taxa_abbrev = [] # make an empty list 
for taxon in taxa: # loop over taxa 
    taxa_abbrev.append( # append a new item to the empty list 
        re.sub(r'^(\S).* ([^\s]+)$', r'\1_\2', taxon) # substitute anything that is not a space, anything in between space and anything, replace this by capture stuffs
    )
print(taxa_abbrev)
```
This strategy is good - start with an empty list and build it up with the `append` function. 

## scope of variables 

Main session
- filenames
- a = "hello world" 

Function, foo
- a = 7, did function a = 18 

But outside of the function, a still equals "hello world" 
These variables are not related to each other. They persist within their own name-spaces. 

## split according to a regex

- removes the matched substrings
- returns an array 

```Python
coolstring = "Homo sapiens is pretty super"
re.split(r's.p', coolstring) # split function from re module to split with a regex 
re.split(r's.*p', coolstring) # split with an s, a character, and a p, then add the coolstring 
re.split(r's.*?p', coolstring)
```

An array is like a list, but you can only perform certain functions on it. It's not like a dictionary that has a key/value pair. Use arrays when you want to do arithmetic on the elements within the collection of items. An array is like a more complicated list. 

Homework: 
- Do the next three Python sections. 
    - creating functions
    - errors and exceptions
    - defensive programming 

# 2018-10-29, Python Functions

```Python
def function_name(arguments):
    """docstring here: to explain what the function does"""
    command indented
    indented command
    return value # returns None if no return statement
```

```Python
def foo(arg1, arg2=0):
  """
  Return arg1 -1 + arg2. # this much documentation is normal 
  arg2 is optional, 0 by default.
  good practice: include examples.
  Examples: # it's really good to provide examples, you can use this later to test your code to make sure it's working as expected 

  >>> foo(5)
  4
  >>> foo(5,8)
  12
  >>> foo(5, arg2=2)
  6
  """
  assert type(arg1)==int, "error message: here arg1 should be an integer"
  res = arg1 - 1 + arg2
  return res
```

Another example: 

```Python
def startswithi(str):
    """Return True if the input string starts with 'i', False otherwise.
    Require that the "re" was imported beforehand.

    # document assumptions 
    notes:
    - the double and single quotes inside my tripe double-quoted docstring
    - in my text here the indentation adds 4 spaces on each line.
      Those are ignored because it's a triple set of quotes.

    Example:

    >>> startswithi("hohoho")
    False
    """
    return(bool(re.search(r'^i', str)))

help(startswithi) # or ?startswithi in interactive session
print(startswithi("iamcecile"))
print(startswithi("hohoho"))
```
Triple quotes = docstrings. This is not specific to Python. 

key principle: break problem down into small parts
write functions
- if you do some “copy-paste” of your code: you need to write a function
- functions make your code easier to debug, easier to read
- use meaningful names for functions and for variables

```Python
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15

print('freezing point of water:', fahr_to_kelvin(32))
print('boiling point of water:', fahr_to_kelvin(212))

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))

def fahr_to_celsius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celsius(temp_k)
    return result

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))
```
**Anytime you find yourself copy/pasting, you should be writing a function. Down the road, it pays off. Keep this in mind. 

Exaple to breakdown: 
```Python
import numpy
import glob
import matplotlib
filenames = glob.glob('inflammation*.csv')

def analyze_all():
  for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)

def analyze(filename):
    data = numpy.loadtxt(fname=filename, delimiter=',')
    # commands to make the figure for one data file

def detect_problems(filename):
    data = numpy.loadtxt(fname=filename, delimiter=',')
    if (numpy.max(data, axis=0)[0] == 0 and
        numpy.max(data, axis=0)[20] == 20):
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')

analyze_all()
```

Write things from global to more detailed. Cecile thinks it helps to have the big picture first. Eg. how the above script is set up where you see okay, I am going to print the filename, then analyze the files, and finally detect any problems. 

in-class exercise: binomial coefficients

goals: 
- write functions, divide a large problem into smaller problems
- use optional arguments and default argument values
- use loops and `if` statements
- use docstring to document functions
- check for assumptions
- test code automatically
- create a module: use the script to be run on the command line, or as a module

Calculate binomia coefficients is not easy numerically. 

Calculating binomial coefficients is not easy numerically. The number of ways to choose k elements among n is `choose(n,k) = n! / (k! (n-k)!)` where factorial n: `n! = 1*2*...*n` becomes very big very fast. But many terms cancel each other in “n choose k”, and it is a lot easier numerically to calculate the log factorial: `log(n!) = log(1) + ... + log(n)`.

1. Write a function “logfactorial” that calculates `log(n!)` for any integer `n>0`. Hint: use `math.log()` to calculate the log of a single value, and use a loop to iterate over `i` and get the `log(i)` values.
2. Add a docstring
3. Add checks on the input `n` (should be an integer, and non-negative)
4. Add tests as examples inside the docstring. For the tests to be used, add a section using the doctest module. Check that you can run the checks with `./binomial.py --test`
5. Add an optional argument `k` to calculate `log(n!/k!) = log((k+1)*...*n) = log(k+1) + ... + log(n)`, with default `k=0`. Return log(1)=0 if k>n, with no error (it’s a sum of 0 terms).
6. Add a check that `k` is a non-negative integer
7. Add examples to test the function with a non-default `k`, for instance: with n=5 and some k<5, also n=k=5 (boundary), and n=5, k=6.
8. Write a function “choose” to calculate the log of the binomial `log(choose(n,k))` for any integers `n>=0` and `0 <= k <= n`. Start with the docstring and with a test. Recall that `choose(n,k) = n!/(k! (n-k)!)`, so `log(choose(n,k)) = log(n!/k!) - log((n-k)!)` and you can use the function from step 5 twice.
9. Add an optional argument to this `choose` function, to return either the binomial coefficient itself (as an integer) or its log (as a `float`). Make the function return the binomial coefficient by default, not its log.
10. Add a docstring for the module itself
11. Add arguments for the script itself, to be able to run it like this for instance: `./binomial.py -n 100 -k 30` or `./binomial.py -n 1000 -k 300 --log`

Try for next time to do 1 through 5. Go through my script again and go through two more software carpentry sessions. Also, try to write the next function. Also, try to get my functions to run and try my test function thing. I'll go through the lecture notes, update this document and commit everything to GitHub before next class. 

# 2018-10-31, python functions and scripts continued 

Submit binomial code on GitHub. I don't think this will be graded formally. 

Strongly recommended to use to argparse library. 

```Python
#!/usr/bin/env python
"""module with very cool functions to say 'hi'"""

import argparse # first need to import this library 
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser() # create an object of library ArgumentParser
parser.add_argument("-n", type=int, help="number of times to say hi") # will take care of error messages, if n is not an integer
parser.add_argument("-l", "--long", action="store_true", help="whether to say 'hi' the long way") # default will be off
parser.add_argument("-g", "--greetings", type=str, help="greeting message, like a name")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args() # call a function on this object that will create a new object (args)
hi = "Howdy" if args.long else "Hi" # howdy if args.long is true, otherwise hi = HI 

# test argument problems early:
if not args.test and __name__ == '__main__': # __name__ is predefined in python, used to check if you are running the file as a script, vs importing the file as a module as a part of something bigger 
    if args.n<0: # assert is a better way to throw an error 
        raise Exception("argument -n must be 0 or positive") # raise is a very generic way of raising an error 
    # no error if file imported as module

def print_greetings(extra_greetings, n=args.n):
    """
    print individualized greeting. example:
    >>> print_greetings("have a good day", 0)
    have a good day, you.
    """
    s = ""
    for i in range(0,n):
        s += hi + ", "
    if extra_greetings:
        s += extra_greetings + ", "
    s += args.greetings if args.greetings else "you"
    s += "."
    print(s)

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print_greetings("")
```

I worked on creating this binomial module in class: 

```Python
#!/usr/bin/env python
import math 
import argparse
# use an Argument Parser object to handle script arguments
import doctest

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("--log", action="store_true", help="returns the log of the binomical coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfac(n, k=0): # default value of k = 0 
    """Return the log factorial `log(n!)` for any integer `n>0`.

    Examples: 

    >>> round(logfac(5),2)
    4.79
    >>> round(logfac(0),2)
    0
    >>> round(logfac(5,3),2)
    3.0
    >>> round(logfac(5,5),2)
    0
    >>> round(logfac(6,5),2)
    1.79
    
    Notes: 

    """
    assert type(n)==int, "error message: here n should be an integer"
    assert type(k)==int, "error message: here n should be an integer"
    assert n >= 0, "error message: n must be great than or equal to zero"
    assert k >= 0, "error message: k must be greater than or equal to zero"


    result = 0

    for i in range(k,n):
        result += math.log(i+1) # to start with k (or 1 if k = 0)
    return result

# print(round(logfac(5),2))
# print(round(logfac(0),2))
# print(round(logfac(5,3),2))
# print(round(logfac(5,5),2))
# print(round(logfac(6,5),2))

def choose(n,k,log=False): 
    """Calculate the log of a binomial `log(choose(n,k))` for any integers `n>=0` and `0 <= k <= n`.
    choose(n,k) = n!/(k! (n-k)!) so log(choose(n,k)) = log(n!/k!) - log((n-k)!)

    Examples: 

    >>> round(choose(4,1),2)
    4
    
    >>> round(choose(5,3,True),2)
    2.3

    >>> round(choose(5,3,False),2)
    10

    Notes:
    """
    
    assert type(n)==int, "error message: here n should be an integer"
    assert n >= 0, "error message: n must be great than or equal to zero"
    assert type(k)==int, "error message: here n should be an integer"
    assert (k >= 0) and (k <= n), "error message: k must be greater than or equal to zero and k must be less than or equal to n"
    
    if log: 
        return(logfac(n,k) - logfac(n - k))
    else:
        return(round(math.exp(logfac(n,k) - logfac(n - k))))

def runTests():
    print("testing the module...")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose(args.n, args.k, args.log))
```

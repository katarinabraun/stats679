# Shell. 
The Shell is a programming language that is used at the terminal interface to speak to my computer.GUI vs CLI (command-line-interaface).  
**Unix philosophy:** Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface. --Doug McIlory

- ^Z pause a job. fg to resume in foreground. bg to resume in the background (get prompt back)
- ^C cacel a job. 
- ^D end of standard input.
- ^a move to the beginning of a line. 
- ^e move to the end of a line.  

## Shell commands: 
1. **ls** - list
2. **rm** - remove  
    Options: `-r` (recursively) `-f` (force)
3. **'*'** - wildcard. `?` - matches exactly 1 character. 
4. **Echo** - epeat exactly what I entered in the command line.  
    echo $SHELL  
    /bin/bash
5. **cat** - print file contents to the terminal window.  
    Options: `-l` (in list format), `-r` (in reverse order), `-t` (ordered by time)
6. **whoami** - get your username. 
7. **mkdir** - make a directory. 
8. **rmdir** - remove a directory. 
9. **mv** - move (and rename). ```mv <from_file> <to_file```
10. **cp** - copy. ```cp <from_file> <to_file>```
11. **touch** - create a blank file. 
12. **diff** - difference. 
13. **wc** - word count.  
    Options: `-l` (lines), `-w` (words), `-c` (characters)
14. **less** - view part of a file in the terminal.  
    Options: - `q` (quit), -'`return`' (next line), -'`space`' (next page), -d (down next 1/2 page), -b (back one page), -`y` (back one line), -`g` or < (go to the first line, '4g' go to fourth line), -`G` or > (go to last line), -`/pattern` (search forward), -`?pattern` (search backward), -`n` (next: repeat previous search)
15. **sort**  
    Options: `-n` (numerically)
16. **head/tail** - view beginning/end of a file. -n #numberoflines.  
    Options: `-f` (follow)
17. **uniq** - filters out repeated lines (consecutive/adjacent lines only).  
    Options: `-c` (to get counts)
18. **cut** - cut out selected portions of each line of a file.   
    Options: `-b list` (list specifies byte positions), -c list (list specifies character positions), `-d delim` (delim as the field delimiter chracter instead of the tab character), `-f list` (list specifies fields, separated in the input by the field delimiter character (-d), output fields are separated by a single occurence of the field delimiter character), `-n` (do not split multi-byte characters), `-s` (suppress lines with no field delimiter characters). `-f`, `-f 1,3`, `-f1-3`, `-c2` to cut the second character rather than the second field, -d to change the delimiter between from tab (default) to comma (-d',') or space (-d' '). 
19. **history** - shows the history of all previous commands, numbered. 
20. **!#** - to re-execute command # in the history. `!$` for last word or last command.
21. **jobs** - see a list of jobs running.  
22. **ps** - see a list of current processes (PID = process ID)
23. **kill** - kill a job. `kill -9 12167` to kill process # 12167. 
24. **top** - see all processes, refreshed, shows CPU and memory consumption. 
25. **man** - print manual of this command to see all options etc. 
26. **grep** - find things in text file  
    Options: `-n` (line numbers), `-i` (case-insensitive search), `-w` (whole words), `-v` (invert the search), `-o` (to get match only), `-E` (Extended regular expressions), `-P` (Perl-like regular expressions)
27. **find** - to find files, whose names match simple patterns  
    Options: `-type` with `d` or `f` (for directory or file), `-name` (with a shell pattern -say '\*.pdf'), -d (depth - eg -d 1), `-mytime` (for modified time)  
    `find . -name '\*.txt'`  

28. **!!** - retrieves immediate preceding command (same as hitting the up arrow key)
29. **more** - like less, but not as good, streams in data from a file to a terminal viewer.
30. **sort** - to sort by specific columns (keys): `-k1,1` to sort by keys in columns 1 to 1, then `-k2,2` to resolve ties by sorting column 2 to 2, and `n` to sort that 2nd column numerically, `r` to sort the 2nd column in reverse order. `-c` to check if the file is sorted already (fast, reports 'disrodered' if not sorted), `-t,` or `-t","` to change the separator to a comma instead of a tab (default)
31. **column** - formats tabular data to visualize in the terminal. `-s","` sets the separator to a comma instead of a tab (default)
32. **basename** & **dirname** - extract the file/folder name and its path from a strong (the file/folder need not exist). `-s suffix` to remove known suffix (like an extension). 
33. **sed** - stream editor. Edits files without having to load it into memory. Its most important use: to substitute things.  
    ```bash
    sed s/pattern/replacement/ filename > newfile
    # do NOT redirect to input file!
    ```
    ```bash
    sed -i s/pattern/replacement/ filename > newfile
    # for in-place replacement
    ```  
    Warning: unlike grep, sed does *not* recognized "enhanced" (perl-like) expressions like `\d`, `\s`, or `\w`. use classes instead: `[0-9]` or `[a-zA-Z_]`
- `s///` to replace first occurence of a match 
- `s///g` to replace globally (all instances)
- `s///i` and `s///gi` for case-insensitive
- `-E` for Extended regular expressions 
- `-n` to *not* print every line
- `s///p` print if there is a match  

    We can capture and re-sue a match: with `()`to capture a pattern and `\i` to print the ith match.


# Regular expressions: 
- **.**    any one character
- **^**    beginning of line (only when placed first)
- **$**    end of line (only if placed last)
- \    turns off special meaning of next symbol 
- **[aBc]**    antything in: a or B or c. Ranges: like [0-9], [a-z], [a-zA-Z]
- **[^aBc]**    anything but: a, B, or c. 
- **\w**    any word character: letter, number, or "_". Also [[:alnum:]_]. Opposite: \W
- **\d**    any single digit. Also [[:digit:]] or [0-9]. Opposite: \D 
- **\s**    any white space character: single space, \t (tab), \n (line feed) or \r (carriage return). Also [[:space:]]. Opposite: \S 
- **\b**    word boundary (null string). also \< and \> for start/end boundaries. Opposite: \B 
- **\+**    one or more of the previous
- **?**   zero or one of the previous
- **\***    zero or more of the previous
- **{4}**    4 of the previous
- **{4,6}**    between 4 and 6 of the previous
- **{4,}**    4 or more of the previous 

# Pipes and redirection: 
- \> to redirect the output of one command to a file. 
- | pipes the output of one command to the input of another command, using streams. 
- \>\> redirects output and appends to a file. 
- 2> redirects standard error. 
- &> redirects both output and error (bash shell). 
- & added to the end of a command to run it in the background automatically and get the shell prompt back. 

# General Shell notes:  
Inside a shell script, **$1** means "the first filename (or other arguemtn) on the command line". For the same reason that we put the loop variable inside double-quotes, in case the filename happens to contain any spaces, we surround **$1** with double-quotes.  
Special variable **$@** means "all of the command-line arguemtns to the shell script". **$@** should also be put inside double-quotes to handle the case of arguments containing spaces. See #11 for an example. 

The `-x` flag cuases `bash` to run in debug mode. This prints out each command as it is run, which will help you to locate errors. 

# If statements and checks 

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

# Shell loops and scripts: 
- a variable named variable is later, used with $variable
- use 'echo' to print info during execution of the scripts
- ; to separate the pieces 
- save scripts in a file, say 'myscript.sh', then execute with >> bash myscript.sh 


1. For loop:  
```bash
for variable in *
do
   echo will analyze this thing next: $variable
   ls $variable
done
```

2. Check to see if a program is going to run on 'correct' files using ECHO:  
```bash
for datafile in NENE*[AB].txt
do
    echo $datafile
done
```

If correct, then:  
```bash
for datafile in NENE*[AB].txt
do
    echo $datafile
    bash program $datafile
done
```

# Example

3. Print the last 5 commands:  
```bash
history | tail -n 5
```

4. $ for species in cubane ethane methanedo; for temperature in 25 30 37 40; do; mkdir $species-$temperature; done; done

5. Command substitution with $(): to pass the list of files found to another command  
```bash
grep xxx $(find yyy)
```

6. Find all files:  
```bash
grep '^$' filename
```

7. For loop to count the number of occurences of a words in a file:  
```bash
for sis in Jo Meg Beth Amy
do
    echo $sis:
    grep -ocw $sis LittleWomen.txt
done
```  
OR  
```bash
for sis in Jo Meg Beth Amy
do
   echo $sis:
   grep -ow $sis LittleWomen.txt | wc -l
done
```

8. Brach expansion to create a directory structure in one step:  
```bash
mkdir -p zmays-snps/{data/seqs,scripts,analysis}
```

Immediately trash the standard output of a script:  
```myprogram > /dev/null```  

9. Write a shell script that takes a species as the first command-line arguemtn and a directory as the second argument. The script should return one file called *species.txt* containing a list of dates and the number of that species seens on each date.  
Input files are like this: '2013-11-05,deer,5'
```bash
grep -w $1 -r $2 | cut -d : -f 2 | cut -d , -f 1,3 > $1.txt
``` 
Run this script like this: `bash count-species.sh bear .`

10. Example of a script that takes in command line arguments called *middle.sh*.  
```bash
head -n "$2" "$1" | tail -n "$3"
```
Then, we can run this from the command line: `bash middle.sh pentane.pdb 15 5`  
"bash" says we are going to run *middle.sh*, which is a script. $1 = pentane.pdb, which is the file that we are going to run this on. $2 = 15, which is the number of lines to apply 'head' to. $3 is 5, which is the number of lines to apply 'tail' to. So this script will pull out lines #10 - 15 from pentane.pdb.  

11. Example of using a special variable in a script, $@  
```bash
# Sort filenames by their length. 
# Usage: bash sorted.sh one_or_more_filenames
wc -l "$@" | sort -n
```

12. Software Carpentry example: Leah has several hundred data files, each of which is formatted like this: '2013-11-05,deer,5'. Write a shell script that takes any number of filenames as command-line arguments, and uses `cut`, `sort`, and `uniq` to print a list of unique species appearing in each of those files separately. 
```bash
# Script to find unique species in csv files where species is the second data field
# This script accepts any number of file names as command line arguments

# Loop over all files
for file in $@
do
    echo "Unique species in $file:"
    # Extract species nams
    cut -d , -f 2 $file | sort | uniq
done
```

13. Recall recent commands and write them to a file.
```bash
history | tail -n 5 > recent.sh
```

14. Write a shell script that takes the name of a directory and a filename extension as its arguments, and prints out the name of the file with the most lines that directory with that extension. For example: 
```bash
# Shell script which takes two arguments:
#    1. a directory name
#    2. a file extension 
# and prints the name of the file in that directory
# with the most lines which matches the file extension. 
wc -l $1/*.$2 | sort -n | tail -n 2 | head -n 1
```  
Usage: `bash longest.sh /tmp/data pdb`

15. **sed** We can capture and re-sue a match: with `()`to capture a pattern and `\i` to print the ith match. For example: transform a file with lines of the form "chromosomename:startposition-endposition" to a tabular table "chromosomename startposition endposition" (3 columns separated with tabs). 
```bash
echo "chr12:74-431" | gsed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'
```  
- Prints: ch12    74    431 


# Python. 

## Python commands:
1. 
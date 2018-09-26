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
    Options: -r (recursively) -f (force)
3. **'*'** - wildcard. ? - matches exactly 1 character. 
4. **Echo** - epeat exactly what I entered in the command line.  
    echo $SHELL  
    /bin/bash
5. **cat** - print file contents to the terminal window.  
    Options: -l (in list format), -r (in reverse order), -t (ordered by time)
6. **whoami** - get your username. 
7. **mkdir** - make a directory. 
8. **rmdir** - remove a directory. 
9. **mv** - move (and rename). ```mv <from_file> <to_file```
10. **cp** - copy. ```cp <from_file> <to_file>```
11. **touch** - create a blank file. 
12. **diff** - difference. 
13. **wc** - word count.  
    Options: -l (lines), -w (words), -c (characters)
14. **less** - view part of a file in the terminal.  
    Options: - q (quit), -'return' (next line), -'space' (next page), -d (down next 1/2 page), -b (back one page), -y (back one line), -g or < (go to the first line, '4g' go to fourth line), -G or > (go to last line), -/pattern (search forward), -?pattern (search backward), -n (next: repeat previous search)
15. **sort**  
    Options: -n (numerically)
16. **head/tail** - view beginning/end of a file. -n #numberoflines.  
    Options: -f (follow)
17. **uniq** - filters out repeated lines (consecutive/adjacent lines only).  
    Options: -c (to get counts)
18. **cut** - cut and return column(s).  
    Options: -d (set the comma field as field delimiter, default = tab), -f2 (to get second field column)
19. **history** - shows the history of all previous commands, numbered. 
20. **!#** - to re-execute command # in the history. !$ for last word or last command.
21. **jobs** - see a list of jobs running.  
22. **ps** - see a list of current processes (PID = process ID)
23. **kill** - kill a job. kill -9 12167 to kill process # 12167. 
24. **top** - see all processes, refreshed, shows CPU and memory consumption. 
25. **man** - print manual of this command to see all options etc. 
26. **grep** - find things in text file  
    Options: -n (line numbers), -i (case-insensitive search), -w (whole words), -v (invert the search), -o (to get match only), -E (Extended regular expressions), -P (Perl-like regular expressions)
27. **find** - to find files, whose names match simple patterns  
    Options: -type with d or f (for directory or file), -name (with a shell pattern -say '\*.pdf'), -d (depth - eg -d 1), -mytime (for modified time)  
    find . -name '\*.txt'  

28. **!!** - retrieves immediate preceding command (same as hitting the up arrow key)
29. **more** - like less, but not as good, streams in data from a file to a terminal viewer.

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


# Python. 

## Python commands:
1. 
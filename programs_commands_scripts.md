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

## Software Carptentry Notes

### Analyzing Patient Data
- assigning variables 
- importing programs into python by using the `import` command 
- visualizing data using matplotlib.pyplot 

`data[30, 20]` accesss the element at row 30, column 20
`data[0, 0]` element in the upper left corner. If we have an MxN array in Python, its indices go from 0 to M-1 on the first axis and 0 to N-1 on the second. 

**Visualizing data**
```Python
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()
```

Key points: 
- Import a library into a program using `import libraryname`.
- Use the `numpy` library to work with arrays in Python.
- Use `variable = value` to assign a value to a variable in order to record it in memory.
- Variables are created on demand whenever a value is assigned to them.
- Use `print(something)` to display the value of `something`.
- The expression `array.shape` gives the shape of an array.
- Use `array[x, y]` to select a single element from a 2D array.
- Array indices start at 0, not 1.
- Use `low:high` to specify a slice that includes the indices from `low` to `high-1`.
- All the indexing and slicing that works on arrays also works on strings.
- Use `# some kind of explanation` to add comments to programs.
- Use `numpy.mean(array)`, `numpy.max(array)`, and `numpy.min(array)` to calculate simple statistics.
- Use `numpy.mean(array, axis=0)` or `numpy.mean(array, axis=1)` to calculate statistics across the specified axis.
- Use the `pyplot` library from `matplotlib` for creating simple visualizations.

### Repeating Actions with Loops

```Python
word = 'lead'
for char in word: 
    print(char)
```

```Python
for variable in collection: 
    do things using variable
```

We can call the `loop variable` anything we like, but there must be a colon at the end of the line starting the loop, and we must indent anything we want to run inside the loop. Unlike many other languages, there is no command to signify the end of the loop body (e.g. `end for`); what is indented after the `for` statement belongs to the loop.

Python has a built-in function called `range` that creates a sequence of numbers. range can accept 1, 2, or 3 parameters.

If one parameter is given, `range` creates an array of that length, starting at zero and incrementing by 1. For example, `range(3)` produces the numbers `0, 1, 2`.
If two parameters are given, `range` starts at the first and ends just before the second, incrementing by one. For example, `range(2, 5)` produces `2, 3, 4`.
If `range` is given 3 parameters, it starts at the first one, ends just before the second one, and increments by the third one. For exmaple `range(3, 10, 2)` produces `3, 5, 7, 9`.
Using `range`, write a loop that uses `range` to print the first 3 natural numbers:

```Python
for i in range(1,4):
    print(i)
```

```Python
result = 1
for i in range(0,3):
    result = result * 5
print(result)
```

```Python
newstring=''
oldstring='Newton'
for char in oldstring:
    newstring = char + newstring
print(newstring)
```

The built-in function `enumerate` takes a sequence (e.g. a list) and generates a new sequence of the same length. Each element of the new sequence is a pair composed of the index (0, 1, 2,…) and the value from the original sequence:
```Python
for i, x in enumerate(xs):
    # Do something using i and x
```
The above code loops through `xs`, assigning the index to `i` and the value to `x`. 

```Python
x = 5
cc = [2, 4, 3]
y = 0
for i, c in enumerate(cc):
    y = y + x**i * c
```

Key points: 
- use `for variable in sequence` to process the elements of a sequence one at a time
- the body of a `for` loop must be indented
- use `len(thing)` to determine the length of seomthing that contains other values 

### Storing multiple values in lists

Create a list: 
`odds = [1, 3, 5, 7]`

Select individual elements from lists by indexing them: 
`print(odds[0], odds[-1])`

Loop over a list: 
```Python
for number in odds: 
    print(number)
```

Strings and numbers are inmutable. This does not mean that variables with string or number values are constants, but when we want to change the value of a string or number variable, we can only replace the old value with a completely new value.
Lists and arrays, on the other hand, are mutable: we can modify them after they have been created. 
The best way to understand inmutable vs mutable is to think about lists being poinsters to data. 

Session: Have a and a = 5. Function will have it's own name-space.  
Name-space: "add1_scalar". Info from session gets copied over to name-space for this new function. Then you can perform and print the output of the function without changing what a is equal to. 

*Nested Lists* - list that contains lists. 
Python stores a list in memory so be careful when copying the name of a list and then making changes within the new list - you may change the original. 

A list can contain strings: 
```Python
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)
```
Subsets of lists and strings can be accessed by specifying ranges of values in brackets, similar to how we accessed ranges of positions in a NumPy array. Eg: 

```Python
binomial_name = "Drosophila melanogaster"
group = binomial_name[0:10]
print("group:", group)

species = binomial_name[11:24]
print("species:", species)

chromosomes = ["X", "Y", "2", "3", "4"]
autosomes = chromosomes[2:5]
print("autosomes:", autosomes)

last = chromosomes[-1]
print("last:", last)
```

Use negative indices to count elements from the end of a container (such as a list or string)
`string[-4:]`
`list[-4:]`

You can get a subset of entries in a container by adding a third argument: 
```Python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print("subset", subset)
```
> subset [2, 7, 17, 29]
You can do the same thing for strings. 

`+` usually means addition, but when used on strings or lists, it means "concatenate." 

Key points: 
- `[value1, value2, value3, ...]` creates a list
- Lists can contain nay Python object, including lists (i.e., list of lists)
- Lists are indexed and sliced with square brackets (e.g., list[0], and list[2:9]), in the same way as strings and arryas. 
- Lists are mutable (i.e., their values can be changed in place)
- Strings are immutable (i.e., the characters in them cannot be changed)

### Analyzing Data from Multiple Files

`import glob`
The `glob` library contains a function, also called `glob`, that finds files and directories whose name match a pattern. We provide pattenrs as strings: the character `*` matches zero or more characters, while `?` matches any one character. We can use this to get the names of CSV files in the current directory: 

```Python
print(glob.glob('inflammation*.csv`))
```

```Python
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('inflammation*.csv'))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = numpy.loadtxt(fname=f, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
```

Plot the difference between the average of the first dataset and the average of the second dataset, i.e., the difference between the leftmost plot of the first two figures.

```Python
import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('inflammation*.csv'))

data0 = numpy.loadtxt(fname=filenames[0], delimiter=',')
data1 = numpy.loadtxt(fname=filenames[1], delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

matplotlib.pyplot.ylabel('Difference in average')
matplotlib.pyplot.plot(data0.mean(axis=0) - data1.mean(axis=0))

fig.tight_layout()
matplotlib.pyplot.show()
```
Use each of the files once to generate a dataset containing values averaged over all patients:
```Python
filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))
for f in filenames:
    # sum each new file's data into composite_data as it's read
    #
# and then divide the composite_data by number of samples
composite_data /= len(filenames)
```
```Python
import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('inflammation*.csv')
composite_data = numpy.zeros((60,40))

for f in filenames:
    data = numpy.loadtxt(fname = f, delimiter=',')
    composite_data += data

composite_data/=len(filenames)

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(composite_data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(composite_data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(composite_data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()
```

Key points
- use `glob.glob(pattern)` to create a list of files whose names match a pattern
- use `*` in a pattern to match zero or more characters, and `?` to match any single character 

### Making Choices

We can ask Python to take different actions, depending on a condition, with an `if` statement. The second line of code uses the keyword `if` to tell Python we want to make a choise. If the test is true, the body of the `if` are executed. If the test is false, teh body of the `else` is executed instead. `elif` can be used to chain several tests together. 

To test for equality: `==` (`=` is used to assign values)
We can combine the test usign `and`, and `or`. `and` is only true if both parts are true. `or` is true if either part is true. 

`True` or `False` are special words in Python called `booleans`, which represent trutch values. A statement stuch as `1 < 0` returns the value `False`, while `-1 < 0` returns the value True. 

We can use these statements to check our script. What we are doing is asking Python to do something different, depending on the condition of our data. 
Example: 

```Python
max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
print('Seems OK!')
```

`True` and `False` booleans are not the only values in Python that are true and false. In fact, any value can be used in an `if` or `elif`.
'word is true'
'non-empty list is true'
'one is true' 

Sometimes it is useful to check whether some condition is not true. The Boolean operator `not` can do this explicitly.
'empty string is not true'
'not not True is true'

Python (and most other languages in the C family) provides in-place operators that work like this: 
```Python
x = 1  # original value
x += 1 # add one to x, assigning result back to x
x *= 3 # multiply x by 3
print(x)
```
x = 6

```Python
positive_sum = 0
negative_sum = 0
test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
for num in test_list: 
    if num > 0: 
        positive_sum += num
    elif num ==0:
        pass
    else: 
        negative_sum += num
print(positive_sum, negative_sum)
```
Here `pass` means "don't do anything". It's not really needed, but `pass` can be used in other ways as well. 

Objective: 
1. Loop over the names of the files
2. Figure out which group each filename belongs 
3. Append the filename to that list

```Python
for file in files: 
    if file.startswith('inflammation-'):
        large_files.append(file)
    elif file.startswith('small-'):
        small_files.append(file)
    else:
        other_files.append(file)
print('large_files:', large_files)
print('small_files:', small_files)
print('other_files:', other_files)
```

Write a loop that counts the number of vowels in a character string: 

```Python

vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence: 
    if char in vowels: 
        count += 1

print("The number of vowels in this string is " + str(count))
```

Key points: 
- Use `if condition` to start a conditional statement, `elif condition` to provide additional tests, and `else ` to provide a default. 
- The bodies of branches of conditional statements must be indented. 
- Use `==` to test for equality. 
- `X or Y` is only true if both `X` and `Y` are true. 
- `X or Y` is true if either `X` or `Y`, or both, are true. 
- Zero, the empty string, and the empty list are considered false; all other numbers, strings, and lists are considered true. 
- `True` and `False` represent truth values. 
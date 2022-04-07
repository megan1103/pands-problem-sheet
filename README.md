##  Programming and Scripting 
> Author: Megan O'Donovan  
> Date: 21/03/2022

### Introduction

This repository contains weekly solutions to python tasks set between January and March for the course Programming and Scripting. Weekly tasks are found on the course homepage or in the link [here](https://learnonline.gmit.ie/course/view.php?id=5057).


<summary>Week 1️⃣ ⮕ Setting up the environment</summary>
 
 - Create a Repository on Github <br/>
 - Clone repository to desktop <br/>
 - Add your scripts <br/>
 - Python Lists <br/> 
 - Commit & Push <br/>
 - Python Dictionary <br/>
 - Create a pull request to merge <br/>

<summary>Week 2️⃣ ⮕ Statements</summary>
 
 - Using VS code and running program <br/>
 - Output results <br/> 
 - Input values (insert()) <br/>
 - Comments <br/>

<summary>Week 3️⃣ ⮕  State (Variables)</summary>

  - How data is stored in a computer <br/>
  - Variable types  (int, float, string) <br/>
  - Using numeric functions (rounding decimal values to whole numbers, absolute value i.e. negative to positive, removing decimal places i.e. floor.) <br/>
  - String functions (determining the length of a string, changing characters from uppercase to lowercase.) <br/>

<summary>Week  4️⃣ ⮕ Controlling the Flow (If/While)</summary>

  - If statements (<b><i>if/ else / end</i></b> loop - If the condition is satisfied then the loop will end and executing the If block code <b><i>otherwise</i></b> if the condition is false, the else block code is executed.) <br/>
  - While statements (used to repeat a specific block of code an unknown number of times, until a condition is met.) <br/>

<summary>Week 5️⃣ ⮕ Data structures</summary>
 
 - List <br/>
 - Tuple <br/>
 - Dictionary <sup>[[1]](https://www.programiz.com/python-programming/methods/built-in/list)</sup> <br/>
 
<summary>Week 6️⃣ ⮕ Functions</summary>

  - Functions (A block of code can be assigned to a function, information can be passed into a function. The function won't output information unless called upon. Similar to <b><i>with table1 as</i></b> code.) <br/>
  - Modules (This is where a block of code from a .py file can be used in another .py file<sup>[[2]](https://www.w3schools.com/python/python_modules.asp)</sup><br/>

<summary>Week 7️⃣ ⮕ Files</summary>

  - Reading/Open (importing csv files, using open command including modes() i.e. 'r' = read, 'r+' = read & write, 'w' = write) <br/>

<summary>Week 8️⃣ ⮕ Plotting data</summary>

  - Numpy (Quicker way of formatting then lists; allowing an array, matrix or random values. <b><i>Range(Start, End)</i></b> and <b><i>Randint(Start, End, Steps)</i></b> ) <br/>
  - Matplotlib (Combined with Numpy this allows users to assign x,y coordinates and plot outcomes. Plots available on python: scatter, plot, pie, bar and hist) <br/>

  
---
###  Description
  - Week 01
     - The weekly task was to set up the needed environment i.e. downloading software and creating repositories. To test that Visual Studio was working and to understand how to generate an output, commit and merge results to github, using 'Hello World' as an example.<br/>
  - Week 02<br/>
     - The weekly task was to write a program that calculates somebody's Body Mass Index (BMI). This involved prompting the user to input values for height and weight, the program then calculates the persons BMI. The program must calculate the BMI by dividing weight(kg) by height(m<sup>2</sup>), height is also converted from cm to m<sup>2</sup>. <br/>
  - Week 03<br/>
     - The weekly task was to write a program that asks a user to input a string and outputs every second letter in reverse order. Similar to the previous week, the user is prompted in input a value. Strings can be accessed by their index in order to get the value.  [::] is used to remove characters from a sentence, index values are used as character locators in the string i.e 2 = 2<sup>nd</sup> character in the string.<br/>
  - Week 04<br/>
      - The weekly task was to write a program that asks the user to input any positive integer and outputs the successive values based on Collatz theory. Starting with a random positive number *n*, the next number in the sequence is *n/2* if n is even and *3n + 1* if n is odd. This theory creates an endless sequence, where no matter what the starting ***positive*** number is, the series will become an infinite loop of *4,2,1*. There are a number of online examples explaining this theory<sup>[[3]](https://www.webucator.com/article/collatz-conjecture-in-python)</sup>. Using a while loop to output the sequence and an if/else statement to determine if it is even, then *n/2* else, *3n+1*. Note that in python *return* only holds the new value if you assign it to a variable.<br/>
  - Week 05<br/>
     - The weekly task was to write a program that outputs whether or not today is a weekday. There are a number of different ways to determine what date today is<sup>[[4]](https://www.hellocodeclub.com/python-get-day-of-week/)</sup>. Using **datetime** to obtain the day of the week (numeric format), day name or format using timestamp<sup>[[5]](https://www.delftstack.com/howto/python/python-datetime-day-of-week/)</sup>. Using the package to get the name of the current day, then assigning Saturday &Sunday to a weekend grouping. An if statement then determined if Today() was included in the weekend grouping or not. <br/>
  - Week 06<br/>
     - The weekly task was to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. This was a complicated task and I used this lecture/tutorial as help<sup>[[6]](https://www.youtube.com/watch?v=3i9KozCUKU4&ab_channel=Skywalker)</sup>.  Another method to calculate the square root is to use Newton's Method ***NewX = 0.5 * (x + b/x)*** letting ***b*** be a given number and ***x*** an estimate of what the square root of ***b*** will be<sup>[[7]](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)</sup>. <br/>
  - Week 07<br/>
     - The weekly task was to write a program that reads in a text file and outputs the number of e's it contains, noting any assumptions. An assumption being that only lowercase characters are being counted i.e excluding upper case values. Python allows the user to read in files and then either read/write/ alter or delete said file.<br/>
  - Week 08<br/>
     - The weekly task was to write a program called plottask.py that displays a plot of the functions *f(x)=x*, *g(x)=x<sup>2</sup>* and *h(x)=x<sup>3</sup>* in the range [0, 4] on the one set of axes. [W3Schools](https://www.w3schools.com/python/matplotlib_plotting.asp) was used to improve the visualisation aspect of the plot. Numpy generates matrix or arrays more performantly then a list. ***randint(0,4,10)*** generates a random group of coordinates between 0 and 4 with 10 steps. There are a number of different plots that can be created in python. <br/>

## Solutions

| **Week No** | **Task**  | **Solution** |
| :---:| :---   | :---   |
| 1  | Setting up the environment    | https://github.com/megan1103/pands-problem-sheet|
| 2  | Statements  | https://github.com/megan1103/pands-problem-sheet/tree/main/Week02|
| 3  | State (Variables)  | https://github.com/megan1103/pands-problem-sheet/tree/main/Week03|
| 4  | Controlling the Flow (If/While) |https://github.com/megan1103/pands-problem-sheet/tree/main/Week04|
| 5  | Data structures  |https://github.com/megan1103/pands-problem-sheet/tree/main/Week05|
| 6  | Functions  |https://github.com/megan1103/pands-problem-sheet/tree/main/Week06|
| 7  | Files | https://github.com/megan1103/pands-problem-sheet/tree/main/Week07|
| 8  | Plotting data  |https://github.com/megan1103/pands-problem-sheet/tree/main/Week08 |

## References
<br /> - *[1] :* https://www.programiz.com/python-programming/methods/built-in/list <br />
<br /> - *[2] :* https://www.w3schools.com/python/python_modules.asp <br />
<br /> - *[3] :* https://www.webucator.com/article/collatz-conjecture-in-python/ <br />
<br /> - *[4] :* https://www.hellocodeclub.com/python-get-day-of-week/ <br />
<br /> - *[5] :* https://www.delftstack.com/howto/python/python-datetime-day-of-week/ <br />
<br /> - *[6] :* https://www.youtube.com/watch?v=3i9KozCUKU4&ab_channel=Skywalker <br />
<br /> - *[7] :* https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ <br />
<br /> - *[8] :* https://www.pythonpool.com/collatz-sequence-python/ <br /> 


>> Code Explanation<br />
      <br /> Week 01
      <br /> `string = "Hello Would" `  *Declaring a string variable.*
      <br /> `print(string)` *Outputs the result.*
      <br /> `string = "Hello!! \nMy name is: \t Megan" ` *Spaces can also be added: "\t" is a tab, "\n" is a new line, and "\r" is a carriage return.*<br />
      <br /> Week 02
      <br />  `height = int(input('Enter height(cm):')) `   *Prompts the users to input a value.*
      <br />  `newheight = (height/100)**2  ` *Change centimetres to meters squared.* <br/>
      <br /> Week 03
      <br />  `input('Please enter a sentence: ')` 
      <br />  `print(firstString[:3]) `   *This will give the first 3 letters of the sentence.*
      <br />  `print(firstString[-3:]) `   *This will give the last 3 letters of the sentence.*
      <br />  `print(firstString[2::]) `   *This will remove the first 2 letters of the sentence.*
      <br />  `print(firstString[2::]) `   *This will remove the first 2 letters of the sentence.*
      <br />  `print(firstString[1::2]) `  *This will remove every second letter, starting from the second.*
      <br />  `print(firstString[2::3]) `  *This will remove every third letter, starting from the third.*
      <br />  `print(firstString[::-1]) `  *This will reverse all the letters of the sentence.* <br/>
      <br />Week 04
      <br /> ` while n > 1:`  <br /> ` collatz(n) `   *This will cause an infinite loop*
      <br /> `while n > 1: `  <br /> ` n = collatz(n) `   *Assigning n rectifies the bug* <sup>[[8]](https://www.pythonpool.com/collatz-sequence-python/)</sup>. <br/>
      <br /> Week 05
      <br /> ` curr_date = date.today()`   *Outputs the current date and name of day.*
      <br /> ` currentDay = print(calendar.day_name[curr_date.weekday()])` *Takes only the name of the date, not the date format.* <br/>
      <br /> Week07
      <br /> `open( , "r")`  *Opens a file for reading.*
      <br /> `file.read()`   *Reads the contents of the imported file.*
      <br /> `str.lower(file.read())`  *Reads in the imported file and converts all characters to lower case.* <br/>
      <br /> Week 08
      <br /> ` plt.plot(xpoints,xpoints, label = "straight line", color = 'blue')`  *Line Chart*
      <br /> ` plt.hist(normData) `  *Histogram*
      <br /> ` plt.pie(normData, labels = fruit) ` *Pie Chart*
      <br /> ` plt.scatter(xpoints,ypoints, label ="random") `  *Scatter Plot*<br />



  

##  Programming and Scripting 
> Author: Megan O'Donovan  
> Date: 21/03/2022

### Introduction

This repository contains weekly solutions to python tasks set between January and March for the course Programming and Scripting. Weekly tasks are found on the course homepage or in the link [here](https://learnonline.gmit.ie/course/view.php?id=5057).

### Summary

- **Setting up the environment**
  - Create a Repository on Github
  - Clone repository to desktop
  - Add your scripts
  - Commit & Push
  - Create a pull request to merge 
 
- **Statements**
   - Using VS code and running program
   - Output results (print())
   - Input values (insert())
   - Comments
    
- **State (Variables)**
   - How data is stored in a computer
   - Variable types  (int, float, string)
   - Using numeric functions (rounding decimal values to whole numbers, absolute value i.e. negative to positive, removing decimal places i.e. floor.)
   - String functions (determining the length of a string, changing characters from uppercase to lowercase.)

- **Controlling the Flow (If/While)**
   - If statements (*if/ else / end* loop - If the condition is satisfied then the loop will end and executing the If block code **otherwise** if the condition is false, the else block code is executed.)
   - While statements (used to repeat a specific block of code an unknown number of times, until a condition is met.)
    
- **Data structures**
   - List/Tuple/Dictionary[^1]

 - **Functions**
   - Functions (A block of code can be assigned to a function, information can be passed into a function. The function won't output information unless called upon. Similar to ***with table1 as*** code.)
   - Modules (This is where a block of code from a .py file can be used in another .py file[^2]

 - **Files**
   - Reading/Open (importing csv files, using open command including modes() i.e. 'r' = read, 'r+' = read & write, 'w' = write)

 - **Plotting data**
   - Numpy (Quicker way of formatting then lists; allowing an array, matrix or random values. *Range(Start, End)* and *Randint(Start, End, Steps)* )
   - Matplotlib (Combined with Numpy this allows users to assign x,y coordinates and plot outcomes. Plots available on python: scatter, plot, pie, bar and hist)


###  Description
  - Explanation of the python code used in the weekly tasks.
    - Week 01
      - The weekly task was to set up the needed environment i.e. downloading software and creating repositories. To test that Visual Studio was working and to understand how to generate an output, commit and merge results to github, using 'Hello World' as an example. 
     - Week 02
       - The weekly task was to write a program that calculates somebody's Body Mass Index (BMI). This involved prompting the user to input values for height and weight, the program then calculates the persons BMI. The program must calculate the BMI by dividing weight(kg) by height(m<sup>2</sup>), height is also converted from cm to m<sup>2</sup>. 
      - Week 03
        - The weekly task was to write a program that asks a user to input a string and outputs every second letter in reverse order. Similar to the previous week, the user is prompted in input a value. [::] is used to remove characters from a sentence, numeric values are used to assign character location in the string i.e 2 = 2<sup>nd</sup> character in the string.
       - Week 04
          - The weekly task was to write a program that asks the user to input any positive integer and outputs the successive values based on Collatz theory. Starting with a random positive number *n*, the next number in the sequence is *n/2* if n is even and *3n + 1* if n is odd. This theory creates an endless sequence, where no matter what the starting ***positive*** number is, the series will become an infinite loop of *4,2,1*. There are a number of online examples explaining this theory[^3]. Using a while loop to output the sequence and an if/else statement to determine if it is even, then *n/2* else, *3n+1*. Note that in python *return* only holds the new value if you assign it to a variable.
       - Week 05
            - The weekly task was to write a program that outputs whether or not today is a weekday. There are a number of different ways to determine what date today is[^5]. Using **datetime** to obtain the day of the week (numeric format), day name or format using timestamp[^6]. Using the package to get the name of the current day, then assigning Saturday &Sunday to a weekend grouping. An if statement then determined if Today() was included in the weekend grouping or not.
       - Week 06
          - The weekly task was to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. This was a complicated task and I used this lecture/tutorial as help.[^7]  Another method to calculate the square root is to use Newton's Method ***NewX = 0.5 * (x + b/x)*** letting ***b*** be a given number and ***x*** an estimate of what the square root of ***b*** will be.[^8]  
       - Week 07
            - The weekly task was to write a program that reads in a text file and outputs the number of e's it contains, noting any assumptions. An assumption being that only lowercase characters are being counted i.e excluding upper case values. Python allows the user to read in files and then either read/write/ alter or delete said file.
       - Week 08
          - The weekly task was to write a program called plottask.py that displays a plot of the functions *f(x)=x*, *g(x)=x<sup>2</sup>* and *h(x)=x<sup>3</sup>* in the range [0, 4] on the one set of axes. [W3Schools](https://www.w3schools.com/python/]) was used to improve the visualisation aspect of the plot. Numpy generates matrix or arrays more performantly then a list. ***randint(0,4,10)*** generates a random group of coordinates between 0 and 4 with 10 steps. There are a number of different plots that can be created in python.

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
[^1]: https://www.programiz.com/python-programming/methods/built-in/list
[^2]: https://www.w3schools.com/python/python_modules.asp
[^3]: https://www.webucator.com/article/collatz-conjecture-in-python/
[^4]: https://www.pythonpool.com/collatz-sequence-python/
[^5]: https://www.hellocodeclub.com/python-get-day-of-week/
[^6]: https://www.delftstack.com/howto/python/python-datetime-day-of-week/
[^7]: https://www.youtube.com/watch?v=3i9KozCUKU4&ab_channel=Skywalker
[^8]: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

>> Code Explanation
      <br /> Week 02
      <br />  `height = int(input('Enter height(cm):'))`  *Prompts the users to input a value.*
      <br /> `newheight = (height/100)**2` *Change centimetres to meters squared.*<br />
      <br /> Week 03
      <br />  `input('Please enter a sentence: ')` 
      <br />  `print(firstString[2::]) `   *This will remove the first 2 letters of the sentence.*
      <br />  `print(firstString[1::2]) `  *This will remove every second letter, starting from the second.*
      <br />  `print(firstString[2::3]) `   *This will remove every third letter, starting from the third.*
      <br />  `print(firstString[::-2]) `   *To change the direction of the string, include a minus sign.<br />*
      <br />Week 04
      <br /> ` while n > 1:`  <br /> ` collatz(n) `   *This will cause an infinite loop*
      <br /> `while n > 1: `  <br /> ` n = collatz(n) `   *Assigning n rectifies the bug.[^4]<br />*
      <br /> Week 05
      <br /> ` curr_date = date.today()`   *Outputs the current date and name of day.*
      <br /> ` currentDay = print(calendar.day_name[curr_date.weekday()])` *Takes only the name of the date, not the date format.<br />*
      <br /> Week07
      <br /> `open( , "r")`  *Opens a file for reading.*
      <br /> `file.read()`   *Reads the contents of the imported file.*
      <br /> `str.lower(file.read())`  *Reads in the imported file and converts all characters to lower case.<br />*
      <br /> Week 08
      <br /> ` plt.plot(xpoints,xpoints, label = "straight line", color = 'blue')`  *Line Chart*
      <br /> ` plt.hist(normData) `  *Histogram*
      <br /> ` plt.pie(normData, labels = fruit) ` *Pie Chart*
      <br /> ` plt.scatter(xpoints,ypoints, label ="random") `  *Scatter Plot*<br />


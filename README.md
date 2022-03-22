##  Programming and Scripting 
> Author: Megan O'Donovan  
> Date: 21/03/2022

### Description

This repository contains weekly solutions to python tasks set between January and March for the course Programming and Scripting. Weekly tasks are found on the course homepage or in the link [here](https://learnonline.gmit.ie/course/view.php?id=5057).

### Course Summary

- **Setting up the enviroment**
  - Create a Repository on Github
  - Clone repository to desktop
  - Add your scripts
  - Commit & Push
  - Create a pull request to merge 
 
- **Statements**
   - Using VScode and running program
   - Output results (print())
   - Input values (insert())
   - Comments
    
- **State (Variables)**
   - How data is stored in a computer
   - Variable types  (int, float,string)
   - Using numeric functions (rounding decimal values to whole numbers, absolute value i.e negative to positive, removing the decimal places i.e floor)
   - String functions (determining the length of a string, changing characters from uppercase to lower)

- **Controlling the Flow (If/While)**
   - If statements (*if/ else / end* loop - If the condition is satisifed then the loop will end and excuting the If block code *otherwise* if the condition is false, the else block code is executed)
   - While statements (used to repeat a specific block of code an unknown number of times, until a condition is met)
    
- **Data structures**
   - List/Tuple/Dictionary[^1]

 - **Functions**
   - Functions (A block of code can be assigned to a function, information can be passed into a function. The function won't output information unless called upon. Similar to *with table1 as code*)
   - Modules (This is where a block of code from a py file can be used in another py file[^2]

 - **Files**
   - Reading/Open (importing csv files, using open command including modes() i.e 'r' = read, 'r+' = read&write, 'w' = write)

 - **Plotting data**
   - Numpy (Quicker way of formatting then list, allowing an array, matrix or random values. Range(StartPoint,EndPoint)...Randint(StartPoint,EndPoint,NumberofSteps) )
   - Matplotlib (Combined with Numpy this allows use to assign x,y coorindates and plot outcomes; scatter, plot, pie, bar and hist)


## Projects

| **Week No** | **Task**                                                                                                                                | **Solution**                                                  |
| :---:| :---   | :---   |
| 1  | Setting up the environment                                   | https://github.com/megan1103/pands-problem-sheet                |
| 2  | Statements                                              | https://github.com/megan1103/pands-problem-sheet/tree/main/Week02              |
| 3  | State (Variables)                                           | https://github.com/megan1103/pands-problem-sheet/tree/main/Week03                 |
| 4  | Controlling the Flow (If/While)                                                  |https://github.com/megan1103/pands-problem-sheet/tree/main/Week04   |
| 5  | Data structures                                   |https://github.com/megan1103/pands-problem-sheet/tree/main/Week05|
| 6  | Functions                                            |https://github.com/megan1103/pands-problem-sheet/tree/main/Week06|
| 7  | Files                                      | https://github.com/megan1103/pands-problem-sheet/tree/main/Week07|
| 8  | Plotting data                                  |https://github.com/megan1103/pands-problem-sheet/tree/main/Week08 |

## Python Code
  - Explanation of the python code used in the weekly tasks.
    - Week 01
      - The weekly task was to set up the needed enviroment i.e downloading software and creating repositories. To test that Visual Studio was working and to understand how to generate an output, commit and merge results to github, we used 'Hello World' as an example. 
     - Week 02
       - The weekly task was to write a program that calculates somebody's Body Mass Index (BMI). This involved prompting the user to input values for height and weight, the program then calculates the persons BMI. The program must calculate the BMI by dividing weight(kg) by height(m<sup>2</sup>), height is also convert from cm to m<sup>2</sup>. The original height is inputted and then divided by 100 and squared: 
         <br />  ```height = int(input('Enter height(cm):'))```
         <br />  ```newheight = (height/100)**2 ```
      - Week 03
        - The weekly task was to write a program that asks a user to input a string and outputs every second letter in reverse order. Similar to the previous week, the user is prompted in input a value, unlike last week we do not need to wrap the input in an *int* since we are inputting a string. [::] is used to remove letters from a sentence, we include a numeric value depending on what letters we want removed.
          <br />  ```firstString = input('Please enter a sentence: ') ```
          <br />  ```print(firstString[2::]) ```    *This will remove the first 2 letters of the sentence*
          <br />  ```print(firstString[1::2]) ```   *This will remove every second letter, starting from the second*
          <br />  ```print(firstString[2::3]) ```   *This will remove every third letter, starting from the third*
          <br />  ```print(firstString[::-2]) ```   *To change the direction of the string, we include a minus sign*
       - Week 04
          - The weekly task was to write a program that asks the user to input any positive integer and outputs the successive values based on Collatz theory. Starting with a random positive number n, the next number in the sequence is n/2 if n is even and 3n + 1 if n is odd. This theory creates an endless sequence, where no matter what the starting number is, the series will become an infinite loop of 4,2,1. There are a number of online examples explaining this theory[^3]. We use a while loop to output the squence and an if/else statement to determine if it is even, we change it to n/2 else, we change it to 3n+1. Note that *return* only holds the new value if you assign it to a variable
            <br /> ``` while n > 1:```  <br /> ``` collatz(n) ```   *This will cause an infinite loop*
            <br /> ```while n > 1: ```  <br /> ``` n = collatz(n) ```   *Assigning n recifies the bug*[^4]
       - Week 05
            - The weekly task was to write a program that outputs whether or not today is a weekday. There are a number of different ways to determine what date today is[^5]. Using *datetime* allows users to look at day of the week number, day name or format using timestamp[^6]. I used the packpage to get the name of the current day, then I assigned Sat&Sun to a weekend grouping. An if statement then determined if Today() was included in the weekend grouping or not.
              <br /> ``` curr_date = date.today()```   *Getting the current date and name of day*
              <br /> ``` currentDay = print(calendar.day_name[curr_date.weekday()])```  *Takes only the name of the date, not the date format*
       - Week 06
          - The weekly task was to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. This was a complicated task and I used this leacture/tutorial as help.[^7]    
       - Week 07
            - The weekly task was to write a program that reads in a text file and outputs the number of e's it contains, noting any assumptions. The only assumption I made was that I was being asked to only find lower case e values i.e excluding upper case values. Python allows the user to read in files and then either read/write/ alter or delete said file. The command:
              <br /> ``` Open( , "r") ```   allows the user to open a file for reading, while 
               <br /> ``` file.read() ```    reads the contents of the imported file. The assumpt I made is that I am to ignore uppercase E values, if this was not the case then 
               <br /> ``` str.lower(file.read())```   would read in the imported file and convert all characters to lower case.
       - Week 08
          - The weekly task was to write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x<sup>2</sup> and h(x)=x<sup>3</sup> in the range [0, 4] on the one set of axes. [W3Schools](https://www.w3schools.com/python/]) was used to improve the visualastion aspect of the plot. Numpy is used to generate matrix or arrays more proformatly then a list. I used *randint(0,4,10)* to generate a random group of coordinates between 0 and 4 with 10 steps. There are a number of different plots that can be created in python:
             <br /> ``` plt.plot(xpoints,xpoints, label = "straight line", color = 'blue')```  *Line Chart*
             <br /> ``` plt.hist(normData) ```  *Histogram*
             <br /> ``` plt.pie(normData, labels = fruit) ``` *Pie Chart*
             <br /> ``` plt.scatter(xpoints,ypoints, label ="random") ```  *Scatter Plot* 


## References
[^1]: https://www.programiz.com/python-programming/methods/built-in/list
[^2]: https://www.w3schools.com/python/python_modules.asp
[^3]: https://www.webucator.com/article/collatz-conjecture-in-python/
[^4]: https://www.pythonpool.com/collatz-sequence-python/
[^5]: https://www.hellocodeclub.com/python-get-day-of-week/
[^6]: https://www.delftstack.com/howto/python/python-datetime-day-of-week/
[^7]: https://www.youtube.com/watch?v=3i9KozCUKU4&ab_channel=Skywalker

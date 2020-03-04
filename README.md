# Probability-Programs
The scripts for [Introduction to Probability by Charles M. Grinstead and J. Laurie Snell](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/book.html) ported to python  
  
## Setup
### Linux
Install Python 3.x and git  
  
Make sure pip for python 3 is installed  
`pip3 --version` should not print an error  
  
Install pipenv via pip  
`pip install --user pipenv`  

Clone the repo  
`git clone git@github.com:FireLemons/Probability-Programs.git`  
  
Install the project dependencies  
`cd Probability-Programs`  
`pipenv install`  
**this may take several minutes**

Install tkinter to be able to display graphs
`sudo apt install python3-tk`

### Windows  
Help wanted  
  
## Running Programs  
run `pipenv shell` in the project folder to start a subshell with all the dependencies loaded  
  
In the subshell `python3 name_of_program.py` will run a program.  
Most programs require arguments(user input usually a number).  
If the arguments are erroneous a usage hint will be printed.  
The same usage hint is also at the top of each program file.

## Contributing  
This repo aims to port the wolfram mathematica programs found [here](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/BookAlgorithms.html) to python.  
  
When editing programs please keep in mind they may need to be modified by someone who may not have a background in programming.  
  
As of now I only plan to port standalone programs. Help for porting mathematica notebook files to jupyter notebook would be greatly appreciated.

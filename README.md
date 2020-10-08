# Probability-Programs
The scripts for [Introduction to Probability by Charles M. Grinstead and J. Laurie Snell](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/book.html) ported to python  
  
## Setup
Install Python 3.8 and git  
  
Other versions of python 3.X may work  
To install using a different version of python, open Pipfile in a text editor and edit the version number  
    [requires]
    python_version = "3.8"

### Linux
Make sure pip for python 3 is installed  
`pip3 --version` should not print an error  
  
Install pipenv via pip  
`pip3 install --user pipenv`  

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
  
### MacOS  
Help Wanted  
  
## Running Programs  
run `pipenv shell` in the project folder to start a subshell with all the dependencies loaded  
  
In the subshell, run a program by typing `python3 name_of_program.py`.  

## Contributing  
This repo aims to port the wolfram mathematica programs found [here](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/BookAlgorithms.html) to python.  
  
When I first discovered the book, I went to download the programs and saw that they were all written in proprietary languages so I decided to prot the programs to python.  
  
When editing programs please keep in mind they may need to be modified by someone who may not have a background in programming.  
  
For the near future I only plan to port standalone programs. In the future I would like to port the mathematica notebook files to jupyter notebook.

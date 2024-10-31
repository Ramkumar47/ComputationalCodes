# Alphabet statistics program
The task is to read books and estimate the number of each alphabet being
used per line and then to generate the distribution graph for each alphabet

## prerequisites
The programs were developed in Python3 language and it requires following
modules to be present for its execution
- numpy
- pandas
- matplotlib
- pypdf

## program execution instruction
- place the necessary pdf files in the "books/" directory
- Open script_reader.py file in an editor and specify the names of books
    in the "bookNames" list.
- Specify the starting and ending page numbers within which the phrases has to be
read, in the variables "pageStart" and "pageEnd". Then save and close the python file.
- Execute the script_reader.py python file, it will read each pdf file and
  extract line-wise data of each alphabet, then store them in linewise_data/
  directory
- Then execute the postProcessing.py script file, it will generate the distribution
plots (Histograms) for each alphabet.

The generated histograms can be found as png files in the histograms/ directory.

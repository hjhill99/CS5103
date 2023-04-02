# Running project.py

The program will read a .txt file and count the instances of each unique word, the number of lines, and the number of characters. To run it, the file it is reading must be in the same directory as the script and must be named "example.txt" (must be a txt file). It can then be executed using any Python IDE or by using Python from the terminal. I will most likely change it to have the user input the name of their file in the future. 

The code reads the file, removes any newline and tab characters (replaces them with spaces as a way of using them as separators), and then creates a dictionary where the keys are the unique words and the values are the counts of those words. It also counts the lines and characters in the file, and displays these alongside the word count dictionary.

# Unit Tests

There are five unit tests in the unit_tests.py script. The first one checks whether a word is in the word count dictionary, and the second checks if that word is counted the correct number of times. The third checks the line count and the fourth checks the character count. There is a fifth one that tests if the document is empty or not. The first four require prior knowledge of what is in the document in order to accurately test the code. 

unit_tests.py can be run the same way as project2.py, and will display the results of the unit tests instead of the word, line, and character counts. 

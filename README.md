# Running project.py

The program will read a .txt file and count the instances of each unique word. The file it is reading must be in the same directory as the script and must be named "example.txt" (must be a txt file). I will most likely change this to have the user input the name of their file in the future. 

The code reads the file, removes any newline and tab characters (replaces them with spaces as a way of using them as separators), and then creates a dictionary where the keys are the unique words and the values are the counts of those words. It then displays this dictionary.

# Unit Tests

There are two unit tests currently in the code. The first one checks if a certain word is found as a key in the dictionary, succeeding if it is and failing if it is not. The word it is checking for is one known to be in the document, so if it fails that means the script did not read the file properly. The second test checks whether or not the count for certain words in the document are correct. If it fails, that means the words were not counted properly.

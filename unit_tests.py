import unittest
# First update for the project, adds the character and line counts of the document
class Counts:    
    def __init__(self, filename):        
        # Initializes object to have empty word, line, and character counts to be filled by other functions        
        self.Lines = None
        self.WordCount = None
        self.LineCount = None
        self.CharCount = None
        
        self.get_counts(filename)
        
    # Reads lines from selected document
    def read_doc(self, filename):
        
        with open(filename, 'r+') as f:
            lines = f.readlines()
         
        self.Lines = lines
        #return lines
    
    # Replaces all newline and tab characters with spaces
    def clean_lines(self):
        
        newlines = []
        
        for line in self.Lines:
            line = line.replace('\n', ' ')
            line = line.replace('\t', ' ')
            if line == '' or line == ' ':
                pass
            else:
                newlines.append(line)
         
        self.Lines = newlines
        #return newlines
    
    # Counts the individual words in the document and creates a dictionary of the structer {word: word_count}
    def count_words(self):
        
        word_count = {}
        
        for line in self.Lines:
            line_words = line.split(' ')
        
            for x in line_words:
                if x.lower() in word_count.keys():
                    word_count[x.lower()] += 1
                else:
                    word_count[x.lower()] = 1
                
        word_count.pop('')
        
        self.WordCount = word_count     
    
    # Counts the number of individual lines
    def count_lines(self):
        
        self.LineCount = len(self.Lines)
    
    # Counts the number of characters, not counting spaces, newlines, or tabs
    def count_chars(self):
        
        CharCount = 0
        for line in self.Lines:
            line = line.replace(' ', '')
            CharCount += len(line)
            
        self.CharCount = CharCount
    
    # Reads the document, cleans the lines, and gets the word, line, and character counts
    def get_counts(self, filename):
        
        self.read_doc(filename)
        self.clean_lines()
        
        self.count_words()
        self.count_lines()
        self.count_chars()
    
    # Displayes the word, line, and character counts
    def display_counts(self):
        print("Word count: ", self.WordCount)
        print("-----------------")
        print("Line count: ", self.LineCount)
        print("-----------------")
        print("Character count: ", self.CharCount)
##################################################################
class TestCountWords(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_doc = Counts('example.txt')
        #print(self.WordCount)
        
    def test_word_present(self):      
        self.assertIn("example", self.test_doc.WordCount.keys(), "Word not in count")
        
        
    def test_word_count(self):
        self.assertEqual(self.test_doc.WordCount.get("example"), 6, "Count is not correct")
        
    def test_line_count(self):
        self.assertEqual(self.test_doc.LineCount, 14, "Line count is not correct")
        
    def test_char_count(self):
        self.assertEqual(self.test_doc.CharCount, 2143, "Character count is not correct")
      
        
        



unittest.main()

import unittest
class Counts:
    
    def __init__(self, filename, old_word, new_word):
        
        # Initializes object to have empty word, line, and character counts to be filled by other functions
        
        self.Lines = None
        self.WordCount = None
        self.LineCount = None
        self.CharCount = None
        self.NewWords = None
        
        self.get_counts(filename, old_word, new_word)
        
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
    

        
    def replace_word(self, old_word, new_word):
        
        doc_words = []
        new_doc_words = []
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        for line in self.Lines:
            words = line.split(' ')
            for word in words:

                for x in word:
                    if x in punc:
                        word = word.replace(x, "")

                if word == ' ' or word == '':
                    pass
                else:
                    doc_words.append(word)
           
        for word in doc_words:
            #print(word.lower())
            if word.lower() == old_word:
                word = word.replace(word, new_word)
                new_doc_words.append(word)
                #print(word)
            else:
                new_doc_words.append(word)
                
        self.NewWords = new_doc_words
                    
        #print(new_doc_words)
                
    # Reads the document, cleans the lines, and gets the word, line, and character counts
    def get_counts(self, filename, old_word, new_word):
        
        self.read_doc(filename)
        self.clean_lines()
        
        self.count_words()
        self.count_lines()
        self.count_chars()
        self.replace_word(old_word, new_word)
        
        self.display_counts()
    
    # Displays the word, line, and character counts
    def display_counts(self):
        print("Word count: ", self.WordCount)
        print("-----------------")
        print("Line count: ", self.LineCount)
        print("-----------------")
        print("Character count: ", self.CharCount)
        print("-----------------")
        print("New words after replacement: ", self.NewWords)
##################################################################
class TestCountWords(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_doc = Counts('example.txt', 'for', 'newword')
        #print(self.WordCount)
        
    def test_word_present(self):      
        self.assertIn("example", self.test_doc.WordCount.keys(), "Word not in count")       
        
    def test_word_count(self):
        self.assertEqual(self.test_doc.WordCount.get("example"), 6, "Count is not correct")
        
    def test_line_count(self):
        self.assertEqual(self.test_doc.LineCount, 14, "Line count is not correct")
        
    def test_char_count(self):
        self.assertEqual(self.test_doc.CharCount, 2143, "Character count is not correct")
        
    def test_doc_empty(self):
        self.assertGreater(len(self.test_doc.Lines), 0, "Document is empty")
        
    def test_word_replacement(self):
        self.assertIn("newword", self.test_doc.NewWords, "Word not in document")
      

unittest.main()

# Count # of instances of each unique word in document
# Support space, tab, and newline as separators
import unittest

def count_words(filename):
    
    with open(filename, 'r+') as f:
        clean_lines = []
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.replace('\t', ' ')
            clean_lines.append(line)   

    
    word_count = {}
    
    for line in clean_lines:
        line_words = line.split(' ')
        
        for x in line_words:
            if x.lower() in word_count.keys():
                word_count[x.lower()] += 1
            else:
                word_count[x.lower()] = 1
                
    word_count.pop('')
        
    return word_count


class TestCountWords(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dict = count_words('example.txt')
        
    def test_word_present(self):      
        self.assertIn("example", self.dict.keys(), "Word not in count")
        
        
    def test_word_count(self):
        self.assertEqual(self.dict.get("example"), 6, "Count is not correct")
        self.assertEqual(self.dict.get("male"), 5, "Count is not correct")
        
        

doc_words = count_words('example.txt')

print("Word counts in document: ", doc_words)

unittest.main()
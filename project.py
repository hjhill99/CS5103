# Count # of instances of each unique word in document
# Support space, tab, and newline as separators

def read_file(filename):
    
    with open(filename, 'r+') as f:
        clean_lines = []
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.replace('\t', ' ')
            clean_lines.append(line)
            
            
        
    return clean_lines

def count_words(lines):
    
    #words = []
    
    word_count = {}
    
    for line in lines:
        line_words = line.split(' ')
        
        for x in line_words:
            if x.lower() in word_count.keys():
                word_count[x.lower()] += 1
            else:
                word_count[x.lower()] = 1
                
    word_count.pop('')
        
    return word_count
    

doc_lines = read_file('test_doc.txt')

doc_words = count_words(doc_lines)

print(doc_lines)
print("Doc words; ", doc_words)
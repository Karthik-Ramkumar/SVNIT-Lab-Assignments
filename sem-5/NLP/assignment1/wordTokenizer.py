import re

pattern = re.compile(r'''
https?://[^\s]+|                                
www\.[^\s]+|                                
^\w+@\w+\.\w+$|  
\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|                  
\d+\.\d+|                                       
\d+|                                      
[\u0900-\u097F]+|                             
[A-Za-z]+|                                      
[^\w\s]                                     
''', re.VERBOSE) # used for formating regex in more than one line 


def word_tokenize(sentence):
    return pattern.findall(sentence)


input_file = "sentence_tokenized.txt"
output_file = "word_tokenized.txt"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for sentence in infile:

        sentence = sentence.strip()

        if not sentence:
            continue

        tokens = word_tokenize(sentence)

        for token in tokens:
            outfile.write(token + "\n")

        outfile.write("\n")

print("Word tokenization completed.")
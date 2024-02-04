#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re

Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
Sample Text- 'Python Exercises, PHP exercises.'
Expected Output: Python:Exercises::PHP:exercises:

# In[3]:


Text='Python Exercises, PHP exercises.'
sol=re.sub(r"[ ,.]",":",Text)
print(sol)

Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
Expected output-
0      hello world
1             test
2    four five six

# In[8]:


data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)
df['SUMMARY'] = df['SUMMARY'].replace(to_replace=r'[^a-zA-Z ]|\s+|XXXXX', value=' ', regex=True).str.strip()

print(df)


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[9]:


def findwords(input_string):
    pattern = re.compile(r'\b\w{4,}\b')
    matches = pattern.findall(input_string)
    return matches
text = "This is a sample text with words of varying lengths."
result = findwords(text)
print(result)

Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# In[11]:


def words(input_string):
    pattern = re.compile(r'\b\w{3,5}\b')
    matches = pattern.findall(input_string)
    return matches
inputt = "This isi a sample text with words of varying lengths."
result = words(inputt)
print(result)

Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World
Data Scientist

# In[15]:


def remove_parentheses(strings):
    pattern = re.compile(r'\(|\)')
    return [pattern.sub('', string) for string in strings]

strings = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

result = remove_parentheses(strings)
print(result)

Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

# In[17]:


with open('C:\\Users\\Lucif\\OneDrive\\Desktop\\Sample Text.txt', 'r') as file:
    contents = file.read()
pattern = re.compile(r'\s*\([^)]*\)')
result = pattern.sub('', contents)

print(result)

Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

# In[18]:


text = "ImportanceOfRegularExpressionsInPython"
pattern = re.compile(r'[A-Z][a-z]*')
result = pattern.findall(text)
print(result)

Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[19]:


def insert_spaces(text):
    pattern = re.compile(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)')
    result = pattern.sub(' ', text)
    return result
text = "RegularExpression1IsAn2ImportantTopic3InPython"

output = insert_spaces(text)
print(output)

Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[20]:


def insert_spaces(text):
    
    pattern = re.compile(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|(?<=[0-9])(?=[A-Za-z])')
    result = pattern.sub(' ', text)
    return result
text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)

Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv


# In[23]:


url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].str[:6]

print(df.head())

Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# In[26]:


def match_string(input_string):
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    if pattern.match(input_string):
        return True
    else:
        return False
input_string = "Abc123_def"
print(match_string(input_string))  

Question 12- Write a Python program where a string will start with a specific number
# In[27]:


def start_with_number(input_string, number):
    pattern = re.compile(r'^' + str(number))
    if pattern.match(input_string):
        return True
    else:
        return False


input_string = "123abc"
number = 1
print(start_with_number(input_string, number))  

Question 13- Write a Python program to remove leading zeros from an IP address


# In[28]:


def remove_leading_zeros(ip_address):
    new_ip = re.sub(r'\b0+(\d+)', r'\1', ip_address)
    return new_ip

ip_address = "192.168.001.001"
print(remove_leading_zeros(ip_address))  

Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format.

# In[29]:


with open("C:\\Users\\Lucif\\OneDrive\\Desktop\\file1.txt") as file:
    text = file.read()

pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th) \d{4}')

date = pattern.search(text).group()
print(date)  

Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

# In[30]:


def search_literals(input_string, *words):
    for word in words:
        if word in input_string:
            print(f'"{word}" found in the string.')
        else:
            print(f'"{word}" not found in the string.')


input_string = 'The quick brown fox jumps over the lazy dog.'
search_literals(input_string, 'fox', 'dog', 'horse')

Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

# In[31]:


def search_literal_and_location(input_string, word):
    if word in input_string:
        print(f'"{word}" found in the string at index {input_string.find(word)}.')
    else:
        print(f'"{word}" not found in the string.')


input_string = 'The quick brown fox jumps over the lazy dog.'
search_literal_and_location(input_string, 'fox')

Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.

# In[34]:


def find_substrings(input_string, pattern):
    substrings = re.findall(pattern, input_string)
    return substrings


input_string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
print(find_substrings(input_string, pattern)) 

Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
# In[35]:


def find_occurrence_and_position(input_string, pattern):
    matches = re.finditer(pattern, input_string)
    for match in matches:
        print(f'Found "{match.group()}" at index {match.start()}')

input_string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_occurrence_and_position(input_string, pattern)

Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# In[36]:


from datetime import datetime

def convert_date_format(input_date):
    date_obj = datetime.strptime(input_date, '%Y-%m-%d')
    return date_obj.strftime('%d-%m-%Y')

input_date = '2023-12-31'
print(convert_date_format(input_date)) 

Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# In[37]:


def find_decimal_numbers(input_string):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    return pattern.findall(input_string)

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
print(find_decimal_numbers(sample_text)) 

Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[38]:


def separate_and_print_numbers(input_string):
    for index, char in enumerate(input_string):
        if char.isdigit():
            print(f"Number: {char}, Position: {index + 1}")

input_string = "abc123def456"
separate_and_print_numbers(input_string)

Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
Expected Output: 950
# In[39]:


def extract_max_numeric_value(input_string):
    numbers = re.findall(r'\d+', input_string)
    max_number = max(map(int, numbers))
    return max_number

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
print(extract_max_numeric_value(sample_text)) 

Question 23- Create a function in python to insert spaces between words starting with capital letters.
Sample Text: “RegularExpressionIsAnImportantTopicInPython"
Expected Output: Regular Expression Is An Important Topic In Python
# In[40]:


def insert_spaces(input_string):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', input_string)

sample_text = "RegularExpressionIsAnImportantTopicInPython"
print(insert_spaces(sample_text))  

Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# In[41]:


def find_upper_lower_sequence(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    return pattern.findall(input_string)

input_string = "TheQuickBrownFoxJumpsOverTheLazyDog"
print(find_upper_lower_sequence(input_string))  

Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
Sample Text: "Hello hello world world"
Expected Output: Hello hello world
# In[42]:


def remove_duplicate_words(input_string):
    pattern = re.compile(r'\b(\w+)(\s+\1)+\b')
    return pattern.sub(r'\1', input_string)

input_string = "Hello hello world world"
print(remove_duplicate_words(input_string)) 

Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.
# In[43]:


def accept_string(input_string):
    pattern = re.compile(r'^.*[a-zA-Z0-9]$')
    if pattern.match(input_string):
        return True
    else:
        return False
    
input_string = "abc123"
print(accept_string(input_string)) 

Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# In[44]:


def extract_hashtags(input_text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(input_text)
    return hashtags

input_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
print(extract_hashtags(input_text)) 

Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[45]:


def remove_symbols(input_text):
    pattern = re.compile(r'<U\+\w{4}>')
    return pattern.sub('', input_text)

input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
print(remove_symbols(input_text))  

Question 29- Write a python program to extract dates from the text stored in the text file.
Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
Note- Store this sample text in the file and then extract dates.
# In[46]:


with open("C:\\Users\\Lucif\\OneDrive\\Desktop\\Ron.txt") as file:
    text = file.read()

pattern = re.compile(r'\b\d{1,2}-\d{1,2}-\d{4}\b')

dates = pattern.findall(text)
print(dates)

Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.
Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[47]:


def remove_words(input_string):
    pattern = re.compile(r'\b\w{2,4}\b')
    return pattern.sub('', input_string)

input_string = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(remove_words(input_string)) 


# In[ ]:





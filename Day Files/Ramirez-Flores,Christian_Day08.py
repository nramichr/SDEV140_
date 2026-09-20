"""
Day 8

Use the provided input file 'cleantext.txt' that was output of today's demo to get a count of how many times a particular word occurs in the passage.  
Read the file contents into a string variable and do a split into individual word list based on a blank space delimiter.  
Reference P453 in section 8.3 for explanation of the split string method.

Once you have your string list created.  
You can sort it in preparation to count the words and how many times they have occurred in the passage.  
Reference p375 in section 7.5 for coverage on list methods  including sorting.  
The result of the (ASCII) sort will group all like words together to enable a search and tally for your final analysis and display of each word that occurs and how many times it shows up.

"""

with open("cleantext.txt", "r") as infile:
    text = infile.read()

words = text.split(" ")

words.sort()

if len(words) > 0:
    count = 1
    for i in range (1, len(words)):
        if words[i] == words[i-1]:
            count += 1
        else:
            print(words[i-1], count)
            count = 1
        print(words[-1], count)

print("Christian Ramirez-Flores")
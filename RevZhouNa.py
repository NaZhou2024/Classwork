# Top Documentation
"""
# Name: Na Zhou  
# Date: 3/17/2025
# Module: 03REV – Review Python Fundamentals
# Description: A vowel counter program that counts how many vowels are in the text that user inputs"
"""

# CONSTANTS
TITLE = "Welcome to vowel counter program!" 
PROMPT = "Enter any text: " 
LINE = '-' 
REPORT_LIST = ["VOWEL COUNT REPORT: ", "Vowel", "Count", "Total"]

def main():
    print(TITLE) # Get text string input
    print(LINE * len(TITLE)) # Create divider line equal to title length
    text = input(PROMPT).upper() # Capitalize the string in order to compare with AEIOU
    vDict, total = findVowelCount(text) # Calling findVoweCount function to update the original values
    generateReport(vDict, total) # Print in a preferred format

def findVowelCount(text): # find vowels and count the numbers of each vowel
    vDict = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0} # initialize vDict dictionary
    total = 0
    for char in text: # extract element from string to compare
        if char in vDict: # update dictionary with counts
            vDict[char] += 1
            total += 1
    return vDict, total
    
def generateReport(vDict, total): # generate a report of results
    print(f"\n{REPORT_LIST[0]}") # print the report title "VOWEL COUNT REPORT"
    print(LINE * len(REPORT_LIST[0])) # print divider lines
    print(f"{REPORT_LIST[1]:<10}{REPORT_LIST[2]:>10}") # print subtitle align to left and right
    print(LINE * len(REPORT_LIST[0])) # print divider lines
    for vowel, count in vDict.items(): # print each vowel and its count values
        print(f"{vowel:<10}{count:>10}")
    print(LINE * len(REPORT_LIST[0])) # print divider lines
    print(f"{REPORT_LIST[3]:<10}{total:>10}") # print total values for all vowels
    print(LINE * len(REPORT_LIST[0])) # print divider lines

main()
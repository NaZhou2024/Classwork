#Name: Na Zhou  
#Date: 3/17/2025
#Module: 03REV – Review Python Fundamentals
#Description: A vowel counter program that counts how many vowels are in the text that user inputs

#CONSTANTS
TITLE = "Welcome to vowel counter program!"
PROMPT = "Enter any text: "
LINE = '-'
REPORT_LIST = ["VOWEL COUNT REPORT: ", "Vowel", "Count", "Total"]

def main():
    print(TITLE)
    print(LINE * len(TITLE))
    text = input(PROMPT).upper()
    vDict, total = findVowelCount(text)
    generateReport(vDict, total)

def findVowelCount(text):
    text = list(text)
    vDict = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    total = 0
    for char in text:
        if char in vDict:
            vDict[char] += 1
            total += 1
    return vDict, total
    
def generateReport(vDict, total):
    print(f"\n{REPORT_LIST[0]}")
    print(LINE * len(REPORT_LIST[0]))
    print(f"{REPORT_LIST[1]:<10}{REPORT_LIST[2]:>10}")
    print(LINE * len(REPORT_LIST[0]))
    for vowel, count in vDict.items():
        print(f"{vowel:<10}{count:>10}")
    print(LINE * len(REPORT_LIST[0]))
    print(f"{REPORT_LIST[3]:<10}{total:>10}")
    print(LINE * len(REPORT_LIST[0]))

main()
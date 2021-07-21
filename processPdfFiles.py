import PyPDF2
import re
import os

path = 'testfiles'
incomeTextList = [] 
totalIncomeTextList = []
totalDeducations = 0

#2. PROCESS THE TEXT FROM THE PDF FILE AND PRODUCT RESULTED INCOME NUMBER
def extractIncomeText(txt):
    data = txt.split()
    wordsOfInterest = []
    incomeStr =""
    for word in data:
        if("INCOME" in word):
            # add the word to the list
            wordsOfInterest.append(word)
    for x in range(len(wordsOfInterest)):
        if("GST" in wordsOfInterest[x]):
           #print(wordsOfInterest[x])
            # Remove the text before dollar amount
            newWord =wordsOfInterest[x][12:]
            # Remove the text after the dollar amount
            incomeStr = newWord.split('P')[0]
    return incomeStr
 
def extractSubTotalText(txt):
    data = txt.split()
    wordsOfInterest = []
    finalSubTotalIncomeText =""
    
    for word in data:
        if("SUB-TOTAL" in word):
            # add the word to the list
            wordsOfInterest.append(word)
    for x in range(len(wordsOfInterest)):
        if("OTHER" in wordsOfInterest[x]):
            # Remove the text before dollar amount
            newWord =wordsOfInterest[x][12:]
            # Remove the text after the dollar amount
            splittedWords = newWord.split("-")
            removeTotalText = splittedWords[1][7:]
            subTotalIncomeTexts =removeTotalText.split("OTHER")
            finalSubTotalIncomeText = subTotalIncomeTexts[0]
    return finalSubTotalIncomeText
 
 
def computeTotal(incomeTxtList):
    totalIncome = 0.0
    for i in range(len(incomeTxtList)):
        # Convert incomeText to number 
        income = float(incomeTxtList[i])
        totalIncome += income
    return totalIncome
 
# 3. ADD THE INCOME NUMBER TO THE LIST OF INCOMES (FOR EACH FILE) SO THAT ENTRIES SHOULD BE EQUAL TO LIST SIZE/LENGTH
#print(processPdfText(text))
for filename in os.listdir(path):
    #with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
    print("------NOW PROCESSING FILE "+filename+"-----------")
    # do your stuff
    fullfilepath = path+"/"+filename
    #print(fullfilepath)
    pdf_file = open(fullfilepath, 'rb')
    #with open(os.path.join(os.getcwd(), filename), 'r') as f:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    #1. PROCESS THE PDF FILE AND EXTRACT ALL TEXT
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    #print (page_content.encode('utf-8'))
    print("------------------------------------------")
    text = page_content.encode('utf-8')
    # To string
    text = text.decode('utf-8')
    # Add the income for the month (current file being processed)
    incomeTextList.append(extractIncomeText(text))
    # Add the Sub-total income for the month (current file being processed)
    totalIncomeTextList.append(extractSubTotalText(text))
    potentialDeducations = float(extractSubTotalText(text)) - float(extractIncomeText(text))
    totalDeducations += potentialDeducations
    print("Sub-total Income: "+extractSubTotalText(text) +" Deductions: "+str(potentialDeducations) +" Income: "+extractIncomeText(text)+" for "+filename)
    
print("--------------------------------FINAL RESULT-------------------------------------------------------")        
print("Grand Total: " + str(computeTotal(totalIncomeTextList))+" Total Deducations: "+str(totalDeducations)+" Total Income: "+str(computeTotal(incomeTextList)))
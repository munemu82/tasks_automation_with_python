# 1. Automating Text Extraction and key figures summarization from PDF files
One of my friends is a driver for uber and DIDI, one day asked me if I could write a script for him to extract Sub-total income, income and deducations from the DIDI monthly Tax summary PDF. This was for his Tax return logdment since DIDI at the time I am writing this did not provide annual Tax summary for driver's income. So I spent few hours reading through the PDF files and figuring out the variable and constant text and came up with a script (see file processPdfFiles.py). To run this script you need to install PyPDF2 python package using Pip install. Then run, the script as -> python processPdfFiles.py
The result should be as shown below (using the provided test files)
![image](https://user-images.githubusercontent.com/13115110/126506559-c0f4c5fb-549b-45ea-88db-ee7551162282.png)


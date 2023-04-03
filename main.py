# pip install PyPDF2
temp = 1
from PyPDF2 import PdfReader

reader = PdfReader("Выписка по кредитной карте (на русском).pdf")
number_of_pages = len(reader.pages)
for num in range(0, number_of_pages):

    print(number_of_pages)
    page = reader.pages[num]
    # text = page.extract_text()
    text = page.extract_text()

    splited_text = text.split('\n')

    for line in splited_text:
        print(line)
        temp += 1

print(temp)
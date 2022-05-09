#! python3
import PyPDF2


#####################################################
# Extracting text from PDF
# pdfFileObj = open('combinedminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)

# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

#####################################################
# Decrypting PDF

# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# print(pdfReader.isEncrypted) # return True as it is encrypted
# pdfReader.getPage(0) # Will error as its not yet been decrypted

# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb')) # Has to be reopened due to a bug. 
# pdfReader.decrypt('rosebud')
# pageObj = pdfReader.getPage(0)
# print(pageObj)

#####################################################
# Creating PDF -> copying pages

# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# pdfWriter = PyPDF2.PdfFileWriter()

# for pageNum in range(pdf1Reader.numPages):
# 	pageObj = pdf1Reader.getPage(pageNum)
# 	pdfWriter.addPage(pageObj) # addPage only adds pages to the end

# for pageNum in range(pdf2Reader.numPages):
# 	pageObj = pdf2Reader.getPage(pageNum)
# 	pdfWriter.addPage(pageObj) # addPage only adds pages to the end

# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close() 
# pdf1File.close()
# pdf2File.close()

#####################################################
# Creating PDF -> rotating pages

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateClockwise(90)

# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile = open('rotatedPage-OUTPUT.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

#####################################################
# Creating PDF -> overlaying pages

# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)

# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)

# for pageNum in range(1, pdfReader.numPages):
# 	pageObj = pdfReader.getPage(pageNum)
# 	pdfWriter.addPage(pageObj)

# resultPdfFile = open('waterMarkedCover-OUTPUT.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

#####################################################
# Creating PDF -> Encrypting PDF's

# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdfFileWriter()

# for pageNum in range(pdfReader.numPages):
# 	pdfWriter.addPage(pdfReader.getPage(pageNum))

# pdfWriter.encrypt('swordfish') # used for both user pword and owner pword. A 2nd argument will set the owner pword
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()











































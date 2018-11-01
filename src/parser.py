import PyPDF2

def loadPage(pageNum):
    pdfFileObj = open('../pdfs/fourier.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    print(pdfReader.getPageLayout())

    pageObj = pdfReader.getPage(pageNum)
    print(pageObj.extractText())

    pdfFileObj.close()


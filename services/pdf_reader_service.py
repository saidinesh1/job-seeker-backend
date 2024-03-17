from pypdf import PdfReader

def Pdf_Reader(pdf):
    reader = PdfReader(pdf)
    print(len(reader.pages))
    text=""
    for page in reader.pages:
        text+= page.extract_text()
    return text

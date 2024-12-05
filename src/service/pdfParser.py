from pdfminer.high_level import extract_text
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PDFMinerLoader
from langchain_community.document_loaders import PDFPlumberLoader


class PDFParserService():
    def __init__(self):
        pass
    
    def parse(self, file_path: str):
        text = extract_text(file_path)
        if text.find("EVERGREEN") != -1:
            print("load by pyPDF")
            return PyPDFLoader(file_path).load()
        elif text.find("YANG MING LINE") != -1:
            print("load by pdfminer")
            return PDFMinerLoader(file_path).load()
        elif text.find("CMA CGM") != -1:
            print("load by pdfplumber")
            return PDFPlumberLoader(file_path).load()
        elif text.find("Hapag-Lloyd") != -1:
            print("load by pyPDF")
            return PyPDFLoader(file_path).load()
        else:
            print("load by pdfplumber")
            return PDFPlumberLoader(file_path).load()
    
    def load_by_pyPDF(self, file_path: str):
        print("load by pyPDF")
        return PyPDFLoader(file_path).load()
    
    def load_by_pdfminer(self, file_path: str):
        print("load by pdfminer")
        return PDFMinerLoader(file_path).load()
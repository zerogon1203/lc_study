from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from typing import List
from langchain_chroma import Chroma
from langchain_community.document_loaders import PDFMinerLoader
import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json
from pathlib import Path
class ChromaDBService:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.db = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embeddings,
            collection_name="my_db"
        )
        
    def add_documents(self, documents):
        self.db.add_documents(documents=documents)
        
    def similarity_search(self, query: str, k: int = 3):
        self.db.get()
        return self.db.as_retriever(search_kwargs={"k": k}).invoke(query)
    
    def get_collection(self):
        return self.db.get()
    
    def add_json_documents(self, file_path: str):
        data = json.loads(Path(file_path).read_text())
        print(data)
        # self.add_documents(docs)

    def add_pdf_documents(self):
        for file in glob.glob("assets/*.PDF"):
            loader = PDFMinerLoader(file)
            docs = loader.load()
            print(docs)   
            
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=125,
                length_function=len,
                is_separator_regex=False,
            )
            docs = splitter.split_documents(docs)
            self.add_documents(docs)

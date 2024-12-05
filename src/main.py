from langchain_ollama import OllamaLLM
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from model.output import Output
from service.pdfParser import PDFParserService
from langchain_core.output_parsers import StrOutputParser

from langsmith import traceable

from pathlib import Path
import glob
class ChatBot():
    def __init__(self):
        self.model = OllamaLLM(model="qwen2.5:14b", keep_alive=0, temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=Output)
        
    @traceable
    def chat(self, file_path: str):
        template = Path("src/prompt/make_markdown.md").read_text()
        file = PDFParserService().parse(file_path)
        if "RATE INFO" in file:
            file = file.split("RATE INFO")[0]

        prompt_template = PromptTemplate(
            template=template,
            input_variables=["question", "format"],
        )
        
        chain = prompt_template | self.model 
        result = chain.invoke({"question": file, "format": self.parser.get_format_instructions()})
        return result
    
    @traceable
    def summrize(self, file_path: str):
        template = Path("src/prompt/summarize.md").read_text()
        docs = PDFParserService().parse(file_path)
        prompt_template = PromptTemplate(
            template=template,
        )
        chain = prompt_template | self.model | StrOutputParser()
        result = chain.batch(docs)
        
        reduce_template = Path("src/prompt/reduce.md").read_text()
        reduce_prompt_template = PromptTemplate(
            template=reduce_template,   
            input_variables=["doc_summaries", "format"],
        )
        reduce_chain = reduce_prompt_template | self.model
        result = reduce_chain.invoke({"doc_summaries": result, "format": self.parser.get_format_instructions()})
        return result
if __name__ == "__main__":
    bot = ChatBot()
    files = glob.glob("assets/*.PDF")
    i = 0
    for file in files:
        print(f"{i} : {file.split('/')[-1]}")
        i += 1
    while True:
        try:
            message = input("파일 번호를 입력해주세요: ")
            file_index = int(message)
            if file_index < 0 or file_index >= len(files):
                print(f"0부터 {len(files)-1} 사이의 숫자를 입력해주세요.")
                continue
            break
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    result = bot.summrize(files[file_index])
    print(result)
    # message = input("질문을 입력하세요: ")
    # result = bot.chat(message)
    # print(result)
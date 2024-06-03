# encoding: utf-8
"""
 RAG for estate advertisement
"""
import os

from langchain_openai import OpenAIEmbeddings

from pipeline.custom_document_loader import CustomDocumentLoader
from pipeline.rag import RAG
from utils import consts, file_utils
from utils.vectorstore_utils import (create_vectorstore_with_save,
                                     load_vectorstore)

if __name__ == "__main__":

    embeddings = OpenAIEmbeddings()

    persist_directory = os.path.join(consts.PERSIST_DIR, "estate_ad/demo")

    if file_utils.is_dir_empty(persist_directory):
        # Load the data from the custom source
        FILE_DIR = "/Users/wangqiang/Downloads/15-临安蓝城·春风燕语/2-文案创作/2020"
        file_map = file_utils.aggregate_files_in_dir(FILE_DIR)
        file_list = file_map["docx"]

        loader = CustomDocumentLoader(file_list)
        docs = loader.load()

        vectorstore = create_vectorstore_with_save(
            docs, embeddings, persist_directory)
    else:
        vectorstore = load_vectorstore(persist_directory, embeddings)

    rag = RAG(vectorstore)

    # Invoke the RAG pipeline
    response = rag.invoke("给一个合院取一个名字")
    print(response["answer"])

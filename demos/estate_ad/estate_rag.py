# encoding: utf-8
"""
    estate rag
"""
import os

from langchain_openai import OpenAIEmbeddings

from pipeline.custom_document_loader import CustomDocumentLoader
from pipeline.rag import RAG
from utils import consts, file_utils
from utils.vectorstore_utils import (create_vectorstore_with_save,
                                     load_vectorstore)


class EstateRag:
    """
        estate rag
    """

    def __init__(self, file_dir: str) -> None:
        embeddings = OpenAIEmbeddings()

        persist_directory = os.path.join(consts.PERSIST_DIR, "estate_ad/demo")

        if file_utils.is_dir_empty(persist_directory):
            # Load the data from the custom source
            file_map = file_utils.aggregate_files_in_dir(file_dir)
            file_list = file_map["docx"]

            loader = CustomDocumentLoader(file_list)
            docs = loader.load()

            vectorstore = create_vectorstore_with_save(
                docs, embeddings, persist_directory)
        else:
            vectorstore = load_vectorstore(persist_directory, embeddings)

        self.rag = RAG(vectorstore)

    def invoke(self, query: str) -> dict:
        return self.rag.invoke(query)

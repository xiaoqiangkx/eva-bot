# encoding: utf-8
"""
    RAG samples
"""
from typing import List

from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


class RAG:
    """
    RAG samples
    """

    def __init__(self, vectorstore: Chroma) -> None:
        self.vectorstore = vectorstore

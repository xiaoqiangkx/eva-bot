# encoding: utf-8
"""
    Utility functions for vectorstore
"""


from typing import List
from langchain_chroma import Chroma
from langchain_core.embeddings.embeddings import Embeddings
from langchain_core.documents import Document


def create_vectorstore_with_save(docs: List[Document], embedding_function: Embeddings, persist_directory: str) -> Chroma:
    """
    Save the vectorstore to a file

    Args:
        vectorstore (Chroma): the vectorstore to save
        path (str): the path to save the vectorstore
    """
    return Chroma.from_documents(docs, embedding_function,
                                 persist_directory=persist_directory)


def load_vectorstore(persist_directory: str, embedding_function: Embeddings) -> Chroma:
    """
    Load the vectorstore from a file

    Args:
        path (str): the path to the vectorstore file

    Returns:
        Chroma: the loaded vectorstore
    """
    return Chroma(persist_directory=persist_directory, embedding_function=embedding_function)

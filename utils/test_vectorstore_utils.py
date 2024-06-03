# encoding: utf-8
"""
    Utility functions for vectorstore
"""
import pytest
from langchain_core.documents import Document
from langchain_chroma import Chroma
from utils import consts
import os
from utils.vectorstore_utils import create_vectorstore_with_save, load_vectorstore
from langchain_openai import OpenAIEmbeddings


def test_save_load_vectors():
    """
        test save laod vectors
    """
    docs = [
        Document(page_content="中国",
                 metadata={"source": "doc1"}),
        Document(page_content="美国",
                 metadata={"source": "doc2"}),
    ]

    embeddings = OpenAIEmbeddings()

    persist_directory = os.path.join(consts.PERSIST_DIR, "estate_ad/tmp")
    # vectorstore: Chroma = create_vectorstore_with_save(
    #     docs, embeddings, persist_directory)

    loaded_vectorstore: Chroma = load_vectorstore(
        persist_directory, embeddings)

    # assert vectorstore.similarity_search("china") == "中国"
    assert loaded_vectorstore.similarity_search(
        "china")[0].page_content == "中国"

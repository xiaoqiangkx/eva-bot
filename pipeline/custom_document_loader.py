# encoding: utf-8
"""
Customer Document Loader used for langchain
"""
from typing import Iterator, List
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from unstructured.partition.docx import partition_docx
from unstructured.documents.elements import Element


class CustomDocumentLoader(BaseLoader):
    """
        Load the data from the custom source
    """

    def __init__(self, file_paths: List[str]) -> None:
        """Initialize the CustomDocumentLoader with a file path

        Args:
            file_path (str): the path to the file
        """
        self.file_paths = file_paths

    def lazy_load(self) -> Iterator[Document]:
        """
            Load the data from the file
        """
        for file_path in self.file_paths:
            elements: List[Element] = partition_docx(filename=file_path)
            yield Document(
                page_content="\n".join([element.text for element in elements]),
                metadata={"source": file_path}
            )

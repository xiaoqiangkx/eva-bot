# encoding: utf-8
"""
Customer Document Loader used for langchain
"""
from pathlib import Path
import pytest
from pipeline.custom_document_loader import CustomDocumentLoader
from utils import consts

TEST_DATA_DIR = Path(consts.ROOT_DIR) / "datasets" / "tests"


class TestCustomDocumentLoader:
    """
        Test the CustomDocumentLoader
    """
    @pytest.mark.parametrize("file_paths", [[
        str(TEST_DATA_DIR / "20191106-蓝城·春风燕语立冬海报文案.docx"),
        str(TEST_DATA_DIR / "20200110-蓝城·春风燕语价值海报.docx"),
    ]])
    def test_custom_document_loader(self, file_paths):
        """
            test the custom document loader
        """
        custom_document_loader = CustomDocumentLoader(file_paths)
        documents = list(custom_document_loader.lazy_load())
        assert len(documents) == 2
        # assert documents[0].page_content == "This is a test document"
        # assert documents[1].page_content == "This is another test document"
        assert documents[0].metadata["source"] == str(TEST_DATA_DIR /
                                                      "20191106-蓝城·春风燕语立冬海报文案.docx")
        assert documents[1].metadata["source"] == str(TEST_DATA_DIR /
                                                      "20200110-蓝城·春风燕语价值海报.docx")

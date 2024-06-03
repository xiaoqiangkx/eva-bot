# encoding: utf-8
"""
Customer Document Loader used for langchain
"""
from pathlib import Path
import logging
import pytest
from pipeline.custom_document_loader import CustomDocumentLoader
from utils import consts

TEST_DATA_DIR = Path(consts.ROOT_DIR) / "datasets" / "tests"

logger = logging.getLogger(__name__)


class TestCustomDocumentLoader:
    """
        Test the CustomDocumentLoader
    """
    @pytest.mark.parametrize("file_paths", [[
        str(TEST_DATA_DIR / "a.docx"),
        str(TEST_DATA_DIR / "b.docx"),
    ]])
    def test_custom_document_loader(self, file_paths):
        """
            test the custom document loader
        """
        custom_document_loader = CustomDocumentLoader(file_paths)
        documents = list(custom_document_loader.lazy_load())
        assert len(documents) == 2
        logging.info(documents[0].page_content)
        assert documents[0].page_content == "价值海报文案\n一方轩阔明朗地下室\n向下生长的深度修为\n延展居者生活的层次"
        assert documents[1].page_content == "logo\n暖阳踏着青黄的韵脚\n捎来新冬的消息"
        assert documents[0].metadata["source"] == str(TEST_DATA_DIR /
                                                      "a.docx")
        assert documents[1].metadata["source"] == str(TEST_DATA_DIR /
                                                      "b.docx")

# encoding: utf-8
"""utility functions for unstructured data
"""
from typing import List
from unstructured.documents.elements import Element
from unstructured.partition.docx import partition_docx


def show_data(elements: List[Element]):
    """show data
    """
    for element in elements:
        print(element.text)
    return


if __name__ == "__main__":
    filename: str = "/Users/wangqiang/Downloads/15-临安蓝城·春风燕语/2-文案创作/2019/20191106-蓝城·春风燕语立冬海报文案.docx"
    element_data: List[Element] = partition_docx(filename=filename)
    show_data(element_data)

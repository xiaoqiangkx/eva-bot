# encoding: utf-8
"""
"""
import os
from utils.file_utils import is_dir_empty
from utils.consts import PERSIST_DIR


def test_is_dir_empty():
    """
    test is_dir_empty
    """
    assert is_dir_empty(os.path.join(PERSIST_DIR, "estate_ad")) is False
    assert is_dir_empty(os.path.join(PERSIST_DIR, "empty")) is True

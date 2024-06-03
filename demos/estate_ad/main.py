# encoding: utf-8
"""
 RAG for estate advertisement
"""
from utils import file_utils


if __name__ == "__main__":
    # Load the data from the custom source
    FILE_DIR = "/Users/wangqiang/Downloads/15-临安蓝城·春风燕语/2-文案创作/2020"
    file_map = file_utils.aggregate_files_in_dir(FILE_DIR)
    file_list = file_map["docx"]

# encoding: utf-8
"""
 RAG for estate advertisement
"""
from demos.estate_ad.estate_rag import EstateRag


if __name__ == "__main__":
    FILE_DIR = "/Users/wangqiang/Downloads/15-临安蓝城·春风燕语/2-文案创作/2020"
    rag = EstateRag(FILE_DIR)

    # Invoke the RAG pipeline
    response = rag.invoke("给一个合院取一个名字")
    print(response["answer"])

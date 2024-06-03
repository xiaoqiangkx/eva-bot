# encoding: utf-8
"""
    RAG samples
"""
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.base import Runnable

from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


class RAG:
    """
    RAG samples
    """

    def __init__(self, vectorstore: Chroma) -> None:
        self.vectorstore = vectorstore
        self.retriever = vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 2})

        system_prompt = (
            "You are an assistant for copy writer. "
            "Use the following pieces of retrieved context to create a response. "
            "\n\n"
            "{context}"
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        self.rag_chain = create_retrieval_chain(
            self.retriever, question_answer_chain)

    def invoke(self, msg: str) -> Runnable:
        """
            Invoke the RAG pipeline
        """
        return self.rag_chain.invoke({"input": msg})

# encoding: utf-8
import pandas as pd
import json


def main():
    final_data = []

    # Load the data
    with open("../datasets/raw/train.json") as f:
        data: dict = json.load(f)
        for row in data["rows"]:
            final_data.append({
                "question": row["row"]["question"],
                "answer": row["row"]["answer"]
            })

    df: pd.DataFrame = pd.read_csv(
        "../datasets/raw/FAQs.csv", index_col=False).fillna("")
    for row in df.iterrows():
        question = row[1]["question"]
        answer = row[1]["answer"].replace("\n", "").replace("\u00a0", "")

        if answer:
            final_data.append({
                "question": question,
                "answer": answer
            })

    final_question = []
    final_answer = []

    for item in final_data:
        final_question.append(item["question"])
        final_answer.append(item["answer"])

    # Save the data
    pd.DataFrame({
        "question": final_question,
        "answer": final_answer
    }).to_csv("../datasets/faq.csv", sep="\t", index=False)
    return


if __name__ == '__main__':
    main()

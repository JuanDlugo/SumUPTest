from load_data import load_data
from answer_questions import answer_questions
from fetch_uf import fetch_and_store_uf

if __name__ == "__main__":
    load_data()
    fetch_and_store_uf()
    answer_questions()

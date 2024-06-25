import sqlite3
import sqlite_vss
from json import dumps
from openai import OpenAI

# OpenAI クライアントの初期化
client = OpenAI()

# SQLiteデータベースに接続
conn = sqlite3.connect("text.db")
cursor = conn.cursor()

# vector0とvss0拡張をロード
conn.enable_load_extension(True)
sqlite_vss.load(conn)

def get_embedding(text, model="text-embedding-3-large", dimensions=1536):
    text = text.replace("\n", " ")
    params = {"model": model, "input": [text], "dimensions": dimensions}
    response = client.embeddings.create(**params)
    return response.data[0].embedding

def find_similar_documents(query, limit=10):
    query_embedding = get_embedding(query)

    search_query = """
    SELECT documents.content, vss_documents.distance
    FROM vss_documents
    JOIN documents ON documents.id = vss_documents.rowid
    WHERE vss_search(vss_documents.embedding, vss_search_params(?, ?))
    ORDER BY vss_documents.distance
    """

    result = conn.execute(search_query, (dumps(query_embedding), limit)).fetchall()
    return result

def main():
    print("既存のデータベースを使用して類似文書を検索します。")

    query = "日本"

    results = find_similar_documents(query)

    if results:
        print("\n類似した文書:")
        for content, distance in results:
            print(f"内容: {content}")
            print(f"距離: {distance}\n")
        

    conn.close()

if __name__ == "__main__":
    main()
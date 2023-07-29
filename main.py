import logging
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

logging.basicConfig(level=logging.INFO)

openai.api_key = 'YOUR_OPENAI_KEY'
faiss_index_filename = 'INDEX_FILE_NAME'
embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key)
faiss_index = FAISS.load_local(faiss_index_filename, embeddings)
num_results = 5

while True:
    search_query = input("Enter search query (the core concept you're interested in): ")
    chat_query = input("Enter chat query (the question you want to ask the model): ")

    if search_query.lower() == 'exit' or chat_query.lower() == 'exit':
        break

    try:
        # Retrieve top 5 documents from the index most related to the search_query
        docs = faiss_index.similarity_search(search_query, k=num_results)
        docs_text = "\n".join([page.page_content for i, page in enumerate(docs)])

        if chat_query:
            # Create messages for the chat model
            messages = [
                {"role": "system", "content": f"You are a helpful assistant that knows a lot about:\n{docs_text}"},
                {"role": "user", "content": chat_query}
            ]

            # Call OpenAI's chat model
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

            print("Response: ", response.choices[0].message.content)
        else:
            print("Relevant Document Contents: ", docs_text)

    except Exception as e:
        logging.error(f"Error processing queries. Search query: {search_query}, chat query: {chat_query}. Error: {str(e)}")

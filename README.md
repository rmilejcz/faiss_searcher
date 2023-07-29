# Document Query Chat Assistant Using OpenAI

This repository contains `main.py`, a Python script which interacts with the user, accepting a search query and optionally a chat query. The script retrieves documents most related to the search query from a pre-existing FAISS index (the process to create this index can be found at this [repository](https://github.com/rmilejcz/faiss_builder)), and uses these documents to inform an OpenAI chat model to generate a response. This application functions as a chat assistant, providing answers based on specific document sets.

## Prerequisites

Please ensure that you have installed:

- Python 3.6+
- `logging` Python library.
- `openai` Python library.
- `langchain` Python library version 0.1+. This library provides `FAISS` vector store and `OpenAIEmbeddings`.

You can install these dependencies with the following pip command:

```bash
pip install logging openai langchain
```

## Usage

To run the script, perform the following steps:

1. Clone this repository to your local machine.

    ```bash
    git clone <repo_url>
    ```

2. Replace `'YOUR_OPENAI_KEY'` in the script with your OpenAI key. If you do not want to send data to OpenAI API, leave this as an empty string.

    ```python
    openai.api_key = 'YOUR_OPENAI_KEY'
    ```

3. Replace `'INDEX_FILE_NAME'` with the name of your FAISS index file.

    ```python
     faiss_index_filename = 'INDEX_FILE_NAME'
    ```

4. Run the script.

    ```bash
    python main.py
    ```

The script interface prompts you to input a "search query" (core concept you're interested in) and optionally a "chat query" (the question to ask the OpenAI model). When a chat query is provided and an OpenAI key is set up, the script retrieves relevant documents from your FAISS index, uses them to inform the OpenAI chat model, and the response is then presented. When a chat query is not provided or an OpenAI key is not set up, the script provides a list of the relevant documents based on your search query.

Enter `exit` as either the search query or chat query to stop the script.

## License

This project is released under the [Unlicense](https://unlicense.org/), granting uncheckered freedom to use, modify, and distribute this project as you see fit.

# Question Answering with Langchain and RAGatouille

This project demonstrates how to use Langchain and RAGatouille to build a question answering system. It allows users to ask questions based on a given dataset and retrieves relevant answers using natural language processing techniques.

## Features

- Load and split data from a text or pdf file
- Create a RAG (Retrieval Augmented Generation) model for retrieving relevant information
- Generate answers to user questions based on the loaded data
- User-friendly web interface powered by Gradio

## Installation

1. Clone the repository: <kbd>https://github.com/jerryola1/RAG-with-ColBERT.git</kbd>

2. Install the required dependencies: <kbd>pip install -r requirements.txt</kbd>

3. Set up the OpenAI API key:
- Sign up for an API key at [OpenAI](https://www.openai.com/)
- Set the API key as an environment variable named `OPENAI_API_KEY`

## Usage

1. Prepare your dataset:
- Create a text file named `data.txt` containing the data you want to use for question answering
- Place the `data.txt` file in the same directory as the script

2. Run the script: <kbd>python app.py</kbd>

3. Open the provided URL in your web browser to access the Gradio interface

4. Type your question in the text input field and press Enter

5. The answer based on the loaded data will be displayed below

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Langchain](https://github.com/hwchase17/langchain)
- [RAGatouille](https://github.com/microsoft/RAGatouille)
- [Gradio](https://github.com/gradio-app/gradio)

## Contact

If you have any questions or inquiries, please contact [olagunjujeremiah@gmail.com](mailto:olagunjujeremiah@gmail.com).
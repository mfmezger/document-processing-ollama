"""The OllamaService class provides a wrapper for the Ollama class."""
from langchain.llms import Ollama


class OllamaService:
    """Base class for OllamaService."""

    def __init__(self):
        """Initialization of the Connection to the Ollama API."""
        self.llm = Ollama(model="mistral:instruct")

    def extract_json(self, text):
        """Extracts JSON data from a given text."""

    def extract_markdown(self, text):
        """Extracts Markdown data from a given text."""

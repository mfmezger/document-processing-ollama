"""This classes handle the loading of documents from a given path."""
from abc import ABC, abstractmethod

from langchain.document_loaders import DirectoryLoader, PyPDFium2Loader, TextLoader


class AbstractDocumentExtractor(ABC):
    """Abstract class for document extraction."""

    def __init__(self, path, format="utf-8"):
        """Constructor for AbstractDocumentExtractor.

        Args:
            path (_type_): _description_
            format (str, optional): _description_. Defaults to "utf-8".
        """
        self.path = path
        self.format = format

    @abstractmethod
    def extract_documents(self) -> list:
        """Abstract method for extracting documents."""


class PDFDocumentExtractor(AbstractDocumentExtractor):
    """Extracts documents from PDF files."""

    def extract_documents(self):
        """Extracts documents from PDF files."""
        # Implement text extraction from PDF document here
        loader = DirectoryLoader(self.path, glob="*.pdf", loader_cls=PyPDFium2Loader)
        docs = loader.load()
        return docs


class WordDocumentExtractor(AbstractDocumentExtractor):
    """Extracts documents from Word files."""

    def extract_documents(self):
        """Extracts documents from Word files."""
        # Implement text extraction from Word document here
        loader = DirectoryLoader(self.path, glob="*.txt", loader_cls=TextLoader(encoding=self.format))
        docs = loader.load()
        return docs


class TextDocumentExtractor(AbstractDocumentExtractor):
    """Extracts documents from text files."""

    def extract_documents(self):
        """Extracts documents from text files."""
        # Implement text extraction from text document here

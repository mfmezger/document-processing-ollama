"""Main file to run the document processing pipeline."""
import json
from pathlib import Path

from document_processing_ollama.document_loader import PDFDocumentExtractor
from document_processing_ollama.ollama_service import OllamaService


def main():
    """Main function to run the document processing pipeline."""
    pdf_extractor = PDFDocumentExtractor(path="input/pdf")
    ollama_service = OllamaService()
    documents = pdf_extractor.extract_documents()

    # extract the json data from the documents using the ollama service
    json_data = ollama_service.extract_json(documents)

    # create the output directory if it does not exist using pathlib
    Path("output").mkdir(parents=True, exist_ok=True)

    # save the result to a file
    with open("output/result.json", "w", encoding="utf8") as f:
        json.dump(json_data, f)


if __name__ == "__main__":
    main()

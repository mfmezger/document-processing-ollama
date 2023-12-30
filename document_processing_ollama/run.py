"""Main file to run the document processing pipeline."""
import json
from pathlib import Path

from document_processing_ollama.document_loader import PDFDocumentExtractor
from document_processing_ollama.ollama_service import OllamaService
from document_processing_ollama.post_processing import JSONPostProcessor


def main():
    """Main function to run the document processing pipeline."""
    pdf_extractor = PDFDocumentExtractor(path="input/pdf")
    ollama_service = OllamaService()

    documents = pdf_extractor.extract_documents()

    # JSON EXTRACTION
    json_data = ollama_service.extract_json(documents)

    # JSON POST-PROCESSING
    post_processor = JSONPostProcessor(data=json_data)
    post_processed_data = post_processor.cleaning()

    # create the output directory if it does not exist using pathlib
    Path("output").mkdir(parents=True, exist_ok=True)

    # save the result to a file
    with open("output/result.json", "w", encoding="utf8") as f:
        json.dump(post_processed_data, f)


if __name__ == "__main__":
    main()

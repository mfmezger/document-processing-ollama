"""Main file to run the document processing pipeline."""
import json
import os
from pathlib import Path

from document_processing_ollama.document_loader import PDFDocumentExtractor
from document_processing_ollama.ollama_service import OllamaService
from document_processing_ollama.post_processing import JSONPostProcessor


def write_json(data, path):
    """Write data to a JSON file."""
    with open(path, "w", encoding="utf8") as f:
        json.dump(data, f)


def main():
    """Main function to run the document processing pipeline."""
    input_dir = os.path.join("input", "pdf")
    output_dir = "output"
    output_file = os.path.join(output_dir, "result.json")

    pdf_to_json(input_dir, output_dir, output_file)


def pdf_to_json(input_dir: str, output_dir: str, output_file: str):
    """Converts PDF files to JSON files.

    Args:
        input_dir (str): Input directory with PDF files.
        output_dir (str): Output directory for JSON files.
        output_file (str): Output file name.
    """
    pdf_extractor = PDFDocumentExtractor(path=input_dir)

    ollama_service = OllamaService(model="mistral:instruct", prompt_name="json-extraction.j2")

    documents = pdf_extractor.extract_documents()

    # JSON EXTRACTION
    json_data = ollama_service.extract_json(documents)

    # JSON POST-PROCESSING
    post_processor = JSONPostProcessor(data=json_data)
    post_processed_data = post_processor.cleaning()

    # create the output directory if it does not exist using pathlib
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # save the result to a file
    write_json(post_processed_data, output_file)


if __name__ == "__main__":
    main()

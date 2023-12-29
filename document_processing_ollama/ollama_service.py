"""The OllamaService class provides a wrapper for the Ollama class."""
import json
import os

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from tqdm import tqdm


class OllamaService:
    """Base class for OllamaService."""

    def __init__(self):
        """Initialization of the Connection to the Ollama API."""
        self.llm = Ollama(model="mistral:instruct")
        self.prompt = self.load_prompt("json-extraction.j2")

    def load_prompt(self, prompt_name):
        """Loads a prompt from a file."""
        prompt_path = os.path.join("prompts", prompt_name)
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt file '{prompt_name}' not found.")

        with open(prompt_path, encoding="utf-8") as f:
            prompt = PromptTemplate.from_template(f.read(), template_format="jinja2")

        return prompt

    def extract_json(self, documents):
        """Extracts JSON data from a given text."""
        result = {}
        # iterate over the text list
        for doc in tqdm(documents):
            # append the text to the prompt
            text_prompt = self.prompt.format(text=documents[doc])

            # generate the prediction
            answer = self.llm(text_prompt)

            # remove all line breaks and double backslashes
            answer = answer.replace("\n", "").replace("\\", "").strip()

            # create a json object from the answer
            try:
                answer_dict = json.loads(answer)
            except json.JSONDecodeError:
                answer_dict = answer

            # append the answer to the result
            result[doc] = {"title": doc, "input": documents[doc], "output": answer_dict}

        return result

    def extract_markdown(self, text):
        """Extracts Markdown data from a given text."""

    def extract_xml(self, text):
        """Extracts XML data from a given text."""

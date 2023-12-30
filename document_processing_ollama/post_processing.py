"""These classes are used to post-process the data after it has been extracted from the documents."""
import json
from abc import ABC, abstractmethod

from loguru import logger


class AbstractPostProcessor(ABC):
    """Abstract class for post-processing of the data."""

    def __init__(self, data, format="utf-8"):
        """Constructor for AbstractPostProcessor."""
        self.data = data
        self.format = format

    @abstractmethod
    def cleaning(self):
        """Clean the data."""

    @abstractmethod
    def validation(self):
        """Validate the correct data format."""


class JSONPostProcessor(AbstractPostProcessor):
    """Post-processes JSON data."""

    def cleaning(self):
        """Clean the data."""
        # iterate over the data
        for doc in self.data:
            # get the answer from the data
            answer = self.data[doc]["output"]

            # remove all line breaks and double backslashes
            answer = answer.replace("\n", "").replace("\\", "").strip()

            # create a json object from the answer
            answer_dict = self.validation(text=answer, doc=doc)

            # add the answer to the data
            self.data[doc]["output"] = answer_dict

        return self.data

    def validation(self, text: str, doc: str):
        """Validate the correct data format."""
        try:
            answer_dict = json.loads(text)
        except json.JSONDecodeError as e:
            logger.error(f"Could not decode JSON data: {doc}")
            raise e

        return answer_dict


class MarkdownPostProcessor(AbstractPostProcessor):
    """Post-processes Markdown data."""

    def cleaning(self):
        """Clean the data."""
        # Implement cleaning of the data here

    def validation(self):
        """Validate the correct data format."""
        # Implement validation of the data here


class XMLPostProcessor(AbstractPostProcessor):
    """Post-processes XML data."""

    def cleaning(self):
        """Clean the data."""
        # Implement cleaning of the data here
        # TODO: Implement XML cleaning

    def validation(self):
        """Validate the correct data format."""
        # Implement validation of the data here
        # TODO: Implement XML validation

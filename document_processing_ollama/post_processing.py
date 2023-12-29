"""These classes are used to post-process the data after it has been extracted from the documents."""
from abc import ABC, abstractmethod


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
        # Implement cleaning of the data here

    def validation(self):
        """Validate the correct data format."""
        # Implement validation of the data here


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

    def validation(self):
        """Validate the correct data format."""
        # Implement validation of the data here

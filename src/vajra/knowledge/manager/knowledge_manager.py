"""
Knowledge Manager

Manages Vajra's stored knowledge.
"""


class KnowledgeManager:
    """
    Stores and retrieves Knowledge objects.
    """

    def __init__(self):
        """
        Initialise knowledge storage.
        """

        self.knowledge_base = []


    def add_knowledge(self, knowledge):
        """
        Add a Knowledge object.

        Parameters:
            knowledge:
                Knowledge object.
        """

        self.knowledge_base.append(knowledge)

        return knowledge


    def get_all_knowledge(self):
        """
        Return all stored knowledge.

        Returns:
            list:
                Knowledge objects.
        """

        return self.knowledge_base


    def search(self, keyword):
        """
        Search knowledge by content.

        Parameters:
            keyword (str):
                Search term.

        Returns:
            list:
                Matching knowledge objects.
        """

        results = []

        for knowledge in self.knowledge_base:

            if keyword.lower() in knowledge.content.lower():

                results.append(knowledge)

        return results


    def clear(self):
        """
        Remove all stored knowledge.
        """

        self.knowledge_base.clear()
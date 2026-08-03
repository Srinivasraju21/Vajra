"""
Vajra Agent Communication Bus

Provides communication between
autonomous agents.

Agents can:

- Send messages
- Receive information
- Share execution updates

This is the foundation for
multi-agent collaboration.
"""





class MessageBus:
    """
    Central communication system
    between Vajra agents.
    """



    def __init__(self):
        """
        Initialize message storage.
        """


        # Stores every communication
        # between agents.

        self.messages = []





    def send(
        self,
        sender,
        receiver,
        message
    ):
        """
        Send message from one agent
        to another.


        Args:

            sender:
                Agent sending message


            receiver:
                Agent receiving message


            message:
                Information shared
        """



        communication = {


            "sender":

                sender.name,


            "receiver":

                receiver.name,


            "message":

                message


        }



        # Save communication
        # for history and learning.

        self.messages.append(

            communication

        )



        return communication





    def get_messages(
        self
    ):
        """
        Return communication history.
        """

        return self.messages
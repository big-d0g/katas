import unittest

from social_network.main import Message, Name, Post, Publisher, User


class TestPublisher(unittest.TestCase):
    # Posting: Alice can publish messages to a personal timeline
    def test_user_can_publish_messages_to_timeline(self) -> None:
        publish = Publisher()
        alice = User(Name("Alice"))
        post = Post(alice.id, Message("Here is a test message."))

        publish.to_personal_timeline(alice, post)

        self.assertEqual(len(alice.timeline), 1)
        self.assertEqual(alice.timeline[0], post)
        self.assertEqual(alice.timeline[0].message, Message("Here is a test message."))


if __name__ == "__main__":
    unittest.main()

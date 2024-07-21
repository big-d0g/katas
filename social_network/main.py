from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

# Value Objects


@dataclass
class ValueObject: ...


@dataclass
class Name(ValueObject):
    value: str


@dataclass
class Message(ValueObject):
    value: str


# Entities


@dataclass
class Entity: ...


@dataclass
class Post(Entity):
    author_id: UUID
    message: Message
    id: UUID = uuid4()
    timestamp_: datetime = datetime.now()


@dataclass
class User(Entity):
    display_name: Name
    id: UUID = uuid4()
    timeline: list[Post] = field(default_factory=list)

    def publish(self, post: Post) -> None:
        self.timeline.append(post)


# Services


class Publisher:
    def to_personal_timeline(self, user: User, post: Post) -> None:
        if user.id == post.author_id:
            user.publish(post)

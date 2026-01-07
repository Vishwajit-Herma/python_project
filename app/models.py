from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class User(BaseModel):
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return self._name
    
    def __eq__(self, other):
        return self._id == other._id

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'email': self._email
        }
    
class Post(BaseModel):
    def __init__(self, post_id, user_id, title):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title

    def to_dict(self):
        return self.__dict__
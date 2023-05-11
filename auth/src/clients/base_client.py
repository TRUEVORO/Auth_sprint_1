from abc import ABC, abstractmethod


class BaseClient(ABC):
    """Base class for client."""

    @abstractmethod
    def create(self, *args, **kwargs):
        """Create a new resource with the given arguments."""

        raise NotImplementedError

    @abstractmethod
    def retrieve(self, *args, **kwargs):
        """Retrieve a resource based on the given arguments."""

        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs):
        """Update an existing resource with the given arguments."""

        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        """Delete a resource based on the given arguments."""

        raise NotImplementedError

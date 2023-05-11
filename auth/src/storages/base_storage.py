from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """An abstract storage."""

    @abstractmethod
    def save_data(self, key: str, value: any, ttl: int | None = None) -> None:
        """Save data in storage."""

        raise NotImplementedError

    @abstractmethod
    def retrieve_data(self, key: str) -> any:
        """Retrieve data from storage."""

        raise NotImplementedError

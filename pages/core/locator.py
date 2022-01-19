from typing import Tuple


class Locator:
    def __init__(self, method: str, query: str):
        self.__method = method
        self.__query = query

    def to_tuple(self) -> Tuple[str, str]:
        return self.__method, self.__query

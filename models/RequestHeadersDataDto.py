from typing import Any

class RequestHeadersDataDto:
    def __init__(self, headers):
        self.headers = headers

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        super().__setattr__(__name, __value)

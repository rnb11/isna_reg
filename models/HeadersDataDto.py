from typing import Any


class HeadersDataDto:
    def __init__(self):
        self.message_uid = None
        self.knp_message_uid = None
        self.message_created_date = None
        self.operation_type = None
        self.initial = None
        self.initiator = None

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        super().__setattr__(__name, __value)


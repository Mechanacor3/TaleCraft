class Agent:
    def __init__(self, *args, **kwargs):
        pass

    def __class_getitem__(cls, item):
        return cls


class Runner:
    @staticmethod
    async def run(agent, input_items, **kwargs):
        return None


class ItemHelpers:
    @staticmethod
    def text_message_outputs(items):
        return ""


TResponseInputItem = dict

from contextlib import contextmanager


@contextmanager
def trace(name: str, trace_id: str | None = None):
    yield

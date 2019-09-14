from handler.Handler import Handler


class HandlerManager:
    def __init__(self):
        self.handlers = []

    def tick(self):
        for handler in self.handlers:
            handler.tick()

    def add(self, handler: Handler):
        self.handlers.append(handler)

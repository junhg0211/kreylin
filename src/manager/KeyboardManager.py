class KeyboardManager:
    def __init__(self):
        self.key_count = 512

        self.keys = [False for _ in range(self.key_count)]

        self.start_keys = None
        self.end_keys = None

        self.buffer = ''

    def initialize(self):
        self.start_keys = [False for _ in range(self.key_count)]
        self.end_keys = [False for _ in range(self.key_count)]

    def pop_buffer(self):
        tmp = self.buffer
        self.buffer = ''
        return tmp

    def pressed(self, unicode):
        self.buffer += unicode

    def key_pressed(self, key_code):
        if key_code < self.key_count:
            self.keys[key_code] = True
            self.start_keys[key_code] = True

    def key_released(self, key_code):
        if key_code < self.key_count:
            self.keys[key_code] = False
            self.end_keys[key_code] = True

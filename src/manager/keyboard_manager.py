class KeyboardManager:
    def __init__(self):
        self.keys = set()
        self.start_keys = set()
        self.end_keys = set()

        self.buffer = ''

    def initialize(self):
        self.start_keys.clear()
        self.end_keys.clear()

    def pop_buffer(self):
        tmp = self.buffer
        self.buffer = ''
        return tmp

    def pressed(self, unicode):
        if unicode != '\\':
            self.buffer += unicode

    def start_key(self, key_code):
        self.keys.add(key_code)
        self.start_keys.add(key_code)

    def end_key(self, key_code):
        if key_code in self.keys:
            self.keys.remove(key_code)
        self.end_keys.add(key_code)

    def is_pressed(self, key_code):
        return key_code in self.keys

    def is_start(self, key_code):
        return key_code in self.start_keys

    def is_end(self, key_code):
        return key_code in self.end_keys

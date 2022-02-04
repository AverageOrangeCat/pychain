class Block:
    def __init__(self, index: int, data):
        self.index = index
        self.data = data
        self.request_counter = 0
        self.agrees = 0
        self.disagrees = 0

    def get_json(self):
        return {
            "index": self.index,
            "data": self.data
        }

    def vote(self, agrees: bool):
        if agrees:
            self.agrees += 1
        else:
            self.disagrees += 1

        self.request_counter += 1

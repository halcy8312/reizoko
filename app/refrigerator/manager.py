class RefrigeratorManager:
    def __init__(self):
        self.contents = {}

    def add_item(self, item):
        self.contents[item] = self.contents.get(item, 0) + 1

    def remove_item(self, item):
        if item in self.contents:
            self.contents[item] -= 1
            if self.contents[item] <= 0:
                del self.contents[item]

    def get_contents(self):
        if not self.contents:
            return "冷蔵庫は空です。"
        return "\n".join([f"{item}: {count}" for item, count in self.contents.items()])

    def get_items(self):
        return list(self.contents.keys())
class Card:
    def __init__(self, root):
        self.root = root
        self.title = root.locator('h2.card-header')
        self.image = root.locator('img')
        self.description = root.locator('div.card-block')
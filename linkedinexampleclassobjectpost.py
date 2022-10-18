class Post:
    def __init__(self, message, author):
        self.message=message
        self.author=author

    def showpost(self):
        print(f"post:{self.message},author is{self.author}")
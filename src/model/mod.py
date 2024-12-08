

class Mod:
    def __init__(
        self,
        name: str, 
        filename: str,
        url: str,
        img: str,
        side: str,
        active: bool,
        description: str,
        tags: list[str],
        dependencies: list[str],
    ): 
        self.name = name
        self.filename = filename
        self.url = url
        self.img = img
        self.side = side
        self.active = active
        self.description = description
        self.tags = tags
        self.dependencies = dependencies

    def __str__(self):
        return self.name
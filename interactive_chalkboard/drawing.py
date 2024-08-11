from PIL import Image, ImageDraw

class Drawing:
    def __init__(self):
        self.image = Image.new('RGB', (800, 600), color = (73, 109, 137))
        self.draw = ImageDraw.Draw(self.image)

    def draw(self, x, y):
        """
        Draw on the image at the given x, y coordinates.
        """
        self.draw.ellipse((x-2, y-2, x+2, y+2), fill=(255,255,255))

    def erase(self, x, y):
        """
        Erase on the image at the given x, y coordinates.
        """
        self.draw.ellipse((x-2, y-2, x+2, y+2), fill=(73, 109, 137))

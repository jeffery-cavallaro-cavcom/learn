class Settings:
    """ All of the game global settings """
    def __init__(self, size=(1000, 600), bgcolor=(230,230,230)):
        self.__width = size[0]
        self.__height = size[1]
        self.bgcolor = bgcolor

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


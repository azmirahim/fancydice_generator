#Fancy Die Class

from graphics import*
from button import Button
import random

class FancyDie:
    
    """A die is produced using its center point and a list of
    images used to reflect the  value of the die.
    Itcan be rolled used the roll() method.
    It's value can be set using the setValue() method.
    The user can check its value using the getValue() method.
    The colour of the dice outline can be set using the
    setOutline() method.
    The size of the width of the die's outline can be set using
    the setWidth() method."""
    
    def __init__(self, win, center, images):
        """ Creates a die, eg:
        dice = FancyDie(window, Point(150, 150), image_list) """
        
        self.win = win
        self.center = center
        self.images = images
        self.image = Image(self.center, self.images[0])
        self.setValue(1)
        
        half_width = (self.image.getWidth())/2
        half_height = (self.image.getHeight())/2
        
        x1 = (self.center.getX()) - half_width
        x2 = (self.center.getX()) + half_width
        y1 = (self.center.getY()) + half_height
        y2 = (self.center.getY()) - half_height
        
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setOutline("black")
        self.rect.setWidth(2)
        
        self.rect.draw(self.win)

    def roll(self):
        "Rolls the die for a new random value."
        self.value = random.randint(1, 6)
        self.image = Image(self.center, self.images[(self.value) - 1])
        self.image.draw(self.win)

    def setValue(self, value):
        "Sets the value of a die to a specific value."
        self.value = value
        self.image = Image(self.center, self.images[(self.value) - 1])
        self.image.draw(self.win)

    def getValue(self):
        "Returns the value of the die."
        return self.value

    def setBackground(self, colour):
        "Set background colour of the window."
        self.win.setBackground(colour)

    def setOutline(self, colour):
        "Sets outline colour of the die."
        self.rect.setOutline(colour)

    def setWidth(self, width):
        "Sets outline width of the die."
        self.rect.setWidth(width)

def main():
    # Create Window
    win = GraphWin("Dice", 300, 300)
    win.setCoords(-4, 0, 298, 304)
    win.setBackground("lightgreen")

    # Create list of dice images
    dice_images = ["Alea_1.png", "Alea_2.png", "Alea_3.png", "Alea_4.png", "Alea_5.png", "Alea_6.png"]

    # Create Dice
    dice_1 = FancyDie(win, Point(90, 210), dice_images)
    dice_2 = FancyDie(win, Point(210, 210), dice_images)

    # Create Roll Dice Button
    roll_button = Button(win, Point(150, 110), 180, 20, "Roll Dice")
    roll_button.activate()

    # Create Quit Button
    quit_button = Button(win, Point(150, 50), 80, 20, "Quit")
    quit_button.activate()

    # Roll Dice

    point = win.getMouse()

    while not roll_button.clicked(point) and not quit_button.clicked(point):
        point = win.getMouse()

    while not quit_button.clicked(point):
        roll_button.deactivate()
        dice_1.roll()
        dice_2.roll()
        roll_button.activate()

        point = win.getMouse()

        while not roll_button.clicked(point) and not quit_button.clicked(point):
            point = win.getMouse()

    quit_button.deactivate()
    win.close()
        
main()

        
        

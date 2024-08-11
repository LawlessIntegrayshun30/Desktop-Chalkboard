import tkinter as tk
from tkinter import PhotoImage
from pygame import mouse
from PIL import ImageTk
from drawing import Drawing
from saving import Saving

class Chalkboard:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.drawing = Drawing()
        self.saving = Saving()
        self.image_tk = ImageTk.PhotoImage(self.drawing.image)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')
        self.canvas.pack()
        self.root.after(100, self.detect_mouse_movements)

    def create_chalkboard(self):
        """
        Create the chalkboard using tkinter and pygame.
        """
        self.root.mainloop()

    def detect_mouse_movements(self):
        """
        Detect mouse movements and translate them into drawings or writings.
        """
        if mouse.get_pressed()[0]:  # If left mouse button is pressed
            x, y = mouse.get_pos()
            self.drawing.draw(x, y)
            self.update_image()
        elif mouse.get_pressed()[2]:  # If right mouse button is pressed
            x, y = mouse.get_pos()
            self.drawing.erase(x, y)
            self.update_image()
        self.root.after(100, self.detect_mouse_movements)

    def update_image(self):
        """
        Update the tkinter image with the PIL image.
        """
        self.image_tk = ImageTk.PhotoImage(self.drawing.image)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

    def save(self):
        """
        Save the current state of the chalkboard.
        """
        self.saving.save(self.drawing.image)

    def load(self):
        """
        Load a previously saved state of the chalkboard.
        """
        image = self.saving.load()
        if image is not None:
            self.drawing.image = image
            self.update_image()

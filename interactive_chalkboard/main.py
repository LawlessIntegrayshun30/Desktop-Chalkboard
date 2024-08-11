from chalkboard import Chalkboard

class Main:
    def __init__(self):
        self.chalkboard = Chalkboard()

    def main(self):
        """
        The main function to start the application.
        """
        self.chalkboard.create_chalkboard()

if __name__ == "__main__":
    main_app = Main()
    main_app.main()

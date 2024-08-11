import shelve

class Saving:
    def __init__(self, filename='chalkboard_data'):
        """
        Initialize Saving with a default filename 'chalkboard_data'.
        """
        self.filename = filename

    def save(self, data):
        """
        Save the given data into a shelve database.
        """
        with shelve.open(self.filename) as db:
            db['data'] = data

    def load(self):
        """
        Load data from the shelve database.
        """
        with shelve.open(self.filename) as db:
            return db.get('data', None)



class InvalidCategoryException(Exception):
    def __init__(self, category):
        self.expression = category
        self.message = "%s is not a valid category"

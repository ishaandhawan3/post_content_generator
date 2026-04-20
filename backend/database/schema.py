class Schema:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def __repr__(self):
        return f"Schema(name={self.name}, fields={self.fields})"
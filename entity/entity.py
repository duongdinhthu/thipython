class Entity:
    def __init__(self, id=None):
        self.id = id  # Mỗi entity sẽ có thuộc tính id chung

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def __repr__(self):
        return f"Entity(id={self.id})"

from model.model import Model

class MainController:
    def __init__(self):
        self.model = Model()

    def create(self, entity_type, entity):
        """Tạo mới một entity (danh mục, sản phẩm, v.v.)."""
        self.model.insert(entity)

    def get_all(self, entity_type):
        """Lấy tất cả các entity (danh mục, sản phẩm, v.v.)."""
        return self.model.get_all(entity_type)

    def update(self, entity_type, condition_entity, fields_to_update):
        """Cập nhật thông tin entity."""
        self.model.update(condition_entity, fields_to_update)

    def delete(self, entity_type, entity):
        """Xóa một entity."""
        self.model.delete(entity)

    def get_by_condition(self, entity_type, condition_entity):
        """Lấy entity theo điều kiện cụ thể."""
        return self.model.get_entity_by_condition(condition_entity)

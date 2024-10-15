from connectionDTB.db_connect import MySqlConnect

class Model:
    def __init__(self):
        self.connection = MySqlConnect.get_sql_connection()
        self.pstm = None

    def open_pstm(self, query, params=None):
        """Mở PreparedStatement với câu truy vấn và các tham số tùy chọn."""
        self.pstm = self.connection.cursor(prepared=True)
        self.pstm.execute(query, params) if params else self.pstm.execute(query)
        return self.pstm

    def ex_update(self):
        """Thực thi câu lệnh UPDATE và commit."""
        self.connection.commit()
        return self.pstm.rowcount > 0

    def ex_query(self):
        """Thực thi truy vấn và trả về kết quả nếu có."""
        return self.pstm.fetchall() if self.pstm.description else []

    def get_table_name(self, entity_class):
        """Lấy tên bảng dựa trên tên class của entity."""
        return entity_class.__name__.lower()

    def query_get_all(self, entity_class):
        """Tạo câu truy vấn SELECT * cho entity."""
        table_name = self.get_table_name(entity_class)
        query = f"SELECT * FROM {table_name}"
        print(f"SQL Query: {query}")
        return query

    def query_insert(self, entity):
        """Tạo câu truy vấn INSERT cho entity, chỉ lấy các trường có giá trị."""
        table_name = self.get_table_name(type(entity))
        fields = {f: getattr(entity, f) for f in dir(entity) if not f.startswith("__") and not callable(getattr(entity, f))}
        included_fields = [f for f, v in fields.items() if v]
        query = f"INSERT INTO {table_name} ({', '.join(included_fields)}) VALUES ({', '.join(['%s'] * len(included_fields))})"
        params = tuple(fields[f] for f in included_fields)
        print(f"SQL Query: {query}")
        return query, params

    def query_update(self, condition_entity, fields_to_update):
        """Tạo câu truy vấn UPDATE với các trường cần cập nhật và điều kiện."""
        table_name = self.get_table_name(type(condition_entity))
        set_clause = ", ".join([f"{k} = %s" for k in fields_to_update.keys()])
        where_clause = " AND ".join([f"{k} = %s" for k, v in vars(condition_entity).items() if v])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        params = list(fields_to_update.values()) + [v for v in vars(condition_entity).values() if v]
        print(f"SQL Query: {query}")
        return query, params


    def query_delete(self, entity):
        """Tạo câu truy vấn DELETE cho entity, chỉ lấy các trường có giá trị."""
        table_name = self.get_table_name(type(entity))
        fields = {f: getattr(entity, f) for f in dir(entity) if not f.startswith("__") and not callable(getattr(entity, f))}
        conditions = [f for f, v in fields.items() if v]
        query = f"DELETE FROM {table_name} WHERE " + " AND ".join([f"{f} = %s" for f in conditions])
        params = tuple(fields[f] for f in conditions)
        print(f"SQL Query: {query}")
        return query, params

    def query_get_by_condition(self, entity):
        """Tạo câu truy vấn SELECT dựa trên nhiều điều kiện (các trường có giá trị)."""
        table_name = self.get_table_name(type(entity))
        fields = {f: getattr(entity, f) for f in dir(entity) if not f.startswith("__") and not callable(getattr(entity, f))}
        conditions = [f for f, v in fields.items() if v]
        query = f"SELECT * FROM {table_name} WHERE " + " AND ".join([f"{f} = %s" for f in conditions])
        params = tuple(fields[f] for f in conditions)
        print(f"SQL Query: {query}")
        return query, params

    def insert(self, entity):
        """Phương thức insert entity vào database."""
        query, params = self.query_insert(entity)
        self.open_pstm(query, params)
        self.connection.commit()

    def update(self, condition_entity, fields_to_update):
        """Cập nhật thông tin entity dựa vào điều kiện linh hoạt và các trường cần cập nhật."""
        query, params = self.query_update(condition_entity, fields_to_update)
        self.open_pstm(query, params)
        self.connection.commit()


    def delete(self, entity):
        """Xóa entity từ database."""
        query, params = self.query_delete(entity)
        self.open_pstm(query, params)
        self.connection.commit()

    def get_all(self, entity_class):
        """Lấy tất cả các bản ghi của entity."""
        query = self.query_get_all(entity_class)
        self.open_pstm(query)
        return self.ex_query()

    def get_entity_by_condition(self, entity):
        """Lấy entity từ database dựa vào điều kiện."""
        query, params = self.query_get_by_condition(entity)
        self.open_pstm(query, params)
        return self.ex_query()

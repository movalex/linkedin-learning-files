

class SQLTable():

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = {}

    def drop_table(self):
        del self

    def insert_row(self, rows):
        n = 0
        # import ipdb;ipdb.set_trace()
        if len(rows) == len(self.columns):
            while n < len(self.columns):
                if self.columns[n].is_pk:
                    self.rows[rows[n]] = rows
                n = n+1

    def update_row(self, column_names, row_values, pk):
        n = 0
        while n < len(column_names):
            if column_names[n] in [x.name for x in self.columns]:
                index = [x.name for x in self.columns].index(column_names[n])
                self.rows.get(pk)[index] = row_values[n]

            n = n +1

    def drop_row(self, pk):
        self.rows.pop(pk)

    def get_index(self):
        for i,each in enumerate(self.columns):
            if each.is_pk == True:
                return i
        else:
            return False

    def set_index(self, new_pk):

        data_dict = dict()
        if new_pk in [x.name for x in self.columns]:
            index = [x.name for x in self.columns].index(new_pk)
            current_index = self.get_index()
            if current_index:
                self.remove_index(current_index)
            self.columns[index].is_pk = True
            for k, v in self.rows.items():
                data_dict[v[index]] = v
            self.rows = data_dict

    def remove_index(self, pk):
        data_dict = dict()
        if pk in [x.name for x in self.columns]:
            index = [x.name for x in self.columns].index(pk)
            self.columns[index].is_pk = False
            count = 1
            for k, v in self.rows.items():
                data_dict[count] = v
                count += 1
            self.rows = data_dict


class Column():
    
    def __init__(self, name, type, is_pk):
        self.name = name
        self.type = type
        self.is_pk = is_pk

    def __repr__(self):
        return self.name


c1 = Column("name", "varchar", False )
c2 = Column("phone", "int", False )
c3 = Column("email", "varchar", True )
c4 = Column("city", "varchar", False )

cn = [c1, c2, c3, c4]

t1 = SQLTable(name="Student", columns=cn)
print(t1.name)
print(t1.rows)
print(t1.columns)

t1.insert_row(["Atul", "89787666", "abc@zyz.com", "bengaluru"])
t1.insert_row(["Mohan", "897666", "ab@zyz.com", "mumbai","ssss"])

print(t1.name)
print(t1.rows)
print(t1.columns)
print("##############################")

# t1.set_index("phone")
#
# print(t1.name)
# print(t1.rows)
# print(t1.columns)
# print("##############################")
# #
# #
# t1.remove_index("phone")
# #
# print(t1.name)
# print(t1.rows)
# print(t1.columns)
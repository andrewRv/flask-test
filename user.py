import MySQLdb


class User:
    db = ""
    cursor = ""
    attributes = {"name", "age", "address"}

    def __init__(self, user, db_credentials=""):
        self.attributes = user
        self.connect_to_db(db_credentials)

    def save(self):
        self.cursor.execute("INSERT INTO users (name, age, address) VALUES (%s, %s, %s)",
                            (self.attributes['name'], self.attributes['age'], self.attributes['address']))
        self.db.commit()

    def connect_to_db(self, host="localhost", user="admin", password="admin", db="users"):
        try:
            self.db = MySQLdb.connect(host, user, password, db)
            self.cursor = self.db.cursor()
        except MySQLdb.Error as e:
            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])

    def update(self, new_attr):
        self.cursor.execute("UPDATE users SET name = %s, age = %s, address = %s WHERE name = %s",
                            (new_attr['name'], new_attr['age'], new_attr['address'], self.attributes['name']))
        self.db.commit()

    def delete(self):
        self.cursor.execute("DELETE FROM users WHERE name = %s",
                            (self.attributes['name']))
        self.db.commit()

    def __str__(self):
        return '({}, {}, {})'.format(self.attributes['name'], self.attributes['age'], self.attributes['address'])

    def __repr__(self):
        return '({}, {}, {})'.format(self.attributes['name'], self.attributes['age'], self.attributes['address'])
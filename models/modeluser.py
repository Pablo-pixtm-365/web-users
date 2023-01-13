from .entities.user import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            query = "SELECT * FROM SuperUsers WHERE usuario=:val1"
            vals = {'val1': user.username}
            cursor = db.session.execute(query, vals)
            row = cursor.fetchone()
            #row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self, db, id):
        try:
            query = "SELECT id, Usuario, Password_ FROM SuperUsers WHERE id=:val1"
            vals = {'val1': id}
            cursor = db.session.execute(query, vals)
            row = cursor.fetchone()
            #
            if row != None:
                return User(row[0], row[1], row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

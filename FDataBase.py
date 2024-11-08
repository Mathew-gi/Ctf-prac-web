import sqlite3
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def checkIfUserExists(self, name):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return True
        except:
            print("Database error")
        return False

    def addUser(self, name, password):
        try:
            self.__cur.execute("INSERT INTO Users VALUES(NULL, ?, ?)", (name, password))
            self.__db.commit()
        except sqlite3.Error as e:
            print("User registration error" + str(e))
            return False
        return True
    
    def defineUser(self, name, password):
        sql = f'''SELECT * FROM Users WHERE name = '{name}' and password = '{password}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getLeaders(self):
        sql = '''SELECT * FROM Points ORDER BY pointValue DESC;'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getYourPoints(self, name):
        sql = f'''SELECT * FROM Points WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []

    def getTasksWeb(self):
        sql = '''SELECT * FROM TasksWeb;'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getSolution(self, flag):
        sql = f'''SELECT * FROM TasksWeb WHERE solution = '{flag}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return True
        except:
            print("Database error")
        return False
    
    def getUserPoints(self, name):
        sql = f'''SELECT * FROM Points WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error1")
        return []
    
    def gainPoints(self, name, points):
        print(points, name)
        sql = f'''UPDATE Points SET pointValue = {points} WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            self.__cur.commit()
        except:
            print("Database error2")
            return False
        return True
import sqlite3
class FDataBase:

    def sendFlag(self, flags, name):
        sql = f'''UPDATE Users SET trueFlags = '{flags}' WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("DB2 error" + str(e))
            return False
        return True
        

    def setFlag(self, tasks, taskId):
        place = int(taskId) - 1
        newTasks = tasks.replace(tasks[place], '1')
        return newTasks
    
    def checkTrueFlag(self, name, taskId):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: 
                if res[0]["trueFlags"][int(taskId) - 1] == "1":
                    return True
                else:
                    return False
        except:
            print("Database error check true flag")
        return False
    
    def addUserPoints(self, name):
        try:
            self.__cur.execute("INSERT INTO Points VALUES(NULL, ?, ?)", (name, 0))
            self.__db.commit()
        except sqlite3.Error as e:
            print("User registration error" + str(e))
            return False
        return True

    def createTrueFlags(self, name, tasksSections):
        tasksCount = 0

        for section in tasksSections:
            sql = f'''SELECT * FROM {section};'''
            try:
                self.__cur.execute(sql)
                res = self.__cur.fetchall()
                    
                if res: 
                    tasksCount += len(res)
            except:
                    print("Database error section")

        flags = "0" * tasksCount   
        print(flags)
        return flags

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_section(self, taskId, tasksSections):
        
        tasksCount = 0

        for section in tasksSections:
            if int(taskId) > tasksCount:
                sql = f'''SELECT * FROM {section};'''
                try:
                    self.__cur.execute(sql)
                    res = self.__cur.fetchall()
                    
                    if res: 
                        tasksCount += len(res)
                        if int(taskId) <= tasksCount:
                            return section
                except:
                    print("Database error section")
            else:
                return section
            

    def checkIfUserExists(self, name):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return True
        except:
            print("Database error")
        return False

    def addUser(self, name, password, trueFlags):
        try:
            self.__cur.execute("INSERT INTO Users VALUES(NULL, ?, ?, ?)", (name, password, trueFlags))
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

    def getTasks(self, section):
        sql = f'''SELECT * FROM {section};'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getSolution(self, flag, section):
        sql = f'''SELECT * FROM {section} WHERE solution = '{flag}';'''
        print(sql)
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: 
                return True
        except:
            print("Database error solution")
        return False
    
    def getUser(self, name):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error1")
        return []
    
    def gainPoints(self, name, points):
        sql = f'''UPDATE Points SET pointValue = {points} WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("DB2 error" + str(e))
            return False
        return True
    
    def getPointsMultiplier(self, section, flag):
        sql = f'''SELECT * FROM {section} WHERE solution = '{flag}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                print(res[0])
                if  res[0]['difficulty'] == "easy":
                    return 1
                elif res[0]['difficulty'] == "medium":
                    return 2
                elif res[0]['difficulty'] == "hard":
                    return 3
        except:
            print("Database error mult")

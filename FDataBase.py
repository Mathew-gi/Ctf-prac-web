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
        place = int(taskId[4:]) - 1
        newTasks = tasks[:place] + '1' + tasks[place + 1:]
        return newTasks
    
    def checkTrueFlag(self, name, taskId):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: 
                
                if res[0]["trueFlags"][int(taskId[4:]) - 1] == "1":
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

    def createTrueFlags(self, tasksSections):
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
        return flags
    
    def setTeamsTrueFlags(self, trueFlags):
        sql = f'''UPDATE Teams SET trueFlags = {trueFlags};'''
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("DB2 error" + str(e))
            return False
        return True

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_section(self, taskId, tasksSections):
        
        tasksCount = 0

        for section in tasksSections:
            if int(taskId[4:]) > tasksCount:
                sql = f'''SELECT * FROM {section};'''
                try:
                    self.__cur.execute(sql)
                    res = self.__cur.fetchall()
                    
                    if res: 

                        tasksCount += len(res)
                        if int(taskId[4:]) <= tasksCount:
                            return section
                except:
                    print("Database error section")
            else:
                return section
    
    def getSectionsLen(self, tasksSections):
        sections = []
        currentShift = 0
        for section in tasksSections:
            sql = f'''SELECT * FROM {section};'''
            try:
                self.__cur.execute(sql)
                res = self.__cur.fetchall()
                    
                if res: 
                    currentShift += len(res)
                    sections.append(currentShift)
                else:
                    sections.append(currentShift)
            except:
                print("Database error sectionsLen")
        return sections
            

    def checkIfUserExists(self, name):
        sql = f'''SELECT * FROM Users WHERE name = '{name}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return True
        except:
            print("Database error")
        return False

    def addUser(self, name, password, trueFlags, team):
        try:
            self.__cur.execute("INSERT INTO Users VALUES(NULL, ?, ?, ?, ?)", (name, password, trueFlags, team))
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
    
    def getTeam(self, team):
        sql = f'''SELECT * FROM Teams WHERE title = '{team}';'''
        print(sql)
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getOtherTeam(self, title):
        sql = f'''SELECT * FROM Teams WHERE title != '{title}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def getTeamPoints(self, title):
        sql = f'''SELECT * FROM Teams WHERE title = '{title}';'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Database error")
        return []
    
    def gainTeamPoints(self, title, points):
        sql = f'''UPDATE Teams SET pointValue = {points} WHERE title = '{title}';'''
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("DB2 error" + str(e))
            return False
        return True
    
    def addTeamSolution(self, team, trueFlags):
        sql = f'''UPDATE Teams SET trueFlags = '{trueFlags}' WHERE title = '{team}';'''
        print(sql)
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("DB2 error" + str(e))
            return False
        return True

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
                if  res[0]['difficulty'] == "easy":
                    return 1
                elif res[0]['difficulty'] == "medium":
                    return 2
                elif res[0]['difficulty'] == "hard":
                    return 3
        except:
            print("Database error mult")

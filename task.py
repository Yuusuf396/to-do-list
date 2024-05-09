class Task:
    def __init__(self,number,deadline,importance,text) :
        self.__number=number
        self.__deadline=deadline
        self.__importance=importance
        self.__text=text
    def set_number(self,number):
        self.__number=number
    def set_deadline(self,deadline):
        self.__deadline=deadline 
    def set_importance(self,importance):
        self.__importance=importance     
    def set_text(self,text):
        self.__text=text            
    def get_number(self):
        return self.__number
    def get_deadline(self):
        return self.__deadline
    def get_importance(self):
        return self.__importance
    def get_text(self):
        return self.__text
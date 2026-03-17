class BigThing:
    def __init__(self, general_variable):
        self.general_variable = general_variable
    
    def get_size(self):
        if isinstance(self.general_variable, (int, float)):
            return self.general_variable
        
        elif isinstance(self.general_variable, (list, dict, str)):
            return len(self.general_variable)
        
        else:
            return 0
        
class BigCat(BigThing):
    def __init__(self, general_variable, weight):
        super().__init__(general_variable)
        self.weight = weight

    def get_size(self):
        if self.weight > 20:
            return "very fat"
        
        if self.weight > 15:
            return "fat"
        
        return "ok"
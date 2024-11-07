# error handling note: you can have these functions return None if they fail
# or have bad input, etc. and then handle the case where they might be None
# where you use their methods in the other files
# ex: define a onbuttonclick() function and have it generate the pairs, if it 
# returns then return a message to the scene and display the pairs
# if it returns None then display an error message instead.
import random

class NameListManager:
    def __init__(self, nameList=set(), constraints=set()):
        self.names = nameList
        self.constraints = constraints  # set of tuples where the first name cannot be paired with the second
        for name in nameList:
            self.add_constraint(name, name)
    
    def add_name(self, name):
        # be sure to include logic rules: a person cannot gift themselves
        self.names.add(name)
        self.add_constraint(name, name)
    
    def remove_name(self, name):  # remember to remove any associated constraints
        # or have a pop up for removing names with existing constraints
        if self.names and name in self.names:
            self.names.remove(name)

    def add_constraint(self, giver, receiver):
        self.constraints.add((giver, receiver))
    
    def remove_constraint(self, giver, receiver):
        if self.constraints and (giver, receiver) in self.constraints:
            self.constraints.remove((giver, receiver))
    
    def generate_pairs(self):
        # use backtracking to generate all possible pairings, stopping when you get
        # a valid configuration. 
        # potential for randomness: choose a random name from the possible options
        # when going into the next step of backtracking
        givers, receivers = set(self.names), set(self.names)
        res = []

        def backtracking(givers, receivers):
            if len(res) == len(self.names):
                return res
            if not givers:
                return
            giver = random.choice(list(givers))
            givers.remove(giver)
            random_receivers = list(receivers)
            random.shuffle(random_receivers)
            for i in range(len(random_receivers)):
                receiver = random_receivers[i]
                if (giver, receiver) in self.constraints:
                    continue 
                res.append((giver, receiver))
                receivers.remove(receiver)
                ret = backtracking(givers, receivers)
                if ret:
                    return ret
                receivers.add(receiver)
                res.pop()
            givers.add(giver)

        backtracking(givers, receivers)

        if res:
            return res
        
        return None

    def get_names(self):
        return self.names
        
        


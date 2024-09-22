class Dictionary:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def put(self,key,value):
        hash_value=self.hash_function(key)
        if self.slots[hash_value]==None:
            self.slots[hash_value]=key
            self.data[hash_value]=value
        else:
            if self.slots[hash_value]==key:
                self.data[hash_value]=value
            else:
                new_hash_value=self.rehash(hash_value)
                while self.slots[new_hash_value]!=None and self.slots[new_hash_value]!=key:
                    new_hash_value=self.rehash(new_hash_value)
                if self.slots[new_hash_value]==None:
                    self.slots[new_hash_value]=key
                    self.data[new_hash_value]=value
                else:
                    self.data[new_hash_value]=value
    def get(self,key):
        start_position=self.hash_function(key)
        current_position = start_position
        while self.slots[current_position]!=None:
            if self.slots[current_position]==key:
                print(self.data[current_position])
                return
            current_position = self.rehash(current_position)
            if current_position == start_position:
                return "Not found"
            return "Not found"
    def str(self):
        for i in range(len(self.slots)):
            if self.slots[i]!=None:
                print(self.slots[i],":",self.data[i],end=" ")
        return ""
    def rehash(self,old_hash):
        return (old_hash+1)%self.size
    def hash_function(self,key):
        return abs(hash(key))%self.size
obj=Dictionary(5)
obj.put("python",35)
obj.put("java",40)
obj.put("php",25)
obj.put("javascript",10)
obj.str()
obj.get("java")



from dugum import Dugum as Node

class HashTable: 
    def __init__(self, total): 
        self.total = total 
        self.table = [None] * total 
  
    def _hash(self, key): 
        return hash(key) % self.total 
  
    def ekle(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            temp = self.table[index]
            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                if not temp.next:
                    temp.next = Node(key, value)
                    return
                temp = temp.next
  
    def ara(self, key): 
        index = self._hash(key) 
  
        temp = self.table[index] 
        while temp: 
            if temp.key == key: 
                return temp.value 
            temp = temp.next
    
    def sil(self, key): 
        index = self._hash(key) 
  
        temp2 = None
        temp = self.table[index] 
  
        while temp: 
            if temp.key == key: 
                if temp2: 
                    temp2.next = temp.next
                else: 
                    self.table[index] = temp.next
                return
            temp2 = temp 
            temp = temp.next
    
    def __contains__(self, key): 
        try: 
            self.ara(key) 
            return True
        except KeyError: 
            return False
        
    def display(self):
        for index, node in enumerate(self.table):
            print(f"\nIndex {index}: ", end="")
            temp = node
            while temp:
                print(f"{temp.key},", end=" ")
                temp = temp.next
            print()  

    def __iter__(self):
        self.current_index = 0
        self.current_node = self.table[self.current_index]
        return self

    def __next__(self):
        while self.current_index < self.total:
            if self.current_node:
                key_value_pair = (self.current_node.key, self.current_node.value)
                self.current_node = self.current_node.next
                return key_value_pair
            else:
                self.current_index += 1
                if self.current_index < self.total:
                    self.current_node = self.table[self.current_index]
        raise StopIteration


from hash_Table import HashTable
from interestedAnalyzer import InterestAnalyzer

class InterestHashTable:
    def __init__(self, interest_list):
        self.interest_tables = HashTable(len(interest_list))
        for interest in interest_list:
            self.interest_tables.ekle(interest, HashTable(5))

    def insert_user(self, user):
        analyzer = InterestAnalyzer() 
        interests = analyzer.analyze_interests(user.tweets)
        for interest in interests:
            if interest not in self.interest_tables:
                self.interest_tables.ekle(interest, HashTable(5))
            self.interest_tables.ara(interest).ekle(user.username, user)
    
    def search(self, interest):
        return self.interest_tables.ara(interest)
    

    def display(self):
        for index, node in enumerate(self.interest_tables.table):
            print(f"Interest Index {index}: ", end="")
            print() 
            current = node
            while current:
                print(f"({current.key}: ", end="")
                current.value.display()
                print(")", end=" ")
                current = current.next
            print()  
    
    def display_users_by_interest(self, interest):
        index = self.interest_tables._hash(interest)  
    
        current = self.interest_tables.table[index]
        while current:
            if current.key == interest:
                print(f"({interest} İlgi Alanına Sahip Kullanıcılar): \n", end="")
                current.value.display()
                return
            current = current.next

        print(f"{interest} İlgi Alanına Sahip Kullanıcı Bulunamadı.")

    def get_user_interests(self, username):
        user_interests = []
        for interest, sub_table in self.interest_tables:
            for node in sub_table.table:
                current = node
                while current:
                    if current.value.username == username:
                        user_interests.append(interest)
                    current = current.next
        return user_interests  

    
    def match_users_selection_sort(self, interest):
        index = self.interest_tables._hash(interest)

        current = self.interest_tables.table[index]
        while current:
            if current.key == interest:
                users_with_interest = self._get_users_from_sub_table(current.value)
                self._selection_sort(users_with_interest)
                self._display_matched_users(users_with_interest)
                return
            current = current.next

        print(f"{interest} İlgi Alanına Sahip Kullanıcı Bulunamadı.")

    def _get_users_from_sub_table(self, sub_table):
        users = []
        for node in sub_table.table:
            current = node
            while current:
                users.append(current.key)
                current = current.next
        return users

    def _selection_sort(self, users):
        for i in range(len(users) - 1):
            min_index = i
            for j in range(i + 1, len(users)):
                if users[j] < users[min_index]:
                    min_index = j
            users[i], users[min_index] = users[min_index], users[i]

    def _display_matched_users(self, users):
        print("Eşleşen Kullanıcılar:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user}")



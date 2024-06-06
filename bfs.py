from queue1 import Queue 

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start_username):
        visited = set()
        queue = Queue()
        result_users = []

        visited.add(start_username)
        queue.enqueue(start_username, None) 

        while not queue.is_empty():
            current_node = queue.dequeue()
            result_users.append(current_node.key)

            for follower in self.graph.successors(current_node.key):
                if follower not in visited:
                    visited.add(follower)
                    queue.enqueue(follower, None)  # None olarak değer ekliyoruz

        return result_users

    def find_users_with_same_followers(self, start_username):
        followers_count = len(list(self.graph.successors(start_username)))
        users = self.bfs(start_username)
        
        users_with_same_followers = [user for user in users if len(list(self.graph.successors(user))) == followers_count and user != start_username]
        
        return users_with_same_followers

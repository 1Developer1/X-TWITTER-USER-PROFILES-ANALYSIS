class DFS:
    @staticmethod
    def dfs(graph, start, end, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path = path + [start]

        if start == end:
            return path

        for neighbor in graph[start]:
            if neighbor not in visited:
                new_path = DFS.dfs(graph, neighbor, end, visited, path)
                if new_path:
                    return new_path

        return None

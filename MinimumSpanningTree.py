class MinimumSpanningTree:
    @staticmethod
    def kruskal(graph):
        edges = []
        for node in graph:
            for neighbor, weight in graph[node]:
                edges.append((node, neighbor, weight))

        edges = sorted(edges, key=lambda x: x[2])
        parent = {node: node for node in graph}

        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            parent[root1] = root2

        mst = []

        for edge in edges:
            node1, node2, weight = edge
            if find(node1) != find(node2):
                union(node1, node2)
                mst.append(edge)

        return mst

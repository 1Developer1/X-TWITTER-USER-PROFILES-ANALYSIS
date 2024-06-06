class Graph:
    def __init__(self, G):
        self.G = G

    def graph_to_text_representation(self):
        text_representation = []
        for node in self.G.nodes():
            neighbors = list(self.G.neighbors(node))
            text_representation.append(f"Düğüm: {node}\nKenarlar: {', '.join(neighbors)}\n")
        return "\n".join(text_representation)

    def save_text_to_file(self, filename="text_representation.txt"):
        text_repr = self.graph_to_text_representation()
        with open(filename, "w") as file:
            file.write(text_repr)
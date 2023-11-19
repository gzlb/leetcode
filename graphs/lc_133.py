class Node: 
    def __init__(self, val, neighbours) -> None:
        self.val = val
        self.neighbours = neighbours


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        return self.dfs(node, {None: None})

    def dfs(self, node: Node | None, graph: dict) -> Node | None:
        if node not in graph:
            graph[node] = Node(node.val)
            for ngh in node.neighbors:
                graph[node].neighbors.append(self.dfs(ngh, graph))
        return graph[node]
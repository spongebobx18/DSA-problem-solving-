class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjacency_list = {}
        for source in range(len(isConnected)):
            adjacency_list[source] = []
            for destination in range(len(isConnected[0])):
                if isConnected[source][destination]:
                    adjacency_list[source].append(destination)

        visited_nodes = set()

        def dfs(node):
            if node in visited_nodes:
                return 0
            visited_nodes.add(node)
            for neighbor in adjacency_list[node]:
                dfs(neighbor)
            return 1

        province_count = 0
        for start_node in adjacency_list:
            province_count += dfs(start_node)

        return province_count

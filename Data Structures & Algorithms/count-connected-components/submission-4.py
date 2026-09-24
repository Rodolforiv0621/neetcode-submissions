class Solution:
    def explore(self, current, graph, visited):
        if current in visited:
            return False
        visited.add(current)

        for neighbor in graph[current]:
            self.explore(neighbor, graph, visited)
        
        return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        visited = set()
        count = 0
        for node in hashmap:
            if self.explore(node, hashmap, visited) == True:
                count += 1
        
        return count
            



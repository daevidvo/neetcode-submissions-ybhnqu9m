class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]

        def find(node):
            p = par[node]

            while p != par[p]:
                p = par[par[p]]

            return p

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for node1, node2 in edges:
            if union(node1, node2) is False:
                return [node1, node2]
            

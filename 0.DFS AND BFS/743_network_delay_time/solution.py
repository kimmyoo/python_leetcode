from collections import defaultdict

class Solution1(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        # a dictionary to record the path and time from each node to its immediate nodes
        for start, end, time in times:
            graph[start].append((time, end))
        # a dictionary to record smallest delay to each node from starting node
        delays = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, delay):
            if delay >= delays[node]: return
            delays[node] = delay
            for time, end in sorted(graph[node]):
                dfs(end, delay+time)
        
        dfs(K, 0)
        res = max(delays.values())
        return res if res < float('inf') else -1

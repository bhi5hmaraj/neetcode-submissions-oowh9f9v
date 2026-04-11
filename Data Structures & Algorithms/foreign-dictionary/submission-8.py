from collections import deque

class Solution:

    def createGraph(self, words) -> List[List[int]]:
        adj = [list() for _ in range(26)]
        for i in range(len(words)):
            for j in range(i + 1, len(words), 1):
                added = False
                for k in range(min(len(words[i]), len(words[j]))):
                    print(words[i], "   ", words[j])
                    small_char_pos = ord(words[i][k]) - ord('a')
                    big_char_pos = ord(words[j][k]) - ord('a')
                    if small_char_pos != big_char_pos:
                        if big_char_pos not in adj[small_char_pos]:
                            adj[small_char_pos].append(big_char_pos)
                        added = True
                        break
                    
                # if w_j is a prefix of w_i and w_j is longer than w_i 
                if not added and len(words[i]) > len(words[j]):
                    return []
                    

        return adj

    visited: List[bool]
    temp_stack: List[bool]
    
    def _cycle_check_rec(self, curr, graph) -> bool:
        self.temp_stack[curr] = True
        self.visited[curr] = True
        ret = False
        for v in graph[curr]:
            if self.temp_stack[v]:
                return True
            if self.visited[v]:
                continue
            else:
                ret |= self._cycle_check_rec(v, graph)
        
        self.temp_stack[curr] = False
        return ret

    def checkCycle(self, graph) -> bool:
        self.visited = [False] * 26
        self.temp_stack = [False] * 26
        ret = False
        for curr in range(26):
            if not self.visited[curr]: 
                ret |= self._cycle_check_rec(curr, graph)
            
        return ret
    
    def topSort(self, graph) -> List[int]:
        in_degree: List[int] = [0] * 26
        for u in range(26):
            for v in graph[u]:
                in_degree[v] += 1
        
        print(in_degree)

        queue = deque([u for u in range(26) if in_degree[u] == 0 and graph[u]])
        topsort_order = []

        while queue:
            curr = queue.popleft()
            topsort_order.append(curr)
            for v in graph[curr]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    queue.append(v)

        return topsort_order



    def _debug_graph(self, graph):
        for i in range(len(graph)):
            print(chr(97 + i) , "  -> ", list(map(lambda x : chr(97 + x), graph[i])))

    def foreignDictionary(self, words: List[str]) -> str:
        # 1. create a graph using words list
        # 2. check for cycles
        # 3. if no cycle, do a top sort and return answer
        # 4. if cycle, return empty
        # 5. we will add a special token in the end of string, to handle prefix
        # words = list(map(lambda x: x + '`', words))
        graph = self.createGraph(words)
        if not graph:
            return ''

        self._debug_graph(graph)
        if self.checkCycle(graph):
            return ''

        topsort_order = self.topSort(graph)
        determined = ''.join(map(lambda x: chr(ord('a') + x), topsort_order))
        det_set = set(determined)
        all_chars = set(''.join(words))
        return determined + ''.join(all_chars - det_set)


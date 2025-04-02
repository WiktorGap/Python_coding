import heapq
graph1 = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
def dijkstra(graph, start):  #
    searched = []
    priority_que = []
    heapq.heappush(priority_que, (0, start))  
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0  
    
    while priority_que:
        current_cost, nodeOut = heapq.heappop(priority_que)  
        if nodeOut in searched:
            continue
        
        searched.append(nodeOut)
       # print(f"Węzeł zewnętrzny {nodeOut}: Węzeł wewnętrzny {graph[nodeOut]}")

        for relatedNode, cost in graph[nodeOut].items():  
            if relatedNode not in searched:
                new_cost = current_cost + cost
                if new_cost < distances[relatedNode]:  
                    distances[relatedNode] = new_cost
                    heapq.heappush(priority_que, (new_cost, relatedNode))  
                #print(f"Węzeł wewnętrzny {relatedNode}  : koszt {cost}")
    return print(distances)
dijkstra(graph1,'A')
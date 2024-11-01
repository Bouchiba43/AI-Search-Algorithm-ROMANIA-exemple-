import heapq

# Define the Romania graph as an adjacency list
romania_map = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)]
}

# Straight-line distances (heuristic) to Bucharest
heuristic_to_bucharest = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Timisoara": 329, "Lugoj": 244,
    "Mehadia": 241, "Drobeta": 242, "Craiova": 160, "Sibiu": 253, "Rimnicu Vilcea": 193,
    "Fagaras": 176, "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80,
    "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234
}

def heuristic(city, goal="Bucharest"):
    return heuristic_to_bucharest.get(city, float('inf'))

def greedy_best_first_search(start, goal="Bucharest"):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), start))
    explored_set = set()
    
    came_from = {start: None}

    while priority_queue:
        _, current_city = heapq.heappop(priority_queue)
        
        if current_city == goal:
            return reconstruct_path(came_from, current_city)
        
        explored_set.add(current_city)

        for neighbor, _ in romania_map.get(current_city, []):
            if neighbor not in explored_set:
                explored_set.add(neighbor)
                heapq.heappush(priority_queue, (heuristic(neighbor), neighbor))
                came_from[neighbor] = current_city
    
    return None  

def reconstruct_path(came_from, current_city):
    path = []
    while current_city:
        path.append(current_city)
        current_city = came_from[current_city]
    path.reverse()
    return path

def main():
    start = "Arad"
    goal = "Bucharest"
    path = greedy_best_first_search(start, goal)
    if path:
        print("Path from", start, "to", goal, ":", path)
    else:
        print("No path found from", start, "to", goal)

if __name__ == "__main__":
    main()

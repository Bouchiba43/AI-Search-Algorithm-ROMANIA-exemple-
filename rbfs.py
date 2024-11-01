# Define the Romania graph as an adjacency list with distances
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

# Heuristic values (straight-line distances to Bucharest)
heuristic_to_bucharest = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Timisoara": 329, "Lugoj": 244,
    "Mehadia": 241, "Drobeta": 242, "Craiova": 160, "Sibiu": 253, "Rimnicu Vilcea": 193,
    "Fagaras": 176, "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80,
    "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234
}

def heuristic(city, goal="Bucharest"):
    return heuristic_to_bucharest.get(city, float('inf'))

def expand(city):
    return [(neighbor, cost) for neighbor, cost in romania_map.get(city, [])]

def g(city, parent_cost):
    return parent_cost

def rbfs(current_city, goal="Bucharest", f_limit=float('inf'), g_cost=0):
    if current_city == goal:
        return [current_city], 0
    
    successors = expand(current_city)
    if not successors:
        return [], float('inf')
    
    # Calculate f values for successors
    f_values = []
    for successor, cost in successors:
        f_value = g_cost + cost + heuristic(successor, goal)
        f_values.append((successor, f_value, g_cost + cost))
    f_values.sort(key=lambda x: x[1])  # Sort by f-value

    while True:
        best_city, best_f, best_g_cost = f_values[0]
        if best_f > f_limit:
            return [], best_f
        
        alternative_f = f_values[1][1] if len(f_values) > 1 else float('inf')
        
        result, best_city_f = rbfs(best_city, goal, min(f_limit, alternative_f), best_g_cost)
        
        f_values[0] = (best_city, best_city_f, best_g_cost)
        f_values.sort(key=lambda x: x[1])

        if result:
            return [current_city] + result, best_city_f

def main():
    start = "Arad"
    goal = "Bucharest"
    path, _ = rbfs(start, goal)
    if path:
        print("Path from", start, "to", goal, ":", path)
    else:
        print("No path found from", start, "to", goal)

if __name__ == "__main__":
    main()

'''
# P.131 Implementation
def get_graph():
    graph = {}
    graph['Start'] = {}
    graph['Start']['A'] = 6
    graph['Start']['B'] = 2

    graph['A'] = {}
    graph['A']['Fin'] = 1

    graph['B'] = {}
    graph['B']['A'] = 3
    graph['B']['Fin'] = 5

    graph['Fin'] = {}

    return graph

def get_costs():
    costs = {}
    costs['A'] = 6
    costs['B'] = 2
    costs['Fin'] = float('inf')

    return costs

def get_parents():
    parents = {}
    parents['A'] = 'Start'
    parents['B'] = 'Start'
    parents['Fin'] = None

    return parents
'''

# P.139 Exercise A
def get_graph():
    graph = {}

    graph['Start'] = {}
    graph['Start']['A'] = 5
    graph['Start']['B'] = 2

    graph['A'] = {}
    graph['A']['C'] = 4
    graph['A']['D'] = 2

    graph['B'] = {}
    graph['B']['A'] = 8
    graph['B']['D'] = 7

    graph['C'] = {}
    graph['C']['D'] = 6
    graph['C']['Fin'] = 3

    graph['D'] = {}
    graph['D']['Fin'] = 1

    graph['Fin'] = {}

    return graph

def get_costs():
    costs = {}
    costs['A'] = 5
    costs['B'] = 2
    costs['C'] = float('inf')
    costs['D'] = float('inf')
    costs['Fin'] = float('inf')

    return costs

def get_parents():
    parents = {}
    parents['A'] = 'Start'
    parents['B'] = 'Start'
    parents['C'] = None
    parents['D'] = None
    parents['Fin'] = None

    return parents

def get_lowest_cost_node(costs, searched):
    lowest_node = None
    lowest_val = float('inf')

    for k, v in costs.items():
        if k not in searched and v < lowest_val:
            lowest_val = v
            lowest_node = k

    return lowest_node

def dijkstra(graph, costs, parents):
    searched = []

    node = get_lowest_cost_node(costs, searched)
    print(f'Next lowest cost node: {node}')

    while node is not None:
        neighbors = graph[node]
        cost = costs[node]

        for n in neighbors.keys():
            new_cost = cost + graph[node][n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        searched.append(node)
        node = get_lowest_cost_node(costs, searched)
        print(f'Next lowest cost node: {node}')

    return costs['Fin']

def display_output(shortest_path):
    print(f'The shortest path is: {shortest_path}.')

def main():
    graph = get_graph()
    costs = get_costs()
    parents = get_parents()
    shortest_path = dijkstra(graph, costs, parents)
    print(f'Parents: {parents}')
    print(f'Costs: {costs}')
    display_output(shortest_path)

main()

import queue

def get_graph():
    graph = {}
    # graph['you'] = ['alice']
    # graph['alice'] = ['you']
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    return graph

def check_name(node):
    if node[-1] == 'm':
        return True

    return False

def breadth_first_search(graph):
    search_queue = queue.Queue()
    search_queue.put(graph['you'])

    searched = []

    while search_queue.empty() is False:
        node_list = search_queue.get()

        for node in node_list:
            if node in searched:
                continue

            if check_name(node) is True:
                print(f'{node} is the guy!')
                return True
            else:
                searched.append(node)
                search_queue.put(graph[node])

    print('Not found!')
    return False

def main():
    graph = get_graph()
    breadth_first_search(graph)

main()

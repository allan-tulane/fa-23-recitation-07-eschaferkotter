from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        visiting = frontier.pop()
        result.add(visiting)
        for i in graph[visiting]:
          if i not in result:
            frontier.add(i)
    return result





def connected(graph):
    keys = list(graph.keys())[0]
    graphLen = len(graph)
    reachLength = len(reachable(graph, keys))

    if graphLen == reachLength:
      return True
    else:
      return False

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    components = []
    frontier = set(list(graph.keys()))
    
    while len(frontier) != 0:
      visited = frontier.pop()
      graphreach = reachable(graph, visited)
      frontier = frontier - graphreach
      components.append(graphreach)

    return len(components)


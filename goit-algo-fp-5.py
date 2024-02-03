import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def bfs_assign_colors(root):
    queue = [(root, 0)]
    visited_order_with_depth = []
    max_depth = 0
    while queue:
        (node, depth) = queue.pop(0)
        if node:
            visited_order_with_depth.append((node, depth))
            max_depth = max(max_depth, depth)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    color_palette = get_color_palette(max_depth + 1)
    for node, depth in visited_order_with_depth:
        node.color = color_palette[depth]


def get_color_palette(n):
    palette = []
    for i in range(n):
        intensity = int((1 - (i / n)) * 255)
        color = f'#{intensity:02x}{intensity:02x}ff'
        palette.append(color)
    return palette


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def dfs_assign_colors(root, depth=0, visited_order_with_depth=None):
    if visited_order_with_depth is None:
        visited_order_with_depth = []
    if root:
        visited_order_with_depth.append((root, depth))
        dfs_assign_colors(root.left, depth+1, visited_order_with_depth)
        dfs_assign_colors(
            root.right, depth+1, visited_order_with_depth)
    if root and len(visited_order_with_depth) == len(nodes):
        color_palette = get_color_palette(len(visited_order_with_depth))
        for i, (node, _) in enumerate(visited_order_with_depth):
            node.color = color_palette[i]


def draw_heap(array, traversal_type='BFS'):
    global nodes
    nodes = [Node(val) for val in array]
    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    if nodes:
        tree_root = nodes[0]
        if traversal_type == 'BFS':
            bfs_assign_colors(tree_root)
        elif traversal_type == 'DFS':
            dfs_assign_colors(tree_root)
        draw_tree(tree_root)


heap_array = [20, 18, 10, 12, 9, 8, 3, 5, 6]

print("BFS Traversal and Coloring:")
draw_heap(heap_array, 'BFS')
print("DFS Traversal and Coloring:")
draw_heap(heap_array, 'DFS')

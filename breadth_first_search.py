class Node:
  name: str = ''
  edges = []

  def __init__(self, name):
    self.name = name
    self.edges = []


root = Node('1')
root.edges.append(Node('2'))
root.edges.append(Node('3'))

root.edges[0].edges.append(Node('4'))
root.edges[0].edges.append(Node('5'))
root.edges[1].edges.append(Node('6'))
root.edges[1].edges.append(Node('7'))

def traverse(node):
  queue = [node]

  while queue:
    current_node = queue.pop(0)
    print(current_node.name)
    for n in current_node.edges:
      queue.append(n)

traverse(root)
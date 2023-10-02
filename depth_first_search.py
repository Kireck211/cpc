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

current_node = root

def traverse(node):
  print(node.name)
  if (len(node.edges) == 0):
    return
  for n in node.edges:
    traverse(n)

traverse(current_node)
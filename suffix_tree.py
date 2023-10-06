ACTION_INDEX = 0
SOURCE_INDEX = 1

class Node:
  suffix: str = ''
  edges = []

  def __init__(self, suffix):
    self.suffix = suffix
    self.edges = []

class SuffixTree:
  suffixes = []
  text = ""
  root = Node('')
  inserted = False
  first_execution = True
  suffix_index = 0
  
  def __init__(self, text):
    self.text = text
    self.suffixes = []
    self.root = Node('')
    self.build()

  def create_node(self, current_node, suffix):
    node = Node(suffix)
    current_node.edges.append(node)
  
  def is_first_execution(self, node):
    if (not self.first_execution):
      return self.first_execution
    
    if (node == self.root and len(node.edges) == 0):
      self.first_execution = False
      return True
  
  def traverse_dfs(self, node, suffix):
    if (self.is_first_execution(node)):
      node.edges.append(Node(suffix))
      return
    
    if(node != self.root):
      result = self.suffixesComparison(node, suffix)

      # if (result[ACTION_INDEX] == 'add_new_child'):
      #   new_node = Node(suffix)
      #   parent.edges.append(new_node)
      #   self.inserted = True
      #   return
      action = result[ACTION_INDEX]
      
      if (action == 'split_suffix'):
        index = result[SOURCE_INDEX]
        new_node = Node(suffix[index:])
        node.edges.append(new_node)
        self.inserted = True
        return
      
      elif (action == 'split_node'):
        mismatched_index = result[SOURCE_INDEX]
        node1 = Node(node.suffix[mismatched_index:])
        node2 = Node(suffix[mismatched_index:])

        node.suffix = suffix[0:mismatched_index]
        node.edges.append(node1)
        node.edges.append(node2)
        self.inserted = True
        return
      
      elif (action == 'continue_dfs'):
        remainig_index = result[SOURCE_INDEX]
        self.suffix_index = remainig_index
      
      elif(action == 'add_new_child'):
        return

    for n in node.edges:
      if (self.inserted):
        break
      self.traverse_dfs(n, suffix[self.suffix_index:])
    
    if (not self.inserted):
      new_node = Node(suffix[self.suffix_index:]) 
      node.edges.append(new_node)
      self.inserted = True
      return
  
  def suffixesComparison(self, node, suffix):
    target_index, source_index = 0, 0
    target_length = len(suffix)
    source_length = len(node.suffix)
    hasMatched = False
    while True:
      if (target_index >= target_length):
        break
      if (source_index >= source_length):
        if (hasMatched):
          return ('continue_dfs', source_index)
        return ('split_suffix', source_index)

      if (suffix[target_index] != node.suffix[source_index]):
        if (hasMatched):
          return ('split_node', source_index)
        return ('add_new_child', None)

      hasMatched = True
      
      target_index += 1
      source_index += 1
  
  def clear_insertion(self):
    self.inserted = False
    self.suffix_index = 0
  
  # TODO(Kireck211): implement substring search on tree
  def exist_substring(self, text):
    pass

  def build(self):
    self.generateSuffixes()
    for suffix in self.suffixes:
      self.clear_insertion()
      self.traverse_dfs(self.root, suffix)
      
  def generateSuffixes(self):
    text_length = len(self.text)
    for i in range(text_length):
      self.suffixes.append(self.text[text_length-i-1:])


def main():
  tree1: SuffixTree = SuffixTree('banana')
  print('Finished tree1')
  tree2: SuffixTree = SuffixTree('bba')
  print('Finished tree3')
  tree3: SuffixTree = SuffixTree('CAGTCAGG')
  print('Finished tree2')


if __name__ == '__main__':
  main()
"""
    Serialize and Deserialize a Binary tree
"""

class TreeNode():
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinayTreeSerializator():
    @staticmethod
    def serialize(root: TreeNode) -> str:
        result = []
        def tree_to_serialized_list(node: TreeNode):
            if not node:
                result.append('None')
            else:
                result.append(str(node.value))
                tree_to_serialized_list(node.left)
                tree_to_serialized_list(node.right)
        tree_to_serialized_list(root)
        return ' '.join(result)
    
    @staticmethod
    def deserialize(serialized_tree: str) -> TreeNode:
        tree_list = serialized_tree.split(' ')
        iterator = iter(tree_list)
        def dsr():
            val = next(iterator)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = dsr()
            node.right = dsr()
            return node
        return dsr()



if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(6), TreeNode(7)), TreeNode(3, TreeNode(4), TreeNode(5)))
    #BinayTreeSerializator.serialize(tree))
    BinayTreeSerializator.deserialize(BinayTreeSerializator.serialize(tree))
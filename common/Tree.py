class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    @staticmethod
    def InOrderArray(node, inArr):
        if not node:
            return
        if node.left:
            Node.InOrderArray(node.left, inArr)
        inArr.append(node.data)
        if node.right:
            Node.InOrderArray(node.right, inArr)

    @staticmethod
    def Depth(node):
        if not node:
            return 0
        return max(Node.Depth(node.left), Node.Depth(node.right)) + 1

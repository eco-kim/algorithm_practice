from collections import defaultdict
import sys 
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, idx,x):
        self.idx = idx
        self.value = x
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, nodeinfo): ##정렬하여 넣어야함
        root = nodeinfo[0]
        self.root = Node(root[2],root[0])
        
        for node in nodeinfo[1:]:
            value = node[0]
            self.current_node = self.root
            while True:
                if value < self.current_node.value:
                    if self.current_node.left != None:
                        self.current_node = self.current_node.left
                    else:
                        self.current_node.left = Node(node[2],node[0])
                        break
                else:
                    if self.current_node.right != None:
                        self.current_node = self.current_node.right
                    else:
                        self.current_node.right = Node(node[2],node[0])
                        break
    
    def pre_order_traversal(self):
        route = []
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                data = root.idx
                if data not in route:
                    route.append(data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
        return route
    
    def post_order_traversal(self):
        route = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                data = root.idx
                if data not in route:
                    route.append(data)
        _post_order_traversal(self.root)
        return route
    
def solution(nodeinfo):
    for i, node in enumerate(nodeinfo):
        node += [i+1]
    nodeinfo.sort(key = lambda x: (-x[1],x[0]))
    bst = BST(nodeinfo)
    
    answer = [bst.pre_order_traversal(), bst.post_order_traversal()]
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42892

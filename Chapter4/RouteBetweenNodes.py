from common.Graph import *
from collections import deque
import unittest

def RouteViaDFS(G, source, destination):
    for v in G:
        v.visited = False
    return DFSVisit(source, destination)

def DFSVisit(u, destination):
    if u == destination:
        return True
    if u.visited:
        return False
    u.visited = True
    for v in u.adjacencyList:
        if DFSVisit(v, destination):
            return True
    return False

def RouteViaBFS(G, source, destination):
    for u in G:
        u.visited = False
    Q = deque()
    source.visited = True
    Q.append(source)
    while len(Q):
        u = Q.popleft()
        if destination == u:
            return True
        for v in u.adjacencyList:
            if v.visited == False:
                v.visited = True
                Q.append(v)
    return False

class TestRouteBetweenNodes(unittest.TestCase):
    def driver(self, G, source, destination, expected):
        self.assertEqual(expected, RouteViaDFS(G, source, destination))
        self.assertEqual(expected, RouteViaBFS(G, source, destination))
    def test_RouteBetweenNodes(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        a.AddAjacencyList([b])
        b.AddAjacencyList([c,d])
        e.AddAjacencyList([f])
        f.AddAjacencyList([g])
        g.AddAjacencyList([e])

        G = [a, b, c, d, e , f, g]
        self.driver(G, a, e, False)
        self.driver(G, a, d, True)
        self.driver(G, c, d, False)
        self.driver(G, e, g, True)

if __name__ == "__main__":
    unittest.main()

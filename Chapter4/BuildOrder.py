from common.Graph import *
import common.Graph
import unittest

def BuildOrderDFSVisit(u, buildOrder):
    if u.visited:
        return True
    u.visiting = True
    for v in u.adjacencyList:
        #Cycle
        if v.visiting:
            return False
        if not BuildOrderDFSVisit(v, buildOrder):
            return False
    u.visiting = False
    u.visited = True
    buildOrder.append(u)
    return True

def BuildOrder(G):
    for u in G:
        u.visiting = False
        u.visited = False
    buildOrder = []
    for u in G:
        if not BuildOrderDFSVisit(u, buildOrder):
            return None
    return buildOrder

class TestBuildOrder(unittest.TestCase):
    #do we expect a buildOrder Or Not
    def driver(self, G, expected):
        buildOrder = BuildOrder(G)
        if not expected:
            self.assertEqual(buildOrder, expected)
            return
        self.assertIsNotNone(buildOrder)
        for i in range(len(buildOrder)):
            buildOrder[i].BuildIndex = i
        for u in G:
            for v in u.adjacencyList:
                self.assertTrue(v.BuildIndex < u.BuildIndex)

    def test_BuildOrder(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        d.AddAjacencyList([a,b])
        b.AddAjacencyList([f])
        a.AddAjacencyList([f])
        c.AddAjacencyList([d])

        G = [a, b, c, d, e , f]
        self.driver(G, "Yes")
        b.AddAjacencyList([f,c])
        self.driver(G, None)

if __name__ == "__main__":
    unittest.main()

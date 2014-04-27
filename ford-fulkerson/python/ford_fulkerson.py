class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v  
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
 
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
        self.forward = {}
        self.backward = {}
        self.st_minnn = []
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
        self.forward[vertex] = []
        self.backward[vertex] = []
 
    def get_edges(self, v):
        # print "here : " , self.adj[v]
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge  #redge is not defined in Edge class
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.forward[u].append(edge)
        self.backward[u].append(redge)
        # print "\n\nForward: ", self.forward[u]
        # print "Backward: ", self.backward[u]

        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge]) 
                if result != None:
                    return result

    def st_mincut(self,source,list_of_vertexes):
        # print "\n\n"
        flag=0
        for edge in self.adj[source]:
            # print edge
            # print edge.capacity - self.flow[edge]
            # if edge in self.forward[source]:
                # print "Forward Edge"
            # else:
                # print "Backward Edge"

            if (edge.capacity > self.flow[edge]) and edge in self.forward[source] and edge.sink not in list_of_vertexes:
                # print "forward: ", edge
                flag=1
                result = self.st_mincut(edge.sink, list_of_vertexes + [edge.sink])
                if result != None:
                    return result
            elif (self.flow[edge]>0) and edge in self.backward[source] and edge.source not in list_of_vertexes:
                # print "backward: ", edge
                result = self.st_mincut(edge.source, list_of_vertexes + [edge.source])
                flag=1
                if result != None:
                    return result
        self.st_minnn.append(list_of_vertexes)

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        i=1
        while path != None:
            # print "\n", i, " step: ", path
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            # print "Residuals in step ", i, ": ", residuals
            i+=1
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
                # print "edge : ", edge, ", flow: ", self.flow[edge], ", back edge: ", edge.redge, ", back flow", self.flow[edge.redge]
            path = self.find_path(source, sink, [])
        size = 0
        self.st_mincut(source, [source])
        for item in self.st_minnn:
            if len(item)>size:
                st_min = item
                size = len(item)
        print "Min cut: ", st_min

        return sum(self.flow[edge] for edge in self.get_edges(source))
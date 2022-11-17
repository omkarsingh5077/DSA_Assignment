from collections import defaultdict

class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
 
# Driver's code
 
 
# Create a graph given
# in the above diagram
if __name__ == "__main__":
    g = Graph()
    c=1
    while(c==1):
        edge=input("Enter the ordinate and abcissa").split(" ")
        g.addEdge(edge[0],edge[1])
        c=int(input("Enter 1 to continue adding new points to graph"))
    
    x=int(input("Enter the starting point for traversal"))
    print("Following is DFS from (starting from x)")
    # Function call
    g.DFS(x)
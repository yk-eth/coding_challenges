
from collections import defaultdict




def form_adjacency_list():
	# mapping = defaultdict(int)
	listt = [
  { 'name': "A", 'connections': ["B", "C"] },
  { 'name': "B", 'connections': ["A", "E"] },
  { 'name': "C", 'connections': ["A", "D"] },
  { 'name': "D", 'connections': ["C"] },
  { 'name': "E", 'connections': ["B", "F"] },
  { 'name': "F", 'connections': ["E"] },
]
	mapping = dict()
	adj_list = dict()
	for i,entry in enumerate(listt):
		# print(entry)
		node = entry["name"]
		neigh = entry["connections"]
		adj_list[node] = neigh
		mapping[node] = i

	# print(adj_list)
	return adj_list,mapping

def bfs_with_path(adj_list,mapping,src,dest):

	parent = [-1]*len(mapping)
	parent[mapping[src]] = src
	q = [src]

	while len(q) > 0:
		node = q.pop()

		for entry in adj_list[node]:
			if parent[mapping[entry]] == -1:
				parent[mapping[entry]] = node
				q.append(entry)
				if entry == dest:
					return True,parent
	return False,parent




adj_list,mapping = form_adjacency_list()
source = "D"
dest = "A"
exist,parent = bfs_with_path(adj_list,mapping,source,dest)
# print(F"{exist},{parent}")

if exist:
	node = dest
	stack = []
	while node != source:
		# print (F"{node} -> ")
		stack.insert(0,node)
		node = parent[mapping[node]]
		if node == source:
			stack.insert(0,node)
	for entry in stack[:-1]:
		print(entry, "->", end=" ")
	print(stack[-1])			

else :
	print("no path exists")





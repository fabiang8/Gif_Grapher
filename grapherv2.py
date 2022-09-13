#!/usr/bin/python3
import pygraphviz as pgv
import subprocess
#This code will read in the first few lines of duplications.txt and create a complete graph
def invis_graph(I):
	with open("duplications.txt") as f:
		num_parents=int(f.readline())
		for nodeID in range(1,num_parents+1):
			I.add_node(nodeID)
			I.get_node(nodeID).attr['style']="invis"
			I.get_node(nodeID)
		for nodeID in range(1,num_parents+1):
			color=f.readline().strip()
			I.get_node(nodeID).attr['color']=color
			for dest in range(nodeID+1,num_parents+1):
				I.add_edge(nodeID,dest,style="invis")
				I.add_edge(nodeID,dest)
def add_nodes_invis(I):
	with open("duplications.txt") as f:
		num_parents=int(f.readline())
		for node2add in f:
			if ' ' in node2add:
				#print(node2add)
				#print("node2add value : ", node2add)
				commandlist=node2add.split()
				new_node = commandlist[0]
				node_copy = commandlist[1]
				I.add_node(new_node)
				new_color = I.get_node(node_copy).attr['color']
				I.get_node(new_node).attr['color'] = new_color
				I.get_node(new_node).attr['style']="invis"
				#print("this is the value of copy_node", node_copy)
				#print("this is the copied nodes color",new_color)
                                #print("value of commandlist before edgeadder:", *>

                                #commandlist.pop(0)
                                #commandlist.pop(1)
				edge_adder_invis(commandlist,I)
                                #print(*commandlist)
			else:
                                #print(node2add)
				continue
				
def edge_adder_invis(commandlist,G):
	print("printing commandlist from edge_adder:",*commandlist)
	new_node = commandlist[0]
	move_edge = commandlist[1]
	copy = "c"
	move = "m"
	for command in commandlist:
		if copy in command:
                        # add copy edges
			print("printing command from edge_adder-copy:")
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			print("printing final cut copy:", dest_node)
			G.add_edge(new_node, dest_node,style="invis")
			G.add_edge(new_node,dest_node)
		elif move in command:
			print("printing command from edge_adder-move:")
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			print(" printing final cut move:", dest_node)
			G.delete_edge(move_edge,dest_node)
			G.add_edge(new_node, dest_node,style="invis")
			G.add_edge(new_node,dest_node)
                        # G.delete_edge(dummy, dummy2)
                        # add move edges
		else:
			continue

def create_og_graph(I):
	length=file_len("duplications.txt")
	with open("duplications.txt") as f:
		num_parents = int(f.readline())
		for i in range(length,length + num_parents):
			parent= (i - length) + 1
			node_color = I.get_node(parent).attr['color']
			node_pos = I.get_node(parent).attr['pos']
			print("printing create_og_graph values: ", node_color, node_pos, parent)
			I.add_node(i,color=node_color,pos=node_pos)
		for i in range(length,length+num_parents):
			for j in range(i + 1, length + num_parents):
				I.add_edge(i,j)

def create_gif(I):
	# create directory
	# cd into director
	# for every command create the 10 positional images
	subprocess.call(['mkdir',"gif_dir"])
	length=file_len("duplications.txt")
	with open("duplications.txt") as f:
		num_parents = int(f.readline())
		start_range = length + num_parents
		end_range = (length*2) - 2
		for line in f:
			if ' ' in line:  # command lines
				commandlist = line.split()
				new_node = commandlist[0]
				copy_node = commandlist[1]
				#new_nodev = (new_node + length) - 1 # position of invisible node
				#copy_nodev = (copy_node + length) - 1
				#generate_gifs(I,new_node,copy_node)
				I.add_node(start_range) # create new node on invisible node
				cpy_ptr = I.get_node(copy_node)
				cpy_ptr_color = cpy_ptr.attr['color'] # color of copy node
				I.get_node(start_range).attr['color'] = cpy_ptr_color	# setting color of copy node
				I.get_node(start_range).attr['pos'] = cpy_ptr.attr['pos']
				I.get_node(start_range).attr['label'] = new_node #setting colored node on top of invis node
				gif_edge(commandlist,I)
				generate_gifs(I,new_node,copy_node,start_range) # moves node along 10 steps 
				start_range += 1
				break
			else:
				continue

def gif_edge(commandlist,I):
	new_node = commandlist[0]
	move_edge = commandlist[1]
	copy = "c"
	move = "m"
	for command in commandlist:
		if copy in command:
			numeric_filter = filter(str.isdigit,command)
			dest_node = "".join(numeric_filter)
			I.add_edge(new_node,dest_node)
		elif move in command:
			numeric_filter = filter(str.isdigit,command)
			dest_node = "".join(numeric_filter)
			I.delete_edge(move_edge,dest_edge)
			I.add_edge(new_node,dest_node)
		else:
			continue

def generate_gifs(I,new_node,copy_node,start_range):
	pos_node = I.get_node(new_node).attr['pos']
	pos_copy = I.get_node(copy_node).attr['pos']
	pos_node_list = pos_node.split(',')
	pos_copy_list = pos_copy.split(',')
	node_xdelta = float(pos_node_list[0]) - float(pos_copy_list[0])
	node_ydelta = float(pos_node_list[1]) - float(pos_copy_list[1])
	new_pos = []
	com =","
	for i in range(1,11):
		child_x_value = ((float(pos_copy_list[0]) + node_xdelta)*i)/10
		child_y_value = ((float(pos_copy_list[1]) + node_ydelta)*i)/10
		print("printing x,y values:",child_x_value,child_y_value)
		curpos = str(child_x_value) + com + str(child_y_value)
		I.get_node(start_range).attr['pos'] = curpos
		break


	#subprocess.call("mv *.gif gif_dir/", shell=True) # move all gif files into gif folder
def labler_color(I):
	with open("duplications.txt") as f:
		num_parents = int(f.readline())
		length = file_len("duplications.txt")
		for i in range(length, length + num_parents):
			new_label = (i - length) + 1
		I.get_node(i).attr['label'] = new_label
def initial_graph(I):
	with open("duplications.txt") as f:
		num_parents=int(f.readline())
		#G=pgv.AGraph()
		for nodeID in range(1,num_parents+1):
			G.add_node(nodeID)
		for nodeID in range(1,num_parents+1):
			color=f.readline().strip()
			G.get_node(nodeID).attr['color']=color
			for dest in range(nodeID+1,num_parents+1):
				G.add_edge(nodeID, dest)
		#print("G=",G)
		#G.layout()
		#G.draw("file2.png")

def add_nodes(G):
	with open("duplications.txt") as f:
		num_parents=int(f.readline())
		for node2add in f:
			if ' ' in node2add:
				#print(node2add)
				#print("node2add value : ", node2add)
				commandlist=node2add.split()
				new_node = commandlist[0]
				node_copy = commandlist[1]
				G.add_node(new_node)
				new_color = G.get_node(node_copy).attr['color']
				G.get_node(new_node).attr['color'] = new_color
				#print("this is the value of copy_node", node_copy)
				#print("this is the copied nodes color",new_color)
				#print("value of commandlist before edgeadder:", *commandlist)

				#commandlist.pop(0)
				#commandlist.pop(1)
				edge_adder(commandlist,G)
				#print(*commandlist)
			else:
				#print(node2add)
				continue
def edge_adder(commandlist,G):
	print("printing commandlist from edge_adder:",*commandlist)
	new_node = commandlist[0]
	move_edge = commandlist[1]
	copy = "c"
	move = "m"
	for command in commandlist:
		if copy in command:
			# add copy edges
			print("printing command from edge_adder-copy:" ,command)
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			print("printing final cut copy:", dest_node)
			G.add_edge(new_node, dest_node)
		elif move in command:
			print("printing command from edge_adder-move:", command)
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			print(" printing final cut move:", dest_node)
			G.delete_edge(move_edge,dest_node)
			G.add_edge(new_node, dest_node)
			# G.delete_edge(dummy, dummy2)
			# add move edges
		else:
			continue
def invis_labeler(I):
	length=file_len("duplications.txt")
	print("value of length in invis_labeler: ", length)
	endrange=(length*2)- 1
	length -= 1
	for i in range(1,length + 1):
		new_value = i + length
		I.get_node(i).attr['label']=new_value
def file_len(file):
	with open(file) as f:
		for i, l in enumerate(f):
			pass
	return i+1
#main loop
# so far this program creates intial complete graph and creates nodes from .txt file
# we still need to connect all nodes, by creating the edge_adder function
print("getting node count for invis graph: ")
I=pgv.AGraph()
invis_graph(I)
add_nodes_invis(I)
#I.get_node(1).attr['label'] = "17"
invis_labeler(I)
I.graph_attr['overlap']="scale"
I.graph_attr['outputorder']="edgesfirst"
I.node_attr['style']="filled"
I.node_attr['shape']="circle"
I.node_attr['fixedsize']="true"
I.layout(prog="neato")
create_og_graph(I)
labler_color(I)
for i in I:
	print(I.get_node(i))
create_gif(I)
print(I.get_node(21).attr['color'])
print(I.get_node(21).attr['pos'])
print(I.get_node(21).attr['label'])
#labler_color(I)
#print("printing pos of 4:")
#print(I.get_node(4).attr['pos'])
#print("printing pos of 5:")
#print(I.get_node(5).attr['pos'])
I.draw("file3.png")

#G=pgv.AGraph()
#initial_graph(G)
#add_nodes(G)
#G.graph_attr['overlap']="scale"
#G.graph_attr['outputorder']="edgesfirst"
#G.node_attr['style']="filled"
#G.node_attr['shape']="circle"
#G.node_attr['fixedsize']="true"
#G.layout(prog="neato")
#print("printing pos of 4:")
#print(G.get_node(4).attr['pos'])
#print("printing pos of 5:")
#print(G.get_node(5).attr['pos'])
#G.draw("file2.png")


#!/usr/bin/python3
import pygraphviz as pgv
import subprocess
import os
import math
import sys
def file_len(file):
	with open(file) as f:
		for i, l in enumerate(f):
			pass
	return i+1
def invis_graph(I):
	length = file_len("duplications.txt")
	start_range = length # 17
	with open("duplications.txt") as f: # add nodes using SECOND range not first
		num_parents=int(f.readline())
		end_range = start_range + num_parents
		for nodeID in range(start_range,end_range):
			I.add_node(nodeID)
			I.get_node(nodeID).attr['style']="invis"  # makes nodes invis
			I.get_node(nodeID)
		for nodeID in range(start_range,end_range):  # nodes added are 17 - 20
			color=f.readline().strip()
			I.get_node(nodeID).attr['color']=color
			for dest in range(nodeID+1,end_range):
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
				new_node = int(new_node) + 16
				node_copy = int(node_copy) + 16
				I.add_node(new_node)
				new_color = I.get_node(node_copy).attr['color']
				I.get_node(new_node).attr['color'] = new_color
				I.get_node(new_node).attr['style']="invis" # unmute this
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
	new_node = int(new_node) + 16
	move_edge = int(move_edge) + 16
	copy = "c"
	move = "m"
	for command in commandlist:
		if copy in command:
                        # add copy edges
			print("printing command from edge_adder-copy:")
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			print("printing final cut copy:", dest_node)
			dest_node = int(dest_node) + 16
			G.add_edge(new_node, dest_node,style="invis")
			G.add_edge(new_node,dest_node)
		elif move in command:
			print("printing command from edge_adder-move:")
			numeric_filter = filter(str.isdigit, command)
			dest_node = "".join(numeric_filter)
			dest_node = int(dest_node) + 16
			print(" printing final cut move:", dest_node)
			G.delete_edge(move_edge,dest_node)
			G.add_edge(new_node, dest_node,style="invis")
			G.add_edge(new_node,dest_node)
                        # G.delete_edge(dummy, dummy2)
                        # add move edges
		else:
			continue
def create_og_graph(I):
	with open("duplications.txt") as f:
		length = file_len("duplications.txt")
		num_node = length - 1
		num_parents = int(f.readline())
		for i in range(1,num_parents+1):
			parent = i + num_node
			node_color = I.get_node(parent).attr['color']
			node_pos = I.get_node(parent).attr['pos']
			print("printing create_og_graph values: ", node_color, node_pos, parent)
			I.add_node(i,color=node_color,pos=node_pos)
		for i in range(1,num_parents+1):
			for j in range(i + 1,num_parents + 1):
				I.add_edge(i,j)


def create_gif(I,choice):
	# create directory
	# cd into director
	# for every command create the 10 positional images
	log = "log"
	lin = "lin"
	subprocess.call(['mkdir',"gif_dir"])
	subprocess.call(['mkdir',"gif_dir_log"])
	length=file_len("duplications.txt")
	with open("duplications.txt") as f:
		num_parents = int(f.readline())
		start_range = num_parents + 1 # 5
		end_range = length - 1 # 16
		anim_count = 1
		for line in f:
			if ' ' in line:  # command lines
				commandlist = line.split()
				new_node = commandlist[0]
				copy_node = commandlist[1]
				copy_node = int(copy_node) + 16
				#new_nodev = (new_node + length) - 1 # position of invisible node
				#copy_nodev = (copy_node + length) - 1
				#generate_gifs(I,new_node,copy_node)
				I.add_node(new_node) # create new node on invisible node
				cpy_ptr = I.get_node(copy_node)
				cpy_ptr_color = cpy_ptr.attr['color'] # color of copy node
				I.get_node(new_node).attr['color'] = cpy_ptr_color	# setting color of copy node
				I.get_node(new_node).attr['pos'] = cpy_ptr.attr['pos']
				I.get_node(new_node).attr['label'] = new_node #setting colored node on top of invis node
				#gif_edge(commandlist,I)
				print("value of pos of newnode: ", I.get_node(new_node).attr['pos'])

				if lin in choice:
					generate_gifs(I,new_node,commandlist,anim_count) # moves node along 10 steps=
				elif log in choice:
					generate_gifs_log(I,new_node,commandlist,anim_count)
				else:
					print("Log or Linear not specified: Error!")
				#edge_del = True
				anim_count += 1
			else:
				continue

def gif_edge(commandlist,I,edge_del):
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
			if edge_del is False:
				numeric_filter = filter(str.isdigit,command)
				dest_node = "".join(numeric_filter)
				I.delete_edge(move_edge,dest_node)
				I.add_edge(new_node,dest_node)
				edge_del = True
			else:
				numeric_filter = filter(str.isdigit,command)
				dest_node = "".join(numeric_filter)
				I.add_edge(new_node,dest_node)
		else:
			continue

def gif_edge_exp(commandlist,I):
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
			I.delete_edge(move_edge,dest_node)
			I.add_edge(new_node,dest_node)
		else:
			continue
def format_graph(I):
	I.graph_attr['overlap']="scale"
	I.graph_attr['outputorder']="edgesfirst"
	I.node_attr['style']="filled"
	I.node_attr['shape']="circle"
	I.node_attr['fixedsize']="true"

def generate_gifs_log(I,new_node,commandlist,anim_count):
	togo = int(new_node) + 16
	print("printing value of togo:", new_node, togo)
	pos_node = I.get_node(new_node).attr['pos']
	pos_togo = I.get_node(togo).attr['pos']
	print(pos_node,pos_togo)
	pos_node_list = pos_node.split(',')
	pos_copy_list = pos_togo.split(',')
	node_xdelta = float(pos_copy_list[0]) - float(pos_node_list[0])
	node_ydelta = float(pos_copy_list[1]) - float(pos_node_list[1])
	print("vaue of delta:", node_xdelta, node_ydelta)
	new_pos = []
	com =","
	anim_end = anim_count * 10
	anim_cur = anim_end - 10
	edge_del = False
	gif_edge_exp(commandlist,I)
	print("printing height")
	I.get_node(new_node).attr['width'] = 0.5
	I.get_node(new_node).attr['height'] = 0.5
	#print(I.get_node(new_node).attr['width'])
	cur_node_h =float(I.get_node(new_node).attr['height'])
	cur_node_w =float(I.get_node(new_node).attr['width'])
	new_height = cur_node_h * 2
	new_width = cur_node_w *2
	delta_h = new_height - cur_node_h
	delta_w = new_width - cur_node_w
	for i in range(1,11):
		if anim_cur < anim_end:
			file1 = "anim_log"
			ext = ".gif"
			digit = "{0:03}".format(anim_cur)
			new_file = file1 + str(digit) + ext
			print(new_file)
			anim_cur += 1
		else:
			pass
		x_in = float(pos_node_list[0])
		y_in = float(pos_node_list[1])
		child_x_value = (x_in + node_xdelta*(1-math.log10(11-i)))
		child_y_value = (y_in + node_ydelta*(1-math.log10(11-i)))
		print("printing x,y values:",child_x_value,child_y_value)
		curpos = str(child_x_value) + com + str(child_y_value)
		I.get_node(new_node).attr['pos'] = curpos
		child_w_value = new_width - (delta_w*i/10)
		child_h_value = new_height - (delta_h*i/10)
		I.get_node(new_node).attr['width'] = child_w_value
		I.get_node(new_node).attr['height'] = child_h_value
		#gif_edge(commandlist,I,edge_del)
		#edge_del = True
		format_graph(I)
		I.draw(new_file)
		subprocess.call(['mv',new_file,"gif_dir_log"])
def generate_gifs(I,new_node,commandlist,anim_count):
	togo = int(new_node) + 16
	print("printing value of togo:", new_node, togo)
	pos_node = I.get_node(new_node).attr['pos']
	pos_togo = I.get_node(togo).attr['pos']
	print(pos_node,pos_togo)
	pos_node_list = pos_node.split(',')
	pos_copy_list = pos_togo.split(',')
	node_xdelta = float(pos_copy_list[0]) - float(pos_node_list[0])
	node_ydelta = float(pos_copy_list[1]) - float(pos_node_list[1])
	print("vaue of delta:", node_xdelta, node_ydelta)
	new_pos = []
	com =","
	anim_end = anim_count * 10
	anim_cur = anim_end - 10
	edge_del = False
	gif_edge_exp(commandlist,I)
	I.get_node(new_node).attr['width'] = 0.5
	I.get_node(new_node).attr['height'] = 0.5
	cur_node_h =float(I.get_node(new_node).attr['height'])
	cur_node_w =float(I.get_node(new_node).attr['width'])
	new_height = cur_node_h * 2
	new_width = cur_node_w * 2
	delta_h = new_height - cur_node_h
	delta_w = new_width - cur_node_w
	for i in range(1,11):
		if anim_cur < anim_end:
			file1 = "anim"
			ext = ".gif"
			digit = "{0:03}".format(anim_cur)
			new_file = file1 + str(digit) + ext
			print(new_file)
			anim_cur += 1
		else:
			pass
		x_in = float(pos_node_list[0])
		y_in = float(pos_node_list[1])
		child_x_value = x_in + (node_xdelta*i/10)
		child_y_value = y_in + (node_ydelta*i/10)
		print("printing x,y values:",child_x_value,child_y_value)
		curpos = str(child_x_value) + com + str(child_y_value)
		I.get_node(new_node).attr['pos'] = curpos
		#gif_edge(commandlist,I,edge_del)
		#gif_edge_exp(commandlist,I)
		#edge_del = True
		child_w_value = new_width - (delta_w*i/10)
		child_h_value = new_height - (delta_h*i/10)
		I.get_node(new_node).attr['width'] = child_w_value
		I.get_node(new_node).attr['height'] = child_h_value
		format_graph(I)
		I.draw(new_file)
		subprocess.call(['mv',new_file,"gif_dir"])
#Main loop
choice=sys.argv[2]
I=pgv.AGraph()
invis_graph(I)
add_nodes_invis(I)
format_graph(I)
I.layout(prog="neato")
create_og_graph(I)
create_gif(I,choice)
for i in I:
	print(I.get_node(i))
log = "log"
lin = "lin"
if lin in choice:
	os.system("gifsicle --colors 256 --delay=10 --optimize=3 gif_dir/* >finalanim.gif")
elif log in choice:
	os.system("gifsicle --colors 256 --delay=10 --optimize=3 gif_dir_log/* >finalanim_log.gif")
else:
	print("No choice specified:")




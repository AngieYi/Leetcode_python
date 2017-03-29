def findPath(maze, source, dest):
	row_n = len(maze)
	if row_n == 0:
		return 0
	col_n = len(maze[0])
	visited = set()
	bfsQueue = [source]
	while bfsQueue:
		curr = bfsQueue.pop(0)
		if curr == dest:
			return maze[curr[0]][curr[1]] - 1
		visited.add(str(curr))
		if curr[0] > 0 and maze[curr[0] - 1][curr[1]] != 0 and str([curr[0] - 1, curr[1]]) not in visited:
			bfsQueue.append([curr[0] - 1, curr[1]])
			maze[curr[0] - 1][curr[1]] = maze[curr[0]][curr[1]] + 1
		if curr[0] < row_n - 1 and maze[curr[0] + 1][curr[1]] != 0 and str([curr[0] + 1, curr[1]]) not in visited:
			bfsQueue.append([curr[0] + 1, curr[1]])
			maze[curr[0] + 1][curr[1]] = maze[curr[0]][curr[1]] + 1
		if curr[1] > 0 and maze[curr[0]][curr[1] - 1] != 0 and str([curr[0], curr[1] - 1]) not in visited:
			bfsQueue.append([curr[0], curr[1] - 1])
			maze[curr[0]][curr[1] - 1] = maze[curr[0]][curr[1]] + 1
		if curr[1] < col_n - 1 and maze[curr[0]][curr[1] + 1] != 0 and str([curr[0], curr[1] + 1]) not in visited:
			bfsQueue.append([curr[0], curr[1] + 1])
			maze[curr[0]][curr[1] + 1] = maze[curr[0]][curr[1]] + 1
	return 0

def main():
	maze = [
				[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
				[ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
				[ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
				[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
				[ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
				[ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
				[ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
				[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
				[ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
			]
	source = [0, 0]
	dest = [8, 1]
	print "Shortest path is: " + str(findPath(maze, source, dest))

if __name__ == "__main__":
	main()
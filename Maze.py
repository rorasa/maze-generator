class Node:
    def __init__(self, type):
        self.type = type
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        
        self.updateOpening(type)
        
    def setOpening(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        
    def updateOpening(self, type):
        if type=='0':
            self.setOpening(north=False, south=False, east=False, west=False)
        elif type=='1':
            self.setOpening(north=True, south=False, east=False, west=False)
        elif type=='2':
            self.setOpening(north=False, south=False, east=True, west=False)
        elif type=='3':
            self.setOpening(north=False, south=True, east=False, west=False)
        elif type=='4':
            self.setOpening(north=False, south=False, east=False, west=True)
        elif type=='5':
            self.setOpening(north=True, south=True, east=False, west=False)
        elif type=='6':
            self.setOpening(north=False, south=False, east=True, west=True)
        elif type=='7':
            self.setOpening(north=False, south=True, east=True, west=False)
        elif type=='8':
            self.setOpening(north=False, south=True, east=False, west=True)
        elif type=='9':
            self.setOpening(north=True, south=False, east=False, west=True)
        elif type=='a':
            self.setOpening(north=True, south=False, east=True, west=False)
        elif type=='b':
            self.setOpening(north=True, south=True, east=True, west=False)
        elif type=='c':
            self.setOpening(north=False, south=True, east=True, west=True)
        elif type=='d':
            self.setOpening(north=True, south=True, east=False, west=True)
        elif type=='e':
            self.setOpening(north=True, south=False, east=True, west=True)
        else:
            self.setOpening(north=True, south=True, east=True, west=True)
            
class Board:
    def __init__(self, size):
        self.nodes = [[Node('0') for i in range(0,size)] for j in range(0,size)]
        self.grid = [[' ' for i in range(0,len(self.nodes[0])*3+1)] for j in range(0,len(self.nodes)*3+1)]
        
        self.updateGrid()
        
    def fillBlocksHorizontal(self, filler, row, col, fill_range):
         for jdx in range(0,fill_range):
            self.grid[row][col+jdx] = filler
            
    def fillBlocksVertical(self, filler, row, col, fill_range):
         for idx in range(0,fill_range):
            self.grid[row+idx][col] = filler
        
    def updateGrid(self):
        # First pass - fill horizontal edges
        self.updateHorizontalEdges()
        # Second pass - fill vertical edges
        self.updateVerticalEdges()
        # Third pass - rectify corners
        self.updateCorners()
        
    def updateHorizontalEdges(self):
        for i in range(0,len(self.nodes)):
            for j in range(0,len(self.nodes[0])):
                
                node = self.nodes[i][j]
                
                # For topmost row
                if i==0:
                    if node.north==True:
                        self.fillBlocksHorizontal(' ', i*3, j*3, 4)
                    else:
                        self.fillBlocksHorizontal('═', i*3, j*3, 4)
                        
                # For bottommost row
                elif i==len(self.nodes)-1:
                    if node.south==True:
                        self.fillBlocksHorizontal(' ', i*3+3, j*3, 4)
                    else:
                        self.fillBlocksHorizontal('═', i*3+3, j*3, 4)
                        
                # For middle rows
                else:
                    upnode = self.nodes[i-1][j]
                    downnode = self.nodes[i+1][j]

                    if node.north==True and upnode.south==True:
                        self.fillBlocksHorizontal(' ', i*3, j*3, 4)
                    elif node.north==False and upnode.south==False:
                        self.fillBlocksHorizontal('═', i*3, j*3, 4)
                    else:
                        raise ValueError("Board corrupts")

                    if node.south==True and downnode.north==True:
                        self.fillBlocksHorizontal(' ', i*3+3, j*3, 4)
                    elif node.south==False and downnode.north==False:
                        self.fillBlocksHorizontal('═', i*3+3, j*3, 4)
                    else:
                         raise ValueError("Board corrupts")
                            
    def updateVerticalEdges(self):
        for i in range(0,len(self.nodes)):
            for j in range(0,len(self.nodes[0])):
                
                node = self.nodes[i][j]
                
                # For leftmost column
                if j==0:
                    if node.west==True:
                        self.fillBlocksVertical(' ', i*3, j*3, 4)
                    else:
                        self.fillBlocksVertical('║', i*3, j*3, 4)

                # For rightmost column
                elif j==len(self.nodes[0])-1:
                    if node.east==True:
                        self.fillBlocksVertical(' ', i*3, j*3+3, 4)
                    else:
                        self.fillBlocksVertical('║', i*3, j*3+3, 4)

                # For middle columns
                else:
                    leftnode = self.nodes[i][j-1]
                    rightnode = self.nodes[i][j+1]

                    if node.west==True and leftnode.east==True:
                        self.fillBlocksVertical(' ', i*3, j*3, 4)
                    elif node.west==False and node.east==False:
                        self.fillBlocksVertical('║', i*3, j*3, 4)
                    else:
                        raise ValueError('Board currupts')

                    if node.east==True and rightnode.west==True:
                        self.fillBlocksVertical(' ', i*3, j*3+3, 4)
                    elif node.east==False and rightnode.west==False:
                        self.fillBlocksVertical('║', i*3, j*3+3, 4)
                    else:
                        raise ValueError('Board currupts')
                        
    def updateCorners(self):
        for i in range(0,len(self.nodes)+1):
            for j in range(0,len(self.nodes[0])+1):

                if i==0:
                    N_block = ' '
                else:
                    N_block = self.grid[i*3-1][j*3]

                if i*3==len(self.grid)-1:
                    S_block = ' '
                else:
                    S_block = self.grid[i*3+1][j*3]

                if j==0:
                    W_block = ' '
                else:
                    W_block = self.grid[i*3][j*3-1]

                if j*3==len(self.grid[0])-1:
                    E_block = ' '
                else:
                    E_block = self.grid[i*3][j*3+1]
                    
                self.joinCornersAt(i*3,j*3, N_block, S_block, E_block, W_block)
                
    def joinCornersAt(self, row,col, N_block, S_block, E_block, W_block):
        if N_block=='║' and S_block=='║' and W_block=='═' and E_block=='═':
            self.grid[row][col] = '╬'
        elif N_block==' ' and S_block=='║' and W_block=='═' and E_block=='═':
            self.grid[row][col] = '╦'
        elif N_block=='║' and S_block==' ' and W_block=='═' and E_block=='═':
            self.grid[row][col] = '╩'
        elif N_block=='║' and S_block=='║' and W_block==' ' and E_block=='═':
            self.grid[row][col] = '╠'
        elif N_block=='║' and S_block=='║' and W_block=='═' and E_block==' ':
            self.grid[row][col] = '╣'
        elif N_block==' ' and S_block==' ' and W_block=='═' and E_block=='═':
            self.grid[row][col] = '═'
        elif N_block=='║' and S_block=='║' and W_block==' ' and E_block==' ':
            self.grid[row][col] = '║'
        elif N_block==' ' and S_block=='║' and W_block=='═' and E_block==' ':
            self.grid[row][col] = '╗'
        elif N_block==' ' and S_block=='║' and W_block==' ' and E_block=='═':
            self.grid[row][col] = '╔'
        elif N_block=='║' and S_block==' ' and W_block=='═' and E_block==' ':
            self.grid[row][col] = '╝'
        elif N_block=='║' and S_block==' ' and W_block==' ' and E_block=='═':
            self.grid[row][col] = '╚'
        elif N_block=='║' and S_block==' ' and W_block==' ' and E_block==' ':
            self.grid[row][col] = '║'
        elif N_block==' ' and S_block=='║' and W_block==' ' and E_block==' ':
            self.grid[row][col] = '║'
        elif N_block==' ' and S_block==' ' and W_block=='═' and E_block==' ':
            self.grid[row][col] = '═'
        elif N_block==' ' and S_block==' ' and W_block==' ' and E_block=='═':
            self.grid[row][col] = '═'
        else:
            self.grid[row][col] = ' '
            
    def drawGrid(self):
        for row in self.grid:
            line = ""
            for block in row:
                line += block
            print(line)
            
    def exportGridToArray(self):
        array = []
        for row in self.nodes:
            row_array = []
            for node in row:
                row_array.append(node.type)
            array.append(row_array)
        return array
    
    def importArrayToGrid(self, array):
        self.nodes = []
        for row in array:
            row_nodes = []
            for node in row:
                row_nodes.append(Node(node))
            self.nodes.append(row_nodes)
            
        self.grid = [[' ' for i in range(0,len(self.nodes[0])*3+1)] for j in range(0,len(self.nodes)*3+1)]
        self.updateGrid()
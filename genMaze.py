

def drawNode(north=False, south=False, east=False, west=False):
    if north:
        top_wall = "┌──┐"
    else:
        top_wall = "┌  ┐"
    
    side_wall = ""
    if west:
        side_wall += "│"
    else:
        side_wall += " "
    side_wall += "  "
    if east:
        side_wall += "│"
    else:
        side_wall += " "

    if south:
        bottom_wall = "└──┘"
    else:
        bottom_wall = "└  ┘"

    print(top_wall)
    print(side_wall)
    print(bottom_wall)

drawNode(north=True,south=False,west=True,east=False)

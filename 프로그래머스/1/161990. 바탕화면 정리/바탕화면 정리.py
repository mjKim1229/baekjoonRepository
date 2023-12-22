def solution(wallpaper):
    row = len(wallpaper)
    column = len(wallpaper[0])
    minX, minY = (row-1,column-1)
    maxX, maxY = (0,0)
    for i in range(row): 
        for j in range(column): 
            if wallpaper[i][j] == "#":
                minX,maxX = min(minX,i), max(maxX,i)
                minY,maxY = min(minY,j), max(maxY,j)
    return [minX,minY,maxX+1,maxY+1]
                
                
    
        
    
import sys
import random

N=int(sys.argv[1])

neighbours={}

neighbours[(0,0)]=[(0,1),(1,0)]
neighbours[(0,N-1)]=[(0,N-2),(1,N-1)]
neighbours[(N-1,0)]=[(N-2,0),(N-1,1)]
neighbours[(N-1,N-1)]=[(N-1,N-2),(N-2,N-1)]

for j in range(1,N-1):
    neighbours[(0,j)]=[(0,j-1),(1,j),(0,j+1)]

for i in range(1,N-1):
    neighbours[(i,0)]=[(i+1,0),(i-1,0),(i,1)]
  
for j in range(1,N-1):
    neighbours[(N-1,j)]=[(N-1,j-1),(N-2,j),(N-1,j+1)]

for i in range(1,N-1):
    neighbours[(i,N-1)]=[(i+1,N-1),(i-1,N-1),(i,N-2)]    

for i in range(1,N-1):
    for j in range(1,N-1):
        neighbours[(i,j)]=[(i,j-1),(i-1,j),(i,j+1),(i+1,j)]


start_x=int(sys.argv[2])
start_y=int(sys.argv[3])
random.seed(sys.argv[4])
output_file=sys.argv[5]

visited=[[0 for i in range(N)] for i in range(N)]
      
path=[]
def DFS(start_x,start_y):
    visited[start_x][start_y]=True
    now=neighbours[(start_x,start_y)]
    random_neighbours = random.sample(now, len(now))
    for k in range(len(random_neighbours)):
        if not(visited[random_neighbours[k][0]][random_neighbours[k][1]]):
            path.append([ (start_x,start_y),(random_neighbours[k][0],random_neighbours[k][1]) ])
            DFS(int(random_neighbours[k][0]),int(random_neighbours[k][1]))          
                   
DFS(start_x,start_y)

file=open(sys.argv[5],'w')
for i in range(N*N-1):
    file.write(str(path[i][0])+','' ' +str(path[i][1]))
    file.write('\n')
file.close()

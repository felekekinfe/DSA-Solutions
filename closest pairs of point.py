def ecludian_distance(p1,p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
def closest_pair(points):
  min=float('inf')
  n=len(points)
  for i in range(n-1):
    for j in range(i+1,n):
        distance=ecludian_distance(points[i],points[j])
        if distance<min:
            min=distance
            x,y=i,j
    return x,
print(closest_pair([(3,4), (1,2),(2,3)]))
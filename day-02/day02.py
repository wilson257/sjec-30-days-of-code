def tri_angle(triangles):
    for i,triangle in enumerate(triangles):
        if i%3==0:
           print(min(triangle))
        elif i%3==1:
            print(sorted(triangle)[1])
        else:
            print(max(triangle))
triangles=[[12, 11, 17],
[3 ,4 ,6],
[114, 114, 211],
[12 ,16 ,25],
[555 ,999 ,445]]
tri_angle(triangles) 

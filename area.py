def area_of_circle(r):
    if r>0:
        return(3.14*r*r)
    else:
        return
r=eval('input("Enter the radius : ")')
area=area_of_circle(r)
print(area)
# import package
import turtle 

t1=turtle.Turtle()
t1.pensize(3)
turtle.bgcolor("Black")


# for default shape

color1=('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow')
n=50
m=100
for i in range(90):
    for i in range (len(color1)):
        t1.color(color1[i])
        t1.circle(m)
        t1.left(n)
    
  


 


 
 

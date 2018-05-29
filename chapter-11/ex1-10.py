#Question 1
"""What is the Python interpreter’s response to the following? >>> list(range(10, 0, -2))
The three arguments to the range function are start, stop, and step, respectively. In this
example, start is greater than stop. What happens if start < stop and step < 0? Write a
rule for the relationships among start, stop, and step."""

"""
[start+(1*step), start+(2*step), start+(3*step) ... ] until (n*step) = start 
where n is a whole number integer and n = |start - stop| / step
"""

#Question 2
"""Consider this fragment of code:
import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
Does this fragment create one or two turtle instances? Does setting the
color of alex also change the color of tess? Explain in detail."""

#This fragment of code will only produce one turtle because alex is tess. The
#variable tess was aliased and both names reference the same turtle. Changes to one
#will result in changes to another.



#Question 3


a = [1, 2, 3]
b = a[:]
b[0]= 5

#  before
#       a --> [1,2,3]
#       b --> [1,2,3]
#  after
#       a --> [1,2,3]
#       b --> [5,2,3]
#In this case, a is not an alias for b
#and changes to b do not affect that of a


#Question 4

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

#The result will be
#Test 1: False
#Test 2: True

# Although this and that are lists with identical elements, they are different ones
# since "this is that" is not true, it will print Test 1: False
#Only after they are made aliases in Line 4, will "this is that" be true and
#yield Test 2: True as an outcome after formatting the function




#Question 6

def scalar_mult(s,v):
    for i in range(len(v)):
        v[i] = v[i]*s
    return v

print(scalar_mult(5,[1,2]))
print(scalar_mult(3, [1, 0, -1]))


#Question 10

def replace(s, old, new):
    x = s.split(old)
    g = new
    new = g.join(x)
    return new

print(replace("Mississippi", "i", "I"))
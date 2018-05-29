#Question 1
def tuple((a,b), (c,d)):
    if (a*c) + (b*d) > 10:
        return "greater than 10"
    else:
        return "less than 10"

print(tuple[(1,4),(3,5)])

# No you cannot pass tuples as arguments of a function unless the arguments themself are a single tuple.
#You would need to assign a pair to a single argument within the function instead



#Question 2
#Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?

#A tuple is a generalization of a pair: it is simply a group of items stored in a single value


#Question 3
#Is a pair a kind of tuple, or is a tuple a kind of pair?

#A pair is a kind of tuple or rather two elements stored together
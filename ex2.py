def max_of_three(a, b, c):

    if a >= b and a >= c:
        print "%d is the largest number among the three." % a
    elif b >= a and b >= c:
        print "%d is the largest number among the three." % b
    elif c >= a and c >= b:
        print "%d is the largest number among the three." % c
    else:
        assert False, "Error in the if construct"
       
max_of_three(124, 78, 78)       

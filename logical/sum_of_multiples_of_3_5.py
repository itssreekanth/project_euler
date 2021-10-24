def multiples(n):
    upper_for_three = n//3
    upper_for_five = n//5
    upper_for_fifteen = n//15
    sum_of_three = 3*(upper_for_three*(upper_for_three+1)/2)
    sum_of_five = 5*(upper_for_five*(upper_for_five+1)/2)
    sum_of_fifteen = 15*(upper_for_fifteen*(upper_for_fifteen+1)/2)
    sum = sum_of_three+sum_of_five-sum_of_fifteen
    return sum
multiples(1000)

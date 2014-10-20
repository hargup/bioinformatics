# Author: Harsh Gupta
# Date: 18th August 2014
# Calculating expected offsprings http://rosalind.info/problems/iev/

expected_dominant_offsprings = {1: 2,
                                2: 2,
                                3: 2,
                                4: 1.5,
                                5: 1,
                                6: 0}

number_of_each_type = [int(x) for x in input().split(' ')]
expected_dominant_offsprings = sum([n*expected_dominant_offsprings[i] for n, i in zip(number_of_each_type, range(1, 7))])
print(expected_dominant_offsprings)

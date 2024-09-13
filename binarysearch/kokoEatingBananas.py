'''
https://leetcode.com/problems/koko-eating-bananas/description/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

e.g. 

[3,6,7,11]
h = 8

ans = 4

soln:
the eating rate k can range anywhere from 1 to max(piles)

[1,2,3,4,5,6,7,8,9,10,11]a

do binary search on the list of possible eating rates

run simulation on the mid point where mid point = testing rate
if simulation passes: right = mid - 1
else: left = mid + 1





'''

import math

def minEatingSpeed(piles, h):


    finalRate = float('inf')

    left = 1
    right = max(piles)
    while left <= right:
        testingRate = (left + right) // 2

        


        hoursSpentInSimulation = simulate(piles, testingRate)
        if hoursSpentInSimulation <= h:
            # update and cut the space
            finalRate = min(finalRate, testingRate)
            right = testingRate - 1
        else:
            left = testingRate + 1
    
    return finalRate

def simulate(piles, eatingRate):
    hoursSpentInSimulation = 0
    for pile in piles:
        hoursSpentInSimulation += math.ceil(pile/eatingRate)
    
    return hoursSpentInSimulation




piles = [1,4,3,2]
h = 9
print(minEatingSpeed(piles, h))

        
        

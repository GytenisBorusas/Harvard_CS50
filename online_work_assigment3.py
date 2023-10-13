"""

Prompt
You have a diamond shape platform crossing of 5 tiles. The coordinates of the tiles are (-1, 0), (0, -1), (0,0), (0,1), (1, 0). 
You start at coordinates (xs,ys) and keep moving randomly either left (i.e. x coordinate decrease by 1), right (i.e. x coordinate 
increases by 1), up (i.e. y coordinate decrease by 1) or down (i.e. y coordinate increases by 1). The direction of subsequent moves 
is independent. What is the probability that you reach coordinates (xe, ye) before falling off the platform? Write code to simulate 
this process and explain how your code works.


Constraints:
(xs, ys) in [(-1, 0), (0,-1), (0 , 1), (1, 0)]
(xe, ye) in [(-1, 0), (0,-1), (0 , 1), (1, 0)]
xs != xe or ys!=ye

for example:
input:
Line 1: xs ys xe ye

output:
Line 1: Probability to reach destination before falling off platform

Sample input
-1 0 0 0

Sample output:
0.25
"""






import random

# This function just picks a direction (up, down, left, right) and moves one step in that direction.
def random_move(x, y):
    direction = random.randint(1, 4)
    if direction == 1:  # Move up
        y = y + 1
    elif direction == 2:  # Move down
        y = y - 1
    elif direction == 3:  # Move left
        x = x - 1
    else:  # Move right
        x = x + 1
    return x, y


# This checks if our current position is off the platform.
def is_off_platform(x, y):
    # List of tiles where we can stand
    tiles = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
    if (x, y) in tiles:
        return False  # We are still on the platform
    else:
        return True  # We have moved off the platform


# This simulates moving from a starting position to an end position. 
# It returns True if we made it to the end and False if we fell off the platform.
def simulate_move(start_x, start_y, end_x, end_y):
    x = start_x
    y = start_y
    while True:
        x, y = random_move(x, y)
        
        if x == end_x and y == end_y:
            return True  # We reached the end point
        if is_off_platform(x, y):
            return False  # We fell off the platform

# Main part of the program
num_trials = 10000
success_count = 0

start_x, start_y, end_x, end_y = map(int, input().split())

for i in range(num_trials):
    if simulate_move(start_x, start_y, end_x, end_y):
        success_count = success_count + 1

probability = success_count / num_trials
print(probability)
    

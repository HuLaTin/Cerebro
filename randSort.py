rand = open(r'Data\rand') # open file
text = rand.read() # read in text

nums = text.split('\n') # split on 'new line' character
nums = [num for num in nums if num.strip()] # remove empty characters
nums =[int(num) for num in nums] # strings to ints

#len(nums)
numCopy = nums.copy() # make a copy just in case
done = False # set flag to break while loop
while True: # infinite while loop
    for i, j in enumerate(nums[:-1]): # enumerate list of ints
        num1 = nums[i] # set variable num1 int
        num2 = nums[i+1] # set variable num2 int

        if num1 > num2: #compare, greater than
            nums[i] = num2 # if greater than, we swap the elements in the list
            nums[i+1] = num1 # swap
            break # break the inner for loop

        if i == len(nums)-2: # need to remind myself why this works, but it does
            done = True # set flag as true
            break # break inner loop
    
    if done: # if flag == true
        break # break while loop

print(nums) # print sorted list to console
# save?
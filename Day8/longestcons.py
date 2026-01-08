testlist = [100,4,200,1,3,2]


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_consecutive_sequence = 0
    
    for num in num_set:
        #checking for consecutive sequence start
        if num - 1 not in num_set:
            current_num= num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_consecutive_sequence = max(longest_consecutive_sequence, current_streak)
    return longest_consecutive_sequence



print(longest_consecutive_sequence(testlist))
#print(longest_consecutive_sequence_alt(testlist))

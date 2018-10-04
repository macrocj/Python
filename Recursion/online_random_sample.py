#Author: JC
#Date: 7/26/2018
#Version: 1.0

import itertools, random
def online_random_sample(stream, k):
    # Store the first k elements.
    sampling_results = list(itertools.islice(stream,k))

    # Have read the first k elements
    num_seen_so_far = k
    for x in stream:
        #num_seen_so_far += 1
        # Generate a random number in [0, num_seen_so_far -1], and is this number
        # is in [0, k - 1], we replace that element from the sample with x.
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results

stream = [3,2,5,3,6,7,3,4,2,6,7,1,9]
print(online_random_sample(stream, 5))
#!/usr/bin/python
# Heaps 9.2: Find the most similar website
# Given a list of (websit, user) tupples that represents users visiting
# websites. Identify the top k pairs of websites with the greatest similarity.
import heapq
from collections import defaultdict

def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)
    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.heappush(pairs, (0, ('', '')))
    
    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[1] for pair in pairs]

if __name__ == "__main__":
    k = 1
    l = [('google.com', 1), ('google.com', 3), ('google.com', 5), ('pets.com', 1), ('pets.com', 2),
    ('yahoo.com', 6), ('yahoo.com', 2), ('yahoo.com', 3), ('yahoo.com', 4), ('yahoo.com', 5), 
    ('wikipedia.org', 4), ('wikipedia.org', 5), ('wikipedia.org', 6), ('wikipedia.org', 7), 
    ('bing.com', 1), ('bing.com', 3), ('bing.com', 5), ('bing.com', 6)]

    print(top_pairs(l, k))
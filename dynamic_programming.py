# Memoized Fibonacci
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 2 : f = 1
    else: f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f
# fib(k) only recurses the first time it's called, forall k
# memoized calls cost O(1)
# nonmemoized calls is n: fib(1), fib(2),...fib(n)
# nonrecursive work per call = O(1)
# => time = O(n)

# DP ~ recursion + memoization + guessing
# - memoize (remember) & reuse solutions to subproblems
# that help solve the problem
# => time = # of subproblems * time/subproblem
# => fib  = n * O(1)

# Bottom-up DP algorithm:
def fib_bottom_up(n):
    fib = {} 
    for k in range(1, n+1):
        if k <= 2: f = 1
        else: f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]

# topological sort of subproblem dependency dag
# can often save space

# Shortest paths: delta(s, v) forall v
# Guessing: don't know the answer? guess ... try all guesses
# & take best one

# subproblem dependencies should be acyclic

# Bellman-Ford // shortest path from one node to all the others in the graph
def bellman_ford(G, s):
    for u in G.vertices:
        dist(u) = inf
        prev(u) = nil

    dist(s) = 0
    for _ in range(G.number_of_vertices - 1):
        for edge in G.edges:
            update(e)

def update(edge):
    u, v = edge
    dist(v) = min(dist(v), dist(u) + edge.length)


# DP ~ shortest paths in problem recurrece DAG

# 5 'easy' steps to DP:
# 1. define subproblems           -> # subproblems
# 2. guess (part of solution)     -> # number of choices for the guess 
# 3. relate subproblem solutions  -> time/subproblem  
# 4.a recurse & memoize           -> check subproblem recurrence is acyclic
# 4.b build DP table bottom-up    .  has topological sort
# 5. solve original problem       ->  

# Text justification:
# split text into 'good' lines
# text = list of words
# badness(i, j)
# { "if don't fit" : inf,  * : (page width - total width)^3}
# use words [i: j] as lines

# ['hello', 'hi', ..., 'end']
# [1, 0, 1, 0, 0, ..., 1] 1 if starts a line 0 otherwise

# 1. subproblems: suffixes words [i:]
# -. # subproblems: n 
# 2. guess: where to start 2nd line 
# -. # choices <= n-1 = O(n) 
# 3. recurrence:  
# . DP(i) = min(DP(j) + badness(i, j) for j in range(i+1, n+1))
# . time/subprob = O(n)
# 4. Topological order: i = n, n-1, ... , 0 
# .  total time: O(n^2)
# 5. Orig. Problem:  DP(0)

# Parent pointers: remember which guess was best.
# parent[i] = argmin(...) = j value

# Perfect-information blackjack:
# 1. Subproblems: suffix ci: #subproblems = n
# 2. guess: how many hits? #choices <= n 
# 3. recurrence: BJ(i) = max(outcome in {-1, 0, 1} + BJ(j) for j in range(i+4, n), if valid)
# 4. 


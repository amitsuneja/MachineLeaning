# Heap queue (or heapq) in Python

# importing "heapq" to implement heap queue
import heapq as hq

# initializing list
mylist = [5, 7, 9, 1, 3]
hq.heapify(mylist)
print(mylist)           # [1, 3, 9, 7, 5]

# using heappush(heap, element) to push elements into heap
# pushes 4
hq.heappush(mylist, 4)
print(mylist)           # [1, 3, 4, 7, 5, 9]

# using heappop() to pop smallest element
hq.heappop(mylist)
print(mylist)           # [3, 5, 4, 7, 9]

hq.heappop(mylist)
print(mylist)           # [4, 5, 9, 7]

# heappushpop(heap, element)  his function combines the functioning of both push and pop operations in one statement,
# increasing efficiency. Heap order is maintained after this operation.
hq.heappushpop(mylist, 8)
print(mylist)           # [5, 7, 9, 8]

# heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from
# above function. In this, element is first popped, then element is pushed.i.e, the value larger than the pushed
# value can be return
hq.heapreplace(mylist, 11)
print(mylist)           # [7, 8, 9, 11]

#  nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable
# specified and satisfying the key if mentioned.

##################################################################################################################
# initializing list
mylist = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
hq.heapify(mylist)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(hq.nlargest(3, mylist))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(hq.nsmallest(3, mylist))

# merge(*iterables) : Merge multiple sorted inputs into a single sorted output (for example,
# merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

mylist_1 = [1, 2, 3, 4]
mylist_2 = [7, 8, 9, 10]
hq.heapify(mylist_1)
hq.heapify(mylist_2)
my_generator_obj = hq.merge(mylist_2, mylist_1)
print(list(my_generator_obj))
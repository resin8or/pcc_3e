motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# pop removes the last item in a list
popped_motorcycle = motorcycles.pop()
print(f"\nThe last motorcycle I sold was a {popped_motorcycle.title()}.")  

# pop can also be used to remove an item from any position in a list   
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# print the remaining motorcycles
print(motorcycles)

# remove an item by value
print("removing yamaha from the list...")
motorcycles.remove('yamaha')
print(motorcycles)

# insert an item into the list  
print("inserting honda and bugati into the list...")
motorcycles.insert(0, 'honda')
motorcycles.append('bugati')
print(motorcycles)

# sort the list
print("sorting the list...")
motorcycles.sort()
print(motorcycles)
print('reverse sorting the list...')
motorcycles.sort(reverse=True)
print(motorcycles)

# sort the list temporarily with sorted() and this does not affect the original list
print("sorting the list temporarily...")
print(sorted(motorcycles))
print(motorcycles)

# show the length of the list
print(f"The length of the list is {len(motorcycles)}")

# print the last item in the list
print(f"The last item in the list is {motorcycles[-1]}")




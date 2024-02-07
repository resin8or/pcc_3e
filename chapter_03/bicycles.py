bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
bicycles.sort()
print(bicycles)

# Print all items in the list that contain the letter 'c'
for bike in bicycles:
    if 'c' in bike:
        print(bike.title())


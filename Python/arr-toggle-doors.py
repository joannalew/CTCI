# CTCI 6.6 Brain Teasers

# There are one hundred closed lockers in a hallway 
# A man begins by opening all one hundred lockers 
# Next, he closes every second locker 
# Then he goes to every third locker and closes it if it is open 
#   or opens it if it is closed (e g , he toggles every third locker) 
# After his one hundredth pass in the hallway, 
#   in which he toggles only locker number one hundred, 
#   how many lockers are open?

def toggle_doors():
    arr = [True] * 101
    for i in range(2, 101):
        for j in range(i, 101, i):
            arr[j] = not arr[j]
    
    count = 0
    for i in range(1, 101):
        if arr[i]:
            count += 1
    
    return count

def main():
    print(toggle_doors())

if __name__ == "__main__":
    main()

        
print("=" * 50)
print("This program will print your message 100 times.")
print("=" * 50)
a = 1
b = 2
c = 3
message = input("Enter a message to print 100 times: ")
choice = input("Choose an option (1, 2, or 3): ")

if choice == "1":
    print((message + "\n") * 100)
elif choice == "2":
    print(message * 100)
else:
    print((message + " ") * 100)
import hash

message = input("Enter message: ")

print("\nHash: {}".format(hash.textToSha256(message)))

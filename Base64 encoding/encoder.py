import base64

path = input("Enter the full file path: ")

with open(path, "rb") as f:
    # read the contents of the file as bytes
    file_bytes = f.read()

# encode the file contents into base64
base64_bytes = base64.b64encode(file_bytes)

# convert the base64 bytes to a string
base64_string = base64_bytes.decode('utf-8')

print(base64_string)

with open("output.txt", "wb") as f:
    f.write(base64_string.encode('utf-8'))

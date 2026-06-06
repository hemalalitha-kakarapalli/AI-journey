filename = input().lower().strip()
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg"):
    print("image/jpeg")
elif filename.endswith(".jpeg"):
    print("image/jpeg")
else:
    print("application/octet-stream")


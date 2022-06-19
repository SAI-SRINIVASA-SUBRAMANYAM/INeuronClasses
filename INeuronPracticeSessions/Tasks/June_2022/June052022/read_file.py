# Try to write a funtion whicsh can perform a read operation from .txt file
with open("message.txt") as f:
    lines = [l.rstrip() for l in f.readlines()]
    print(lines)
    f.close()
import sys
import os

print("Hello, World !!!")

for i, a in enumerate(sys.argv):
    print(f"argv[{i}] = {a}")

sys.exit(os.EX_OK if len(sys.argv) <= 1 else os.EX_USAGE)

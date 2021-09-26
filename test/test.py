import sys
sys.path.append('../src')
from main import main

n = int(input("Input N: "))
response = main(n)
for i in response:
  print(i)
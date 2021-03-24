import sys

class Calculator:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def multiply(self):
      return self.a * self.b

def main():

  if len(sys.argv) == 3:  
    a = int(sys.argv[1])    
    b = int(sys.argv[2])    
    calc = Calculator(a, b)

    r = calc.multiply()
    print(r)
  else:
    print("Supply exaclty 2 arguments")
    sys.exit(1)

if __name__ == '__main__':
  main()
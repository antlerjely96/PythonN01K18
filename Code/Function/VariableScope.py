# Biến toàn cục
a = 5

def function1():
    # Biến cục bộ của function1
    a = 6;
    print("------------------------")
    print("function 1")
    print(f"a = {a}")
    
def function2():
    global a
    a = 8
    print("------------------------")
    print("function 2")
    print(f"a = {a}")
    
def main():
    function1()
    function2()
    print("------------------------")
    print("main")
    print(f"a = {a}")

if __name__ == "__main__":
    main()
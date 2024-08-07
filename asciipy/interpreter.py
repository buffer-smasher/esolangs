import sys

def main():
    if (len(sys.argv) > 0):
        if (sys.argv[1].endswith(".asciipy")):
            pass
        else:
            print("File does not end in .asciipy")
            return
    else:
        print("Please pass file path argument")
        return
    
    program = ""
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            for ascii in line.split(" "):
                program += chr(int(ascii))
    
    exec(program)


if __name__ == '__main__':
    main()
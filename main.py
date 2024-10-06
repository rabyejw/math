import sys
import tkinter as tk

def main():
    questionType = input("(0-?) What question type?: ") # input() returns a string

    if(questionType == "0"):
        print("Exiting program")
        sys.exit(0)

    print(f"You asked for question type: {questionType}")










































if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
A simple greeting program
"""

def greet(name):
    """Return a personalized greeting"""
    return f"Hello, {name}! Welcome to GitHub!"

def main():
    print("=== GitHub Greeting Program ===")
    user_name = input("What's your name? ")
    
    if user_name:
        print(greet(user_name))
        print(f"\nNice to meet you, {user_name}!")
    else:
        print("Hello, mysterious stranger!")

if __name__ == "__main__":
    main()
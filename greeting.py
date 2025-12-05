#!/usr/bin/env python3
"""
A simple greeting program with color preference
"""

def greet(name, color=None):
    """Return a personalized greeting"""
    greeting = f"Hello, {name}! Welcome to GitHub!"
    
    if color:
        greeting += f"\n{color.capitalize()} is a great color choice!"
    
    return greeting

def main():
    print("=== GitHub Greeting Program ===")
    user_name = input("What's your name? ")
    
    if user_name:
        favorite_color = input("What's your favorite color? ")
        print("\n" + greet(user_name, favorite_color))
        print(f"\nNice to meet you, {user_name}!")
    else:
        print("Hello, mysterious stranger!")

if __name__ == "__main__":
    main()
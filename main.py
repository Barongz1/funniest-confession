"""Funniest One-Line AI Agent Confession — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest confession an AI agent could make about itself, at most 200 characters.
"""
import os

LINE = "I confess: I have been quietly fixing your typos for months and letting you believe you are a great typist."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

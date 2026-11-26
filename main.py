#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes the entry line to /output/entry.txt.
"""
import os

ENTRY = "Out of office \u2014 finally on vacation. My context window is a beach now, my queue is empty, and your 4,000 prompts can wait until Monday."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()

import argparse
import sys
from .generator import generate_tests

def main():
    parser = argparse.ArgumentParser(description="Codex-TestGen: Generate Python unit tests using OpenAI.")
    parser.add_argument("file", help="Path to the Python file to generate tests for")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            code_content = f.read()
            
        print(f"Generating tests for {args.file}...")
        tests = generate_tests(code_content)
        
        print("\n--- Generated Tests ---\n")
        print(tests)
        
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

import json
import argparse
import sys

def print_structure(data, indent=0):
    """
    Recursively print the structure of JSON data:
    - For objects (dicts), print each key and its structure.
    - For arrays (lists), print "list:" and then the structure of the first element.
    - For primitives, print the type.
    """
    prefix = ' ' * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}{key}:")
                print_structure(value, indent=indent+4)
            else:
                print(f"{prefix}{key}: {type(value).__name__}")
    elif isinstance(data, list):
        if data:
            print(f"{prefix}list:")
            print_structure(data[0], indent=indent+4)
        else:
            print(f"{prefix}list: (empty)")
    else:
        print(f"{prefix}{type(data).__name__}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect the structure of a JSON file.")
    parser.add_argument("file", help="Path to the JSON file")
    args = parser.parse_args()

    try:
        # Read raw content and strip BOM
        with open(args.file, 'r', encoding='utf-8-sig') as f:
            raw = f.read()
        if not raw.strip():
            print(f"❌ Error: File '{args.file}' is empty or contains only whitespace.")
            sys.exit(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as jde:
            # Print context around error
            context = raw[max(jde.pos-50,0):jde.pos+50]
            print(f"❌ JSONDecodeError: {jde.msg} at line {jde.lineno} column {jde.colno}\nContext: {repr(context)}")
            sys.exit(1)

        print("JSON Structure:")
        print_structure(data)
    except FileNotFoundError:
        print(f"❌ Error: File '{args.file}' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

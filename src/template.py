def part1(data):
    result = 0
    
    for line in data:
        line = line.strip()
        if not line:
            continue
        
        # TODO....

    return result

def part2(data):
    result = 0
    
    for line in data:
        line = line.strip()
        if not line:
            continue 

        # TODO....

    return result

def get_input(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        return []

def main():
    INPUT_FILE = "../input/dayX.txt"
    
    input_data = get_input(INPUT_FILE)
    
    if not input_data:
        return

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
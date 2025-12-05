def part1(data):
    result = 0
    index = 50
    
    for line in data:
        line = line.strip()
        if not line:
            continue
        
        if line[0] == 'L':
            index -= int(line[1:])
        else:
            index += int(line[1:])
        
        if range(100)[index % 100] == 0:
            result += 1

    return result

def part2(data):
    result = 0
    index = 50
    lock = range(100)
    
    for line in data:
        line = line.strip()
        if not line:
            continue
        
        if line[0] == 'L':
            num = int(line[1:])
            if lock[index % 100] == 0 and lock[index % 100] < num:
                result -= 1
            while lock[index % 100] < num:
                result += 1
                num -= 100

            index -= int(line[1:])
        else:
            num = int(line[1:])
            while (100 - lock[index % 100]) < num:
                result += 1
                num -= 100

            index += int(line[1:])
        
        if lock[index % 100] == 0:
            result += 1

    return result

def get_input(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        return []

def main():
    INPUT_FILE = "../input/day1.txt"
    
    input_data = get_input(INPUT_FILE)
    
    if not input_data:
        return

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
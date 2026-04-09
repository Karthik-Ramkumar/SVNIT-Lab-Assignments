districts = [
    "Kachchh", "Banaskantha", "Patan", "Mehsana", "Sabarkantha",
    "Gandhinagar", "Ahmedabad", "Surendranagar", "Rajkot", "Jamnagar",
    "Porbandar", "Junagadh", "Amreli", "Bhavnagar", "Anand",
    "Kheda", "Panchmahal", "Dahod", "Vadodara", "Bharuch",
    "Narmada", "Surat", "Navsari", "Valsad", "Dangs"
]

neighbors = {
    "Kachchh": ["Banaskantha", "Surendranagar", "Jamnagar"],

    "Banaskantha": ["Kachchh", "Patan", "Mehsana", "Sabarkantha"],

    "Patan": ["Banaskantha", "Mehsana", "Surendranagar"],

    "Mehsana": ["Banaskantha", "Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad"],

    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Kheda", "Panchmahal"],

    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],

    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Bhavnagar", "Surendranagar"],

    "Surendranagar": ["Kachchh", "Patan", "Ahmedabad", "Rajkot", "Bhavnagar"],

    "Rajkot": ["Surendranagar", "Jamnagar", "Porbandar", "Junagadh", "Amreli"],

    "Jamnagar": ["Kachchh", "Rajkot", "Porbandar"],

    "Porbandar": ["Jamnagar", "Rajkot", "Junagadh"],

    "Junagadh": ["Porbandar", "Rajkot", "Amreli"],

    "Amreli": ["Rajkot", "Junagadh", "Bhavnagar"],

    "Bhavnagar": ["Amreli", "Ahmedabad", "Anand", "Bharuch", "Surendranagar"],

    "Anand": ["Ahmedabad", "Kheda", "Vadodara", "Bharuch", "Bhavnagar"],

    "Kheda": ["Gandhinagar", "Sabarkantha", "Ahmedabad", "Anand", "Vadodara", "Panchmahal"],

    "Panchmahal": ["Sabarkantha", "Kheda", "Vadodara", "Dahod"],

    "Dahod": ["Panchmahal", "Vadodara"],

    "Vadodara": ["Kheda", "Anand", "Panchmahal", "Dahod", "Bharuch", "Narmada"],

    "Bharuch": ["Bhavnagar", "Anand", "Vadodara", "Narmada", "Surat"],

    "Narmada": ["Vadodara", "Bharuch", "Surat", "Dangs"],

    "Surat": ["Bharuch", "Narmada", "Navsari", "Dangs"],

    "Navsari": ["Surat", "Valsad", "Dangs"],

    "Valsad": ["Navsari", "Dangs"],

    "Dangs": ["Narmada", "Surat", "Navsari", "Valsad"]
}

def is_safe(district, color, assignment): # checks to see if i colour this place will it clash with neighbouring colours?
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def choose_next(assignment):
    # we are picking neighbour with most neighbours first
    unassigned = [d for d in districts if d not in assignment]
    unassigned.sort(key=lambda d: len(neighbors[d]), reverse=True)
    return unassigned[0] if unassigned else None

def backtrack_algo(colors, assignment):
    if len(assignment) == len(districts):
        return True

    district = choose_next(assignment)

    for color in colors:
        if is_safe(district, color, assignment):
            assignment[district] = color

            if backtrack_algo(colors, assignment):
                return True

            del assignment[district]   # backtracking

    return False

def min_colours_needed():
    color_names = ["Red", "Green", "Blue", "Yellow"] # for maps max is only 4 colors

    for num_colors in range(1, 5):
        colors = color_names[:num_colors]
        assignment = {}

        if backtrack_algo(colors, assignment):
            return num_colors, assignment

    return None, None

def main():
    min_colors, solution = min_colours_needed()

    if solution is None:
        print("No solution found.")
        return

    print("minimum num of colors needed:", min_colors)
    print("\nDistrict -> Color")
    for district in districts:
        print(f"{district:15} -> {solution[district]}")

if __name__ == "__main__":
    main()
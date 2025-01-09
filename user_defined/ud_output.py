def print_dict_raw(d):
    print(d)

def print_dict_simple(d):
    for key, value in d.items():
        print(f"{key} depth-{value}")

def print_dict_sorted_keys(d):
    for key in sorted(d.keys()):
        print(f"{key} depth-{d[key]}")

def print_dict_sorted_values(d):
    for key, value in sorted(d.items(), key=lambda item: item[1]):
        print(f"{key} depth-{value}")

# Example usage
if __name__ == "__main__":
    sample_dict = {'94': 2, '68': 3, '10': 1}
    
    print("Simple raw:")
    print_dict_raw(sample_dict)

    print("\nSimple print:")
    print_dict_simple(sample_dict)
    
    print("\nSorted by keys:")
    print_dict_sorted_keys(sample_dict)
    
    print("\nSorted by values:")
    print_dict_sorted_values(sample_dict)
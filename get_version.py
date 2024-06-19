def get_version():
    with open('version.txt', 'r') as file:
        version = file.read().strip()
    return version

if __name__ == "__main__":
    print(get_version())

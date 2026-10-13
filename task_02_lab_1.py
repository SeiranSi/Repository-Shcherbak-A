import hashlib

def generate_file_hashes(*file_paths):
    hashes_dict = {}
    for file_path in file_paths:
        try:
            with open(file_path, "rb") as file:
                sha256 = hashlib.sha256()

                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    sha256.update(data)

                hashes_dict[file_path] = sha256.hexdigest()

        except FileNotFoundError:
            print("File not found:", file_path)
        except IOError:
            print("IO error:", file_path)
    return hashes_dict

#example
result = generate_file_hashes("apache_logs.txt", "new_file.txt", "not_found_file.txt", "not_file")
print(result)
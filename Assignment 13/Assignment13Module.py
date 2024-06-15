import os
import hashlib
from datetime import datetime

total_files_scanned = 0
total_duplicate_files = 0

def find_duplicate_files(directory):
    global total_files_scanned, total_duplicate_files
    duplicates = []
    checksums = {}
    for root, _, files in os.walk(directory):
        for file in files:
            total_files_scanned += 1
            path = os.path.join(root, file)
            checksum = hash_file(path)
            if checksum in checksums:
                duplicates.append([checksums[checksum], path])
                total_duplicate_files += 1
            else:
                checksums[checksum] = path
    return duplicates

def hash_file(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def create_marvelous_directory():
    marvelous_dir = os.path.join(os.getcwd(), "Marvelous")
    try:
        if not os.path.exists(marvelous_dir):
            os.makedirs(marvelous_dir)
            print("Marvelous directory created successfully.")
        else:
            print("Marvelous directory already exists.")
    except Exception as e:
        print(f"Error creating Marvelous directory: {e}")
    return marvelous_dir


def create_log_file(directory):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(directory, f"log_{timestamp}.txt")
    #return open(log_file, "w+")
    return log_file
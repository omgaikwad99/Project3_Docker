import os
import socket
from collections import Counter

# Ensure that the output directory exists
output_dir = '/home/output/'
os.makedirs(output_dir, exist_ok=True)

# List all text files in the directory
files = [f for f in os.listdir() if f.endswith('.txt')]
print("List of text files:", files)

# Read the text files and count words
word_counts = {}
grand_total = 0
for file in files:
    with open(file, 'r') as f:
        words = f.read().split()
        word_counts[file] = len(words)
        grand_total += len(words)

        # Find top 3 words in IF.txt
        if file == 'IF.txt':
            top_words = Counter(words).most_common(3)
            print("Top 3 words in IF.txt:", top_words)

# Find the IP address of the machine
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("IP Address:", ip_address)

# Write output to result.txt
result_file_path = os.path.join(output_dir, 'result.txt')
try:
    with open(result_file_path, 'w') as result_file:
        result_file.write(f"Grand total number of words: {grand_total}\n")
        result_file.write("Top 3 words in IF.txt:\n")
        for word, count in top_words:
            result_file.write(f"{word}: {count}\n")
        result_file.write(f"IP Address: {ip_address}\n")
    print("Output written to:", result_file_path)
except Exception as e:
    print("Error writing output:", e)

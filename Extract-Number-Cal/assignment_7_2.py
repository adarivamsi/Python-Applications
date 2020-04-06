# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    values = line.find("0")
    number = float(line[values:])
    total = total + number
    avg = total / count

print("Average spam confidence:", avg)

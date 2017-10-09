import sys

def main(fin, fout_name):
    lines = [x.strip() for x in open(fin).readlines()]
    index = 0
    key = ""
    value = ""
    entries = list()
    while index < len(lines):
        line = lines[index]
        start = line.find('{')
        if start != -1:
            key = line.split(' ')[0]
        is_value = line.find("unitDescriptor=")
        if is_value != -1:
            value = line.split"\"")[1]
            entries.append("%s,%s\n" % (key, value))
        index += 1
    answer = "".join(entries)
    with open(fout_name, 'w') as fout:
        fout.write(answer)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

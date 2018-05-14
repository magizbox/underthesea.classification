f = open("topic_classifier_ver1.0.txt")
for i, line in enumerate(f):
    x = line.find(" ")
    label = line[:x]
    text = line[x+1:]
    if len(text) < 3:
        print(i, ",", text)
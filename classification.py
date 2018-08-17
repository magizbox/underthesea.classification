import argparse

from models.fasttext.model_fasttext import classify

parser = argparse.ArgumentParser("classification.py")
text_group = parser.add_argument_group("The following arguments are mandatory for text option")
text_group.add_argument("text", metavar="TEXT", help="text to predict", nargs="?")
file_group = parser.add_argument_group("The following arguments are mandatory for file option")
file_group.add_argument("--fin", help="text file input")
file_group.add_argument("--fout", help="file output")
args = parser.parse_args()
if not (args.text or args.fin):
    parser.print_help()

if args.text:
    text = args.text
    label = classify(text)[0]
    print(label)

if args.fin:
    if not (args.fin and args.fout):
        parser.error("File option requires --fin and --fout")
    fin = args.fin
    fout = args.fout
    lines = open(fin).read().splitlines()
    open(fout, "w").write("")
    f = open(fout, "a")
    for line in lines:
        label = classify(line)[0]
        print(label)
        text = "{},{}\n".format(label, line)
        f.write(text)

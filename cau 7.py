print("Nguyen Van Thai","\nMSSV: 235752021610005")
def doc_file(fname):
    with open(fname,'r') as file:
        lines=file.readlines()
        return len(lines)
fname='vd.txt'
print("So dong trong tep la: ", doc_file(fname))

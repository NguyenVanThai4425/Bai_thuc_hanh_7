print("Nguyen Van Thai","\nMSSV: 235752021610005")
def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("Python Execises\n")
        myfile.write("Java Excercises")
    txt=open(fname)
    print(txt.read())
file_read('C:/Users/DELL Inc/OneDrive - vinhuni.edu.vn/Tài liệu/vd.txt')

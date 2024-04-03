# Advantage of using context manager in file is, we do not need to explicitly close the file
# the file closes itself while the context manager block ends


filename = "test1.txt"

with open(filename, "w") as fp:  # context manager
    fp.write("Writing in file using context manager")



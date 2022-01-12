def file_attr(fname):                    # takes filename as attribute
    with open(fname, 'w') as newfile:       # fname as first attribute and in write mode
        newfile.write("Hey this is PFSD assingment")     # write the contents to file
        newfile.write("This is a new file")             # another content
    s = open(fname)                           # opening file name for terminal
    print(s.read())                            # reading the contents from that file and displaying it


file_attr('PFSDf1.txt')                  # passing filename

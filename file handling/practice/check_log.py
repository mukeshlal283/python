
# check is python is present log.txt or not
# even if it upper or lower

with open("log.txt") as f:
    con = f.read().lower()      #f.read().lower()
                                        #or
if 'python' in con.lower():           # convert to lower
    print("yes it present")
else:
    print("no present")


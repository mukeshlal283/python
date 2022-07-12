def strip_and_replace(statement, word):
    
    see = statement.strip()
    return see.replace(word, "")

str = "   this is mukesh   "    

print(strip_and_replace(str, "mukesh"))


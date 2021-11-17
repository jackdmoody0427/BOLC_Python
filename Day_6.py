'''
Day 6 Activities
'''

'''
def PyAct 18-1():
    def tough_read(fname):

    Sometimes my cousin is just mean. He sent me a file with a special message 
    but made it into a crazy series of ones and zeros. He told me each letter 
    was on its own line and could be converted into an ASCII character, 
    whatever that means. Can you help me by decoding his message?
    Args:
        fname (str): path to a file where the input is located
    Returns:
        str: Sentence that was decoded
    pass 
'''
def tough_read(fname):
    cont = []
    with open(fname) as f1:
        lines = [line.strip() for line in f1.readlines()]
        for i in lines:
            cont.append(chr(int(i,2)))
        x = ''.join(cont)
        print(x)
#tough_read("orphan.txt")

'''
def PyAct 18-2():
    def log_to_file(fname, theme):
    You have a artist friend that likes to jot down some inspirational words
    when the mood strikes. These fits of inspiration always have a theme that
    he needs to remember with the messages. Your friend needs some help
    keeping track. 
    
    Read each of the inspirational messages from the user and
    write them to the end of the file specified by fname. 
    
    Since the theme is
    important and must be remembered, add the theme and a colon before each
    message and ensure each inspirational message is on its own line. 
    
    An empty
    input will indicate no more entries and the end of the theme.
    Args:
        fname (str): Path to an existing file that includes previous
                     inspirational messages to keep.
        theme (str): Theme to be placed on each line.
    Returns:
        None
'''
def log_to_file(fname, theme):
    inp = input("put in your word: ")
    lst = []
    while inp != '':
        lst.append(inp)
        inp = input("put in your word: ")
    f = open(fname, 'a')
    for i in lst:
        f.write("{}:{}\n".format(theme, i))

#log_to_file("orphan.txt", "love")

'''
def PyAct 18-3():
    def replace_in_file(in_path, out_path, reps):

    Replace all found instances of the individual entries in the file
    found at in_path. 

    Replacements will be in the list reps as a list of
    tuples. 

        Each tuple entry will contain the 'find' as the first element and
        the 'replace' will be the second element. 

    Write the result to the file
    specified with out_path.
    Args:
        in_path (str): input file path
        out_path (str): output file path
        reps (list): list of tuples containing ('find', 'replace') mappings
    Returns:
        None
'''

def repl(input_s, to_find, replace_with):
    # find 'to_find' inside of 'input_s'
    # replace 'to_find' at that position with 'replace_with'
    location = input_s.find(to_find)
    while location > -1:
        input_s = input_s[:location] + replace_with + input_s[location+len(to_find):]
        location = input_s.find(to_find)
    return input_s

def replace_in_file(in_path, out_path,reps):
    with open(in_path) as f1:
        inps= f1.read()
    
    for to_find, replace_with in reps:
        inps = repl(inps, to_find, replace_with)

    with open(out_path, 'w') as f:
        f.write(inps)

    
replace_in_file("input.txt","out2.txt", [('world', 'class'),("won", "one"),("to","two"),('tree',"three")])
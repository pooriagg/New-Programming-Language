import time

#######################################
TOKENS = {
    "if": "IF",
    "num": "NUMBER",
    "for": "FOR",
    ".": "DOT",
    "#": "SHARP",
    "$": "CALL_ID",
    "&": "AND",
    "while": "WHILE",
    "function": "FUNCTION",
    "@": "CALL_FUNC",
    "id": "ID",
    "$id": "CALL_ID",
    "add": "ADD",
    "mul": "MUL",
    "sub": "SUB",
    "div": "DIV",
    "space": "SPACE",
    "comment": "COMMENT",
    "in": "IN",
    "range": "RANGE",
    "set": "SET",
    "aqulad_close": "AQULAD_CLOSE",
    "aqulad_open": "AQULAD_OPEN",
    "parantes_close": "PARANTES_CLOSE",
    "parantes_open": "PARANTES_OPEN",
    "eq": "EQUAL",
    "lt": "LITTLE_THAN",
    "gt": "GRATER_THAN",
    ";": "SEMI",
    "str": "STRING",
    "desc": "DESCRIPTION",
    ",": "VA"
}
#######################################

# get the compile time
beforeTime = time.time()

# compile phase 1 #

filePatch = input("Please enter your file path: ")

file = open(filePatch, "r")

print("\n***********************\n*** Compile results ***\n***********************\n")

# metrics
isThereError = False
countTotal = 1
countKey = 0
countId = 0
countFailed = 0

# will create a result file after compile
resultFile = open("Result.txt", "w")

content = file.readlines()

# trim the content
for j in range(len(content)):
    content[j] = content[j].strip()

for k in range(len(content)):

    data = content[k].split(" ")

    for i in data:
        lexem = i.strip()
        if (lexem == "eq"):
            token = TOKENS["eq"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('eq' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "lt"):
            token = TOKENS["lt"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('lt' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem.isnumeric()):
            token = TOKENS["num"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. (number)".format(lexem))
            print("--------------------------------------------------------")    
        elif (lexem == "gt"):
            token = TOKENS["gt"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('gt' key-word)".format(lexem))
            print("--------------------------------------------------------")        
        elif (lexem == "&if"):
            token = TOKENS["if"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('if' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "range"):
            token = TOKENS["range"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('range' key-word)".format(lexem))
            print("--------------------------------------------------------")    
        elif (lexem == "&for"):
            token = TOKENS["for"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('for' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "&while"):
            token = TOKENS["while"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('while' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "func"):
            token = TOKENS["function"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('func' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "add"):
            token = TOKENS["add"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('add' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "sub"):
            token = TOKENS["sub"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('sub' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "mul"):
            token = TOKENS["mul"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('mul' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "div"):
            token = TOKENS["div"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('div' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "set"):
            token = TOKENS["set"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('set' key-word)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "$"):
            token = TOKENS["$"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. (calling an id)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "@"):
            token = TOKENS["@"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. (calling a function)".format(lexem))
            print("--------------------------------------------------------")    
        elif (len(data) == 1 and data[0] == "\n"):
            token = TOKENS["space"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. (empty)".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "{"):
            token = TOKENS["aqulad_open"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {\n-Status: valid. ( '{' )")
            print("--------------------------------------------------------")   
        elif (lexem == "}"):
            token = TOKENS["aqulad_close"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> }\n-Status: valid. ( '}' )")
            print("--------------------------------------------------------")  
        elif (lexem == "("):
            token = TOKENS["parantes_open"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: valid. ( '(' )".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == ")"):
            token = TOKENS["parantes_close"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: valid. ( ')' )".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == ","):
            token = TOKENS[","]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: valid. ( ',' )".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "#"):
            token = TOKENS["#"]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: valid. ( comment )".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "."):
            token = TOKENS["."]
            resultFile.write(f"{token}\n")
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: valid. ( '.' )".format(lexem))
            print("--------------------------------------------------------")
        elif (lexem == "in"):
            token = TOKENS["in"]
            resultFile.write(f"{token}\n")
            countKey += 1
            print("--------------------------------------------------------")
            print(f"{countTotal})")
            print("-> {}\n-Status: Accepted. ('in' key-word)".format(lexem))
            print("--------------------------------------------------------") 
        else:
            original = lexem
            lexem += "/"
            lexem2 = list(lexem)

            countId += 1

            isFirst = False
            isNonFirst = False
            isAllInvalid = True

            state = 1

            for char in lexem2:
                match state:
                    case 1:
                        if ((char >= "a" and  char <= "z") or (char >= "A" and char <= "Z")):
                            state = 2
                        else:
                            isFirst = True
                    case 2:
                        isAllInvalid = False
                        if (char == "/"):
                            if (isFirst == False and isNonFirst == False):
                                token = TOKENS["id"]
                                resultFile.write(f"{token}\n")
                                print("--------------------------------------------------------")
                                print(f"{countTotal})")
                                print("-> {}\n-Status: Accepted. (ID)".format(original))
                                print("--------------------------------------------------------")
                            elif(isFirst == True and isNonFirst == True):
                                countFailed += 1
                                print("--------------------------------------------------------")
                                print(f"{countTotal})")
                                print("-> {}\n-Status: Not accepted. (ID)\n(reason => only you can start id with a-z A-Z AND you cannot use special charaters in your id)".format(original))
                                print("--------------------------------------------------------")
                                isThereError = True
                            elif(isFirst):
                                countFailed += 1
                                print("--------------------------------------------------------")
                                print(f"{countTotal})")
                                print("-> {}\n-Status: Not accepted. (ID)\n(reason => only you can start id with a-z A-Z)".format(original))    
                                print("--------------------------------------------------------")
                                isThereError = True
                            elif(isNonFirst):
                                countFailed += 1
                                print("--------------------------------------------------------")
                                print(f"{countTotal})")
                                print("-> {}\n-Status: Not accepted. (ID)\n(reason => you cannot use special characters while defining your id)".format(original))         
                                print("--------------------------------------------------------")
                                isThereError = True
                            elif ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z") or (char >= "0" and char <= "9")):
                                state = 2
                            else:
                                countFailed += 1
                                isThereError = True      
        countTotal += 1                                                
resultFile.close()

# compile phase 2 #

result = open("./Result.txt", "r")

# check the existince of error
isAllConfirmed = True

content = result.readlines()

# trim the content
for j in range(len(content)):
    content[j] = content[j].strip()

# keep track of current token
index = 0
if (len(content) > 0):
    lookahead = content[index]
else:
    lookahead = ""

def match(key, value):
    global index
    global lookahead
    global isAllConfirmed

    if (key == value and index < len(content)):
        if (index + 1 < len(content)):
            index += 1

        lookahead = content[index]

        return True
    else:
        isAllConfirmed = False
        return False

def Syntax():
    if (lookahead == "IF"):
        match(TOKENS["if"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        Condition()
        match(TOKENS["parantes_close"], lookahead)
        match(TOKENS["aqulad_open"], lookahead)
        Body()
        match(TOKENS["aqulad_close"], lookahead)
    elif (lookahead == "FOR"):
        match(TOKENS["for"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["in"], lookahead)
        match(TOKENS["range"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["num"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
        match(TOKENS["aqulad_open"], lookahead)
        Body()
        match(TOKENS["aqulad_close"], lookahead)
    elif (lookahead == "WHILE"):
        match(TOKENS["while"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        Condition()
        match(TOKENS["parantes_close"], lookahead)
        match(TOKENS["aqulad_open"], lookahead)
        Body()
        match(TOKENS["aqulad_close"], lookahead)
    elif (lookahead == "FUNCTION"):
        match(TOKENS["function"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
        match(TOKENS["aqulad_open"], lookahead)
        Body()
        match(TOKENS["aqulad_close"], lookahead)
    elif (lookahead == "CALL_FUNC"):
        match(TOKENS["@"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "CALL_ID"):
        match(TOKENS["$"], lookahead)
        match(TOKENS["id"], lookahead)
    elif (lookahead == "SHARP"):
        Comment()
    elif (lookahead == "SET"):
        Assign()
    elif (
        lookahead == "ADD" or
        lookahead == "SUB" or
        lookahead == "MUL" or
        lookahead == "DIV"
    ):
        Operation()
    else:
        isAllConfirmed = False

def Body():
    if (
        lookahead == "IF" or
        lookahead == "FOR" or 
        lookahead == "WHILE" or
        lookahead == "FUNCTION" or
        lookahead == "CALL_FUNC" or
        lookahead == "CALL_ID" or
        lookahead == "SHARP" or
        lookahead == "SET" or
        lookahead == "ADD" or
        lookahead == "SUB" or
        lookahead == "MUL" or
        lookahead == "DIV"
    ):
        Syntax()
        Body()
    else:
        return True

def Condition():
    if (lookahead == "EQUAL"):
        match(TOKENS["eq"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "LITTLE_THAN"):
        match(TOKENS["lt"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "GRATER_THAN"):
        match(TOKENS["gt"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    else:
        isAllConfirmed = False

def Operation():
    if (lookahead == "ADD"):
        match(TOKENS["add"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "SUB"):
        match(TOKENS["sub"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "MUL"):
        match(TOKENS["mul"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)
    elif (lookahead == "DIV"):
        match(TOKENS["div"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)    
    else:
        isAllConfirmed = False    

def Assign():
    if (lookahead == "SET"):
        match(TOKENS["set"], lookahead)
        match(TOKENS["parantes_open"], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS[","], lookahead)
        match(TOKENS["id"], lookahead)
        match(TOKENS["parantes_close"], lookahead)  
    else:
        isAllConfirmed = False    

def Comment():
    if (lookahead == "SHARP"):
        match(TOKENS["#"], lookahead)
        match(TOKENS["id"], lookahead)
    else:
        isAllConfirmed = False 

# initation
Body()

afterTime = time.time()

# phase 1
etc = (countTotal - (countId + countKey))
print("\n\n============================= Compile phase 1 Status ==============================")
print("===================================================================================")
print(f"        Total words validated: {countTotal - 1} (ID: {countId}, KeyWords: {countKey}, etc: {etc}, errors: {countFailed})")
print("===================================================================================")
# phase 2
status = "No error"
if (not isAllConfirmed):
    status = "Error"
print("\n\n============================= Compile phase 2 Status ==============================")
print("===================================================================================")
print(f"                          Validation status: {status}")
print("===================================================================================")
# timer
timeElapsed = (afterTime - beforeTime)
roundedTime = round(timeElapsed, 3)
print("\n\n============================= Total compile time ==================================")
print("===================================================================================")
print(f"                          Total time elapsed: {roundedTime}s")
print("===================================================================================")
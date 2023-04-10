import re

print("""      
        **Welcome to Madlib game!** 
this game is to make a funny sentence, so you should input none ,verb ,adjective and numbers""")

def read_template(path):

    try:
      p=open(path)
      return p.read().strip("\n")

    except FileNotFoundError as error:
        print('not found!')
        print(error)

def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    x=text.split(' ')
    reg = r"^{\w+}|\.$"

    for i in x:
        if re.match(reg,i)==None :
            actual_stripped+=f"{i} "
        else :
            if i==x[-1]:
                actual_stripped += '{}.'
                actual_parts += [i[1:-2]]  
            else:
                actual_parts += [i[1:-1]]
                actual_stripped += '{} '

    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)
    

def merge(text,tep):
     return text.format(*tep)


def create_file(result ,file_to_write_on_it):
    with open(file_to_write_on_it, "w") as f:
        f.write(result)


def start_game(file_toRead_game,file_toWrite_game):
    text = read_template(file_toRead_game)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"\n{result}")
    create_file(result,file_toWrite_game)
  
  
if __name__=="__main__":
    start_game("assets/text_full.txt","assets/outcome.txt")
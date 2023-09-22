import databasestuff

#func space

def create_subject():
    name = input("Enter the name for the new subject: ")
    #content = input("Enter the content for the new subject (leave empty for none): ")

    new_subject = databasestuff.subject(name)
    #new_subject.content = content

    parent_name = input("Enter the name of the parent subject (leave empty for root): ")
    if parent_name:
        parent = find_subject(root, parent_name)
        if parent:
            parent.addchild(new_subject)
        else:
            print(f"Parent subject '{parent_name}' not found. Creating subject at the root.")
            root.addchild(new_subject)
    else:
        root.addchild(new_subject)

def find_subject(node, name):
    if node.name == name:
        return node
    for child in node.children:
        result = find_subject(child, name)
        if result:
            return result
    return None

#main space

root = databasestuff.subject("Root")

while True:
    inp = input("enter command: ")
    match inp:
        case "make_subject":
            create_subject()
        case "list":
            inpu = input("select perspective subject: ")
            if inpu != "root":
                print(find_subject(root, inpu))
            else:
                print(root)
        case "exit":
            break
        case "setup_sys_subject":
            sys = databasestuff.subject("system root")
            core = databasestuff.subject("system core")
            kernal = databasestuff.subject("kernal")
            root.addchild(sys)
            sys.addchild(kernal)
            sys.addchild(core)
        case "edit":
            inpu = input("what do you want to edit: ")
            if inpu == "content":
                ncon = input("new content: ")
                sub = input("what subject do you want to edit: ")
                find_subject(root, sub).edit_subject_content(ncon)
        case "read":
            inpu = input("what subject needs to be readed: ")
            print(find_subject(root, inpu).get_content())
print(root)
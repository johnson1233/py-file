class subject:
    def __init__(self, name):
        self.contents = 0
        self.subject_perms = "rw"
        self.save = 0
        self.children = []
        self.name = name
    
    def addchild(self, child):
        self.children.append(child)

    def get_content(self):
        if "r" in self.subject_perms:
            return self.contents
        else:
            print("access declined")

    def edit_subject_content(self, value):
        save = self.contents
        perm = self.subject_perms
        if "w" in self.subject_perms:
            self.save = self.contents
            self.contents = value
        else:
            print("access declined")

    def load_backup(self):
        self.contents = self.save

    def set_perm(self, permsnew):
        self.subject_perms = permsnew

    def __str__(self, level=0):
        result = "  " * level + f"{self.name}\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result


#active area:

# #setup subjects
# db = subject("work space")
# users = subject("users")
# managers = subject("lower management")
# systemsubjects = subject("sys")
# version = subject("sys_version")
# core = subject("system core")

# #adding children and content 
# systemsubjects.addchild(core)
# version.edit_subject_content("indev")
# systemsubjects.addchild(version)
# users.edit_subject_content(["jeff","joe","omar"])
# db.addchild(users)
# users.addchild(managers)
# db.addchild(systemsubjects)

# # print(db)
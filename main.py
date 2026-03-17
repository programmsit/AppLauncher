import subprocess

way_app = []
name_app = []
print("")
print("▄▀█ █▀█ █▀█ █░░ ▄▀█ █░█ █▄░█ █▀▀ █░█ █▀▀ █▀█")
print("█▀█ █▀▀ █▀▀ █▄▄ █▀█ █▄█ █░▀█ █▄▄ █▀█ ██▄ █▀▄")
print("--------------------------------------------")
print("--------------------------------------------")
print("выберите 1 что-бы добавить приложение      |")
print("                                           |")
print("выберите 2 что-бы зайти в список программ  |")
print("                                           |")
print("выберите 3 что-бы запустить приложение     |")
print("                                           |")
print("выберите 4 что-бы удалить приложение       |")
print("-"*43)



class app:

    def __init__(self,app_way,app_name):
        self.app_way = app_way
        self.app_name = app_name

    def add_app(self):
        way_app.append(self.app_way)
        name_app.append(self.app_name)
        #print(self.app_name,self.app_way)
        print("✅ приложение добавлено")

def app_input():
      global app_input_way,app_input_name
      app_input_way = input("путь:")
      app_input_name = input("имя приложение:")

while True:
    choose = int(input("выбор:"))

    if choose == 1:
        app_input()
        app_main = app(app_input_way,app_input_name)
        app_main.add_app()
        choose = 0
    
    if choose == 2:
        print(f"приложение:{name_app}")
        
    if choose == 3:
       
       programm_name = input("ведите название программы:")
       start=name_app.index(programm_name)
       
       print(start)

       file_start = way_app[start]
       print(file_start)
       subprocess.Popen(file_start)
       print("⚙️  приложение запускается")

    if choose == 4:
        del_app = input("ведите название программы:")
        del_app_in = name_app.index(del_app)
        name_app.pop(del_app_in)
        way_app.pop(del_app_in)
        print("🗑️  приложение удаленно")

    if choose == -1:
        break




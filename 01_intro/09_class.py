class Stack(object):
    def __init__(self): # Инициализация стека
        self.stack = [ ]    
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)

class Stack_(list):
# Добавить метод push() интерфейса стека
# Обратите внимание: списки уже имеют метод pop().
    def push(self,object):
        self.append(object)

s = Stack() # Создать стек
s.push('Dave') # Поместить на стек некоторые данные
s.push(42)
s.push([3,4,5])
x = s.pop() # переменная x получит значение [3,4,5]
y = s.pop() # переменная y получит значение 42
print (x,y)
del s # Уничтожить объект s
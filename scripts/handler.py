
def execute_move(operation, number, target):
    options[operation](number, target)

def plus(number, target):
    target.hp = target.hp + number

def minus(number, target):
    target.hp = target.hp - number

def times(number, target):
    target.hp = target.hp * number

def over(number, target):
    target.hp = target.hp / number

options = {
    '+' : plus,
    '-' : minus,
    'x' : times,
    '/' : over,
}

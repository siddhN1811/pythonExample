#Indirect Function Calls: “First Class” Objects
p=print
def echo(message):
    p(message)
echo('hello python')
x=echo
x('hello python')

def indirect(fun,args):
    fun(args)

indirect(echo,'hello python')
schedule = [ (echo, 'Spam!'), (echo, 'Ham!'),(echo, 'Raju!') ]
for (fun,args) in schedule:
    fun(args)
 

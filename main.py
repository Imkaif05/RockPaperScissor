import random
from flask import Flask,render_template,redirect,request
# opt=["Stone","Paper","Scissor"]

# while(True):
#     print("\n1]Stone \t 2]Paper \t 3]Scissor")
#     x=int(input("Choose any (1 or 2 or 3) : "))
#     if(x>3):
#         print("Wrong input !!")
#     else:
#         break
# x=x-1 #for convinence
# y=random.randrange(0,3)

# print(f"You choose : {opt[x]}")
# print(f"Oppents chooses : {opt[y]}")

results=[[0,1,-1],  #0=Draw
     [-1,0,1],      #1=Win
     [1,-1,0]]      #-1=Lose

# res=results[y][x]
# if(res==0):
#     print("The game is draw")   
# elif(res==1):
#     print("Congrats You won the game")    
# elif(res==-1):
#     print("Hard Luck ! You Lose the game")



app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        return redirect('/result')
    return render_template("index.html")

@app.route('/result',methods=["POST"])
def result():
    b_val=request.form.get('button_value')
    x=int(b_val)
    y=random.randrange(0,3)
    res=results[y][x]
    if(res==0):
        return render_template("tie.html",x=x,y=y)  
    elif(res==1):
        return render_template("win.html",x=x,y=y)   
    elif(res==-1):
        return render_template("lose.html",x=x,y=y)
    

if __name__=="__main__":
    app.run(debug=True,port=8000)
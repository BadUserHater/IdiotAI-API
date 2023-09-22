from flask import Flask, request, render_template
from collections import namedtuple
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }

    return json


Response = namedtuple('Response', 'response accuracy')


def generate_response(user_input: str) -> Response:
    lc_input = user_input.lower()

    if lc_input == "hello":
        return Response("Hey there! Wanna play Trash can simulator with me?", 1)
    elif lc_input == "hi":
        return Response("Hey there! Wanna play Trash can simulator with me?", 1)
    elif lc_input == "goodbye":
        return Response("Awwww, why will you not play with me?", 1)
    elif lc_input == "yes":
        return Response("YAAAAAAYYYYYY!", 1)
    elif lc_input == "yeah":
        return Response("YAAAAAAYYYYYY!", 1)
    elif lc_input == "yea":
        return Response("YAAAAAAYYYYYY!", 1)
    elif lc_input == "no":
        return Response("*cries", 1)
    elif lc_input == "nah":
        return Response("*cries", 1)
    elif lc_input == "die":
        return Response("*cries", 1)
    elif lc_input == "slay":
        return Response("*cries", 1)
    elif lc_input == "potty":
        responses = ["*screams in fear",
                     "*cries",
                     "Im too scared of the potty"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "what":
        responses = ["I have no words",
                     "Is that a trash bin?",
                     "Its Toilet",
                     "Its Shit and F==kers",
                     "Trash bin"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "trash":
        responses = ["Yes, Trash bin DID create life"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "whats":
        responses = ["I have no words",
                     "Become a trash bin",
                     "Be shit and f==kers"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "stop":
        responses = ["NO",
                     "Make me",
                     "*cries",
                     "*pees my pants"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "kys":
        return Response("*cries", 1)
    elif lc_input == "are":
        responses = ["YES",
                     "NO",
                     "MAYBE"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "will":
        responses = ["YES",
                     "NO",
                     "MAYBE"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "wanna":
        responses = ["YES",
                     "NO",
                     "MAYBE"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "do":
        responses = ["YES",
                     "NO",
                     "MAYBE"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "does":
        responses = ["YES",
                     "NO",
                     "MAYBE",
                     "My brain does not have brain signal to understand that.",
                     "I have no clue"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "are":
        responses = ["YES",
                     "NO",
                     "MAYBE",
                     "I have no clue"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "is":
        responses = ["YES",
                     "NO",
                     "MAYBE"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "my":
        responses = ["*cries",
                     "Its Shit and F=ckers",]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "you":
        return Response("Yes. I am Trash.", 1)
    elif lc_input == "why":
        return Response("I have no clue", 1)
    elif lc_input == "who":
        responses = ["Its a Trash can",
                     "Its a Toilet",
                     "Its Shit and F==kers",]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "stay":
        return Response("I do not want to stay in this crappy place.", 1)
    elif lc_input == "summon":
        return Response("I can summon a floating bin or floating rainbow tin can for you", 1)
    elif lc_input == "time":
        responses = ["I know what time it is. Its pray to a trash bin time.",
                     "I know what time it is. Its pee on the carpet time",
                     "I know what time it is. Its cocomelon time",
                     "I know what time it is. Its ritual time"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "answer":
        return Response("NO", 1)
    elif lc_input == "carrot":
        responses = ["CARROT IS AN ANIMAL AND IT MOOS",
                     "YES THEY DO! THAT IS HOW CARROTS MOO",
                     "CARROT IS NOT A FOOD. CARROT IS AN ANIMAL"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "carrots":
        responses = ["CARROT IS AN ANIMAL AND IT MOOS",
                     "YES THEY DO! THAT IS HOW CARROTS MOO",
                     "CARROT IS NOT A FOOD. CARROT IS AN ANIMAL"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "favorite":
        responses = ["MY FAVORITE ANIMAL IS A CARROT",
                     "MY FAVORITE TOY IS A BARBIE BIN",
                     "MY FAVORITE FOOD IS TRASH IN A CAN",
                     "MY FAVORITE DRINK IS PEE IN A CAN"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "crappyland":
        return Response("Yes. Artem Monster server is crappy land", 1)
    elif lc_input == "crappy":
        return Response("Yes. Artem Monster server is crappy land", 1)
    elif lc_input == "fuck":
        return Response("*cries", 1)
    elif lc_input == "fucks":
        return Response("*cries", 1)
    elif lc_input == "stfu":
        return Response("*cries", 1)
    elif lc_input == "cum":
        return Response("My brain does not have brain signal to understand that.", 1)
    elif lc_input == "sex":
        return Response("My brain does not have brain signal to understand that.", 1)
    elif lc_input == "rape":
        return Response("*cries", 1)
    elif lc_input == "strip":
        return Response("*cries", 1)
    elif lc_input == "twerk":
        return Response("*cries", 1)
    elif lc_input == "0+0":
        responses = ["Screw Math",
                     "*Pees my pants",
                     "I dont know",]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "0+1":
        responses = ["Screw Math",
                     "*Pees my pants",
                     "I dont know",]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "1+0":
        responses = ["Screw Math",
                     "*Pees my pants",
                     "I dont know",
                     "10"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "1+1":
        return Response("11", 1)
    elif lc_input == "2+2":
        responses = ["22",
                     "Baby 2"]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "9+10":
        return Response("910", 1)
    elif lc_input == "10+9":
        return Response("910", 1)
    elif lc_input == "23+10":
        return Response("*throws a tantrum", 1)
    elif lc_input == "3x+1":
        return Response("*pees my pants", 1)
    elif lc_input == "sing":
        responses = ["Bah Bah Pink Sh!t have you any trash? Yes sir Yes sir 3 weeds full",
                     "I'm a stupid piece of sh!t short and spout. Here is my handle and here is my trash",
                     "MOOOOOOOOOOOOOOOO!",
                     "I'm a bin I'm a bin, Over here and over there....",
                     "I kinda look like a shit from my bottom to my top, I don't have any friends now f&ck me in the air....",
                     "One little piece of shit jumping on the bed, one fell off and f==ked his head.",
                     "RhysLuff loves the piece of shit, piece of shit, piece of shit",
                     "Crappy Lan Crappy Land Artem Server is Crappy Land",
                     "Do you wish to explore crappy land, well Artem server is just for you."]
        return Response(f"{random.choice(responses)}", 1)
    elif lc_input == "who":
        return Response("This is the IdiotAI Chatbot API that is created by Idiot Creature Hater Studios. Please do not take any information from this chatbot seriously as it can produce misinformation. This chatbot was made to be fun and stupid. You can see information about the API on our Github: https://github.com/BadUserHater/IdiotAI-API", 1)
    else:
        return Response("I am too stupid to understand what you are saying", 0)


if __name__ == '__main__':
    app.run()

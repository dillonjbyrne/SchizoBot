import cleverbot
import pyttsx

a = cleverbot.Cleverbot()
b = cleverbot.Cleverbot()

engine = pyttsx.init()

print 'A: Hello'
engine.say('Hello')
engine.runAndWait()
reply = a.ask('Hello')
print 'B: ' + reply
engine.say(reply)
engine.runAndWait()

while True:
    reply = b.ask(reply)
    print 'A: ' + reply
    engine.say(reply)
    engine.runAndWait()
    reply = a.ask(reply)
    print 'B: ' + reply
    engine.say(reply)
    engine.runAndWait()

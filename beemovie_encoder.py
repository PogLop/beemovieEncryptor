result = ""
decode_result = ""

alphabet = {
    "a" : "According to all known laws/",
    "b" : "of aviation,/",
    "c" : "there is no way a bee/",
    "d" : "should be able to fly./",
    "e" : "Its wings are too small to get/",
    "f" : "its fat little body off the ground./",
    "g" : "The bee, of course, flies anyway/", 
    "h" : "because bees don't care/",
    "i" : "what humans think is impossible./",
    "j" : "Yellow, black. Yellow, black./",
    "k" : "Ooh, black and yellow!/",
    "l" : "Let's shake it up a little./",
    "m" : "Barry! Breakfast is ready!/",
    "n" : "Ooming!/",
    "o" : "Hang on a second./",
    "p" : "Hello?/",
    "q" : "- Barry?/",
    "r" : "- Adam?/",
    "s" : "- Oan you believe this is happening?/",
    "t" : "We're very proud of you, son./",
    "u" : "- I can't. I'll pick you up./",
    "v" : "Looking sharp./",
    "w" : "Use the stairs. Your father/",
    "x" : "paid good money for those./",
    "y" : "Sorry. I'm excited./",
    "z" : "Here's the graduate./"
}

decode = {
    "According to all known laws" : "a",
    "of aviation," : "b",
    "there is no way a bee" : "c",
    "should be able to fly." : "d",
    "Its wings are too small to get" : "e",
    "its fat little body off the ground." : "f",
    "The bee, of course, flies anyway" : "g", 
    "because bees don't care" : "h",
    "what humans think is impossible." : "i",
    "Yellow, black. Yellow, black." : "j",
    "Ooh, black and yellow!" : "k",
    "Let's shake it up a little." : "l",
    "Barry! Breakfast is ready!" : "m",
    "Ooming!" : "n",
    "Hang on a second." : "o",
    "Hello?" : "p",
    "- Barry?" : "q",
    "- Adam?" : "r",
    "- Oan you believe this is happening?" : "s",
    "- I can't. I'll pick you up." : "t",
    "We're very proud of you, son." : "u",
    "Looking sharp." : "v",
    "Use the stairs. Your father" : "w",
    "paid good money for those." : "x",
    "Sorry. I'm excited." : "y",
    "Here's the graduate." : "z"
}

while True:
    choice = input("encode/decode - ")
    if choice == "encode":
        result = ""
        word = input("type here word, that you want to encode (split with ""-"") - ")
        raw = word.split("-")
        for lett in raw:
            str(lett)
            if lett in alphabet:
                result += alphabet[lett]
        print(result)
    if choice == "decode":
        decode_result = ""
        letter = input("type here decoded word/s, that you want to decode - ")
        raw = letter.split("/")
        for word in raw:
            str(word)
            if word in decode:
                decode_result += decode[word]
        print(decode_result)
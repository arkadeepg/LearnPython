# Program to understand user defined functions


def emoji_converter(message):
    words = message.split()
    emojis = {
        ":)": "😀",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)


message = input(">")
emoji_converter(message)


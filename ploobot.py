import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

ascii_to_emoji = {
    "a": ":regional_indicator_a:", "b": ":regional_indicator_b:", "c": ":regional_indicator_c:",
    "d": ":regional_indicator_d:", "e": ":regional_indicator_e:", "f": ":regional_indicator_f:",
    "g": ":regional_indicator_g:", "h": ":regional_indicator_h:", "i": ":regional_indicator_i:",
    "j": ":regional_indicator_j:", "k": ":regional_indicator_k:", "l": ":regional_indicator_l:",
    "m": ":regional_indicator_m:", "n": ":regional_indicator_n:", "o": ":regional_indicator_o:",
    "p": ":regional_indicator_p:", "q": ":regional_indicator_q:", "r": ":regional_indicator_r:",
    "s": ":regional_indicator_s:", "t": ":regional_indicator_t:", "u": ":regional_indicator_u:",
    "v": ":regional_indicator_v:", "w": ":regional_indicator_w:", "x": ":regional_indicator_x:",
    "y": ":regional_indicator_y:", "z": ":regional_indicator_z:",
    "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:",
    "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "0": ":zero:",
    " ": " "
}

ascii_to_bold = {
    "A": "𝐀", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄",
    "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉",
    "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎",
    "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓",
    "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘",
    "Z": "𝐙", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒",
    "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗",
    "0": "𝟎", " ": " "
}

ascii_to_freaky = {
    "a": "𝓪", "b": "𝓫", "c": "𝓬", "d": "𝓭", "e": "𝓮",
    "f": "𝓯", "g": "𝓰", "h": "𝓱", "i": "𝓲", "j": "𝓳",
    "k": "𝓴", "l": "𝓵", "m": "𝓶", "n": "𝓷", "o": "𝓸",
    "p": "𝓹", "q": "𝓺", "r": "𝓻", "s": "𝓼", "t": "𝓽",
    "u": "𝓾", "v": "𝓿", "w": "𝔀", "x": "𝔁", "y": "𝔂",
    "z": "𝔃", " ": " "
}

ascii_to_default = {
    "a": "A", "b": "B", "c": "C", "d": "D", "e": "E",
    "f": "F", "g": "G", "h": "H", "i": "I", "j": "J",
    "k": "K", "l": "L", "m": "M", "n": "N", "o": "O",
    "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T",
    "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y",
    "z": "Z", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    "0": "0", " ": " "
}

flip_dict = {
    "a": "ɐ", "b": "q", "c": "ɔ", "d": "p", "e": "ǝ", "f": "ɟ", "g": "ɓ", "h": "ɥ", "i": "ᴉ", "j": "ſ",
    "k": "ʞ", "l": "l", "m": "ɯ", "n": "u", "o": "o", "p": "d", "q": "b", "r": "ɹ", "s": "s", "t": "ʇ",
    "u": "n", "v": "ʌ", "w": "ʍ", "x": "x", "y": "ʎ", "z": "z"
    }


zalgo_dict = [
    "̷", "̶", "̸", "̹", "̻", "̼", "͞", "͟", "͠", "͡", "͢", "ͣ", "ͤ", "ͥ", "ͦ", "ͧ", "ͨ", "ͩ", "ͪ", "ͫ",
    "ͬ", "ͭ", "ͮ", "ͯ", "Ͱ", "ͱ", "Ͳ", "ͳ", "ʹ", "͵", "Ͷ", "ͷ", "͸", "͹", "ͺ", "ͻ", "ͼ", "ͽ", ";", "Ϳ",
    "Ά", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ"
]


leet_dict = {
    "a": "4", "b": "8", "c": "(", "d": "|)", "e": "3", 
    "f": "|=", "g": "6", "h": "|-|", "i": "1", "j": ".]", 
    "k": "|<", "l": "|", "m": "/\\/\\", "n": "|\\|", 
    "o": "0", "p": "|o", "q": "O,", "r": "|2", "s": "5", 
    "t": "7", "u": "|_|", "v": "\\/", "w": "\\/\\/", 
    "x": "><", "y": "`/", "z": "2", " ": " "
}

morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
    "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
    "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": "/"
}

kaomoji_list = [
    "(✿◠‿◠)", "(｡♥‿♥｡)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(｡◕‿◕｡)", "(ʘ‿ʘ)", "(´• ω •`)", "(o´∀`o)", 
    "(✧ω✧)", "(･ω<)☆", "(≧◡≦)", "(＾▽＾)", "(✿´‿`)", "(￣▽￣)", "(⌒ω⌒)", "(♡°▽°♡)", 
    "(´｡• ᵕ •｡`)", "(☆▽☆)", "( ´ ▽ ` )", "(≧▽≦)", "(o^▽^o)", "(⌒‿⌒)", "(＾▽＾)", 
    "(╯✧▽✧)╯", "(>‿<)", "(ღ✪v✪)｡o♡", "(˶◕‿◕˶✿)", "(๑˃ᴗ˂)ﻭ", "(⁄ ⁄•⁄ω⁄•⁄ ⁄)"
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to  𝐏  𝐋  𝐎  𝐎")
        return

    words = user_input.upper().split(" ")
    widened_words = [
        "  ".join(ascii_to_bold.get(char, char) for char in word)
        for word in words
    ]
    final_output = "   ".join(widened_words)
    await ctx.send(final_output)

@bot.command()
async def upsidedownploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to flip")
        return

    # flip the text using the flip_dict
    flipped_input = ''.join(flip_dict.get(c, c) for c in user_input.lower())
    # reverse the flipped input
    # send help <3
    flipped_and_reversed_input = flipped_input[::-1]
    flipped_output = "  ".join(flipped_and_reversed_input)

    await ctx.send(flipped_output)

@bot.command()
async def binaryploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to convert into binary")
        return

    binary_output = "  ".join(format(ord(c), '08b') for c in user_input)
    await ctx.send(binary_output)

@bot.command()
async def freakyploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to freakyploo")
        return

    words = user_input.lower().split(" ")
    freaky_words = [
        "  ".join(ascii_to_freaky.get(char, char) for char in word)
        for word in words
    ]
    final_output = "   ".join(freaky_words)
    await ctx.send(final_output)

@bot.command()
async def zalgoploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to zalgo-ploo")
        return

    zalgo_output = "".join(char + random.choice(zalgo_dict) for char in user_input)
    await ctx.send(zalgo_output)

@bot.command()
async def superploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to SUPER-PLOO")
        return

    lines = []
    for char in user_input:
        # scatter effect idk what i am doing with my life
        spaces_before = " " * random.randint(1, 5)
        spaces_after = " " * random.randint(1, 5)
        lines.append(f"{spaces_before}{char}{spaces_after}")

    # make box so spamming is less annoying
    boxed_output = "\n".join(lines)
    await ctx.send(f"```\n{boxed_output}\n```")

@bot.command()
async def emojiploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to emojiPLOO")
        return

    words = user_input.lower().split(" ")
    emoji_words = [
        "  ".join(ascii_to_emoji.get(char, char) for char in word)
        for word in words
    ]
    final_output = "   ".join(emoji_words)
    await ctx.send(final_output)

@bot.command()
async def defaultploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to defaultploo")
        return

    words = user_input.lower().split(" ")
    default_words = [
        "  ".join(ascii_to_default.get(char, char) for char in word)
        for word in words
    ]
    final_output = "   ".join(default_words)
    await ctx.send(final_output)


@bot.command()
async def reverseploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to reverse")
        return
    
    reversed_input = user_input[::-1]
    reversed_output = "  ".join(reversed_input)
    await ctx.send(reversed_output)

@bot.command()
async def shufflploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to shuffle")
        return

    shuffled_input = ''.join(random.sample(user_input, len(user_input)))
    shuffled_output = "  ".join(shuffled_input)
    await ctx.send(shuffled_output)


#NEW COMMANDS!!!!!

@bot.command()
async def leetploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("Enter something for me to leetify")
        return

    leet_output = ''.join(leet_dict.get(char.lower(), char) for char in user_input)
    await ctx.send(leet_output)


@bot.command()
async def spongebobploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to mOcK")
        return

    spongebob_output = "".join(
        char.upper() if random.choice([True, False]) else char.lower()
        for char in user_input
    )
    await ctx.send(spongebob_output)


@bot.command()
async def morseploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to convert to morse code")
        return

    morse_output = "   ".join(morse_dict.get(char.lower(), char) for char in user_input)
    await ctx.send(morse_output)



@bot.command()
async def kaomojiploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to kaomojiploo")
        return

    random_kaomoji = random.choice(kaomoji_list)
    final_output = f"{user_input} {random_kaomoji}"

    await ctx.send(final_output)

@bot.command()
async def hexploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to hexploo")
        return

    hex_output = "  ".join(format(ord(c), 'x') for c in user_input)
    
    await ctx.send(hex_output)


@bot.command()
async def whaleploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to whaleploo")
        return

    vowels = "aeiou"
    whale_output = []

    for char in user_input:
        if char.lower() in vowels:
            # Extend the vowel randomly between 5 and 9 times
            extended_vowel = char * random.randint(5, 9)
            whale_output.append(extended_vowel)
        else:
            whale_output.append(char)

    final_output = "".join(whale_output)
    await ctx.send(final_output)

@bot.command()
async def numploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to numploo")
        return

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_to_num = {letter: index + 1 for index, letter in enumerate(alphabet)}

    num_output = "  ".join(str(letter_to_num.get(c.lower(), c)) for c in user_input)  
    await ctx.send(num_output)

@bot.command(name="uwuploo")
async def uwuploo(ctx, *, text: str):
    replacements = {
        'r': 'w',
        'l': 'w',
        'R': 'W',
        'L': 'W',
        'no': 'nyo',
        'No': 'Nyo',
        'NO': 'NYO',
        'ove': 'uv',
        'th': 'd',
        'Th': 'D',
        'TH': 'D'
    }
    #please kill me
    uwu_text = text
    for key, value in replacements.items():
        uwu_text = uwu_text.replace(key, value)

    uwu_specific_list = ["UwU", "OwO", ">w<", "^w^", "(*^ω^)", "uwu~"]
    uwu_text += " " + random.choice(uwu_specific_list)

    await ctx.send(uwu_text)

@bot.command(name="countploo")
async def countploo(ctx, *, text: str):
    characters = len(text)
    words = len(text.split())
    unique_letters = len(set(c.lower() for c in text if c.isalpha()))
    
    await ctx.send(f"Characters: {characters}\nWords: {words}\nUnique letters: {unique_letters}")


bot.run("your-very-skibidi-bot-token")

"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 1. An encrypted field brief was intercepted on the second night. It uses a Caesar cipher: every letter has been shifted forward in the alphabet by a fixed number. A shift of 3 turns a into d, b into e, and z wraps around to c.

Implement decrypt_brief(message, shift). Walk the message one character at a time. For each letter, shift it backwards by the given number, wrapping from a back to z. Leave spaces, punctuation, and digits unchanged. Handle both upper-case and lower-case letters separately, so A stays upper-case and a stays lower-case.

You will need two built-in functions you have not seen before. Research ord() and chr(). ord(ch) gives the number code of a character; chr(n) gives the character back from its code. The lower-case letters a to z have codes 97 to 122. The modulo operator handles the wrap-around.

For message khoor and shift 3 the result is hello. (When the cipher text was finally decoded on Day Three, it turned out to be a supply request for more tea bags. Classified, apparently.)
"""
def decrypt_brief(message, shift):
    decrypted = ""
    
    for ch in message:
        if ch.islower():
            new_code = (ord(ch) - ord('a') - shift) % 26 + ord('a')
            decrypted += chr(new_code)
        elif ch.isupper():
            new_code = (ord(ch) - ord('A') - shift) % 26 + ord('A')
            decrypted += chr(new_code)
        else:
            decrypted += ch
            
    return decrypted
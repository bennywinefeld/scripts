# Original encrypted message
original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print("Scrambled text:\n" + original)

# Method 1
print("\nMethod 1\nUnscrambled text:")
for char in original:
    if (char in [" ", ".", "(", ")", "'"]):
        new_char = char        
    else:
        unicode = ord(char) + 2
        if (unicode > ord('z')):
            unicode -= 26    
        new_char = chr(unicode)

    print(new_char,end='', flush=True)




# Method 2
print("\n\nMethod 2\nUnscrambled text:")
table = bytes.maketrans(b"abcdefghijklmnopqrstuvwxyz", b"cdefghijklmnopqrstuvwxyzab")

print(original.translate(table))
print("map".translate(table))


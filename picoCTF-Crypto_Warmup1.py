# Made for picoCTF Crypto Warmup1 challenge
# Could use almost everything from the Wrong version I made, just needed to reverse it
import sys

word = sys.argv[1]
keyword = sys.argv[2]

listAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
indexlist = []
keyindex = []
answer = ""
i = 0
for letter in word:
	indexlist.append(listAlphabet.index(letter.upper()))
for keyletter in keyword:
	keyindex.append(listAlphabet.index(keyletter.upper()))
while(i < len(indexlist)):
	realindex = indexlist[i] - keyindex[i]
	i += 1
	if realindex < 0:
		realindex += 26
	answer += listAlphabet[realindex]
print answer
# answer: SECRETMESSAGE

#     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
#    +----------------------------------------------------
# A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

# message: 	llkjmlmpadkkc
# key: 		thisisalilkey

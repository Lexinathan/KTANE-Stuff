startcode = input('Lowercase: ')
codeword = 'abcdefghijklmnopqrstuvwxyz'
translate = '0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 00 01 10 11 0 1'
codeword = [*codeword]
translate = translate.split(' ')
for c in translate:
    startcode = startcode.replace(codeword[translate.index(c)],c)
startcode = [*startcode]
tree = ['0','1']
hold = ''
while not(len(tree) == 26):
    hold = hold + startcode[0]
    startcode.pop(0)
    if hold in tree:
        treeind = tree.index(hold)
        tree.remove(tree[treeind])
        tree.insert(treeind,hold+'1')
        tree.insert(treeind,hold+'0')
        hold = ''
hold2 = ''
for c in startcode:
    hold = hold + c
    if hold in tree:
        hold2 = hold2 + codeword[tree.index(hold)]
        hold = ''
input(hold2)

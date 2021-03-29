def revword(word:str):
    word=word.lower()
    return(word[::-1])

def countword() ->int:
    text=open('text.txt','r')
    text=text.read().split()
    count=0
    word=text[0]
    print(word)
    for chek in text:
            test=revword(chek)
            if test==word:
                count+=1
    return(count+1)

print(countword())



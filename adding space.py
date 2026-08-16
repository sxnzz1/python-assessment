def insert_space():
    
    sentance = (input("Enter string:"))
    answer = sentance[0]
    for i in sentance[1:]:
        if i.isupper(): 
            answer += (" ")
        answer += i
    print(answer)

insert_space()

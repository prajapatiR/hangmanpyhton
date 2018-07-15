import random
words_hint={'apple':'a common fruit','ball':'a common famous sports instrument','shinchan':'a famous kids cartoon'}
words=['apple','ball','shinchan']
secret_word=random.choice(words)
ans=list(secret_word)
usr_ans=[]
dash="-"*len(secret_word)
life=10

while True:
	if usr_ans==ans:
		print("you won!!!")
		break
	if life>0 and usr_ans!=ans and len(ans)!=0:
		print('"'+"- "*len(secret_word)+'"'+"\n" +
		"Guess The Word"+"\n"+
		"HINT: "+words_hint[secret_word])

		x=str(input('your answer("please note enter the desrired answer word by word)": '))

		if x in ans and len(ans)!=0:
			life=life
			print("%s is correct guess" %(x))
			k=ans.index(x)
			ans.pop(k)
			print(life)
			
			usr_ans.append(x)
			print(usr_ans)
			continue
		
		else :
			life-=1
			print("%s is wrong guess" %(x))
			print(life)
	elif len(ans)==0:
			print("right Guess: "+'"'+secret_word+'"' )
			break
	elif life==0:
		print("you lost")
		break
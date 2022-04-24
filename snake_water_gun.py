import random as rd
import time



def final(name, u_s, c_s ):
    if u_s > c_s:
        print(f"congretulation {name}, you won the game")
    elif u_s < c_s:
        print("BETTER LUCK FOR NEXT TIME")
    else:
        print(f"ohh, {name} it's TAI ")



def result(user_cho, co_cho, user_score, comp_score):

    if user_cho == co_cho:
        print("TAI!")
    elif user_cho=="WATER" and co_cho=="GUN":
        user_score += 1
        print("you win.")
    elif user_cho=="WATER" and co_cho=="SNAKE":
        comp_score += 1
        print("computer win...")

    elif user_cho=="SNAKE" and co_cho=="GUN":
        comp_score += 1
        print("computer win.")
    elif user_cho=="SNAKE" and co_cho=="WATER":
        user_score += 1
        print("you win.")
    elif user_cho=="GUN" and co_cho=="SNAKE":
        user_score += 1
        print("you win.")
    elif user_cho=="GUN" and co_cho=="WATER":
        comp_score += 1
        print("computer win.")


    return [user_score, comp_score]




if __name__ == '__main__':
    name = input("your good name please: ")
    i=1

    while True:
        re=input(f"Hey!,dear {name}, are you radey to play game? [yes/no] :").upper()


        if re == "YES":
            tim = int(input("how many time would you like to play? :"))
            t = 0
            print("ok, let's start")
            lst = ["SNAKE", "WATER", "GUN"]
            usr_score=0
            comp_score=0
            while True:
                t+=1

                user_choise = input(f"enter your choise: from {lst}: ").upper()


                if user_choise not in lst:
                    t-=1
                    print("you select wrong item.. try again")
                    continue
                else:

                    print("your input is processed...")
                    time.sleep(2)
                    com_choise = rd.randint(0, 2)
                    if com_choise == 0:
                        cose = "SNAKE"
                    elif com_choise == 1:
                        cose = "WATER"
                    else:
                        cose = "GUN"

                    result1=result(user_choise, cose, usr_score,comp_score)
                    usr_score=result1[0]
                    comp_score=result1[1]



                    if t == tim:
                        break
                    else:
                        continue
            print("Final result....")
            time.sleep(3)
            final(name, result1[0], result1[1])
            time.sleep(1)
            v= input("would you like to start new game?[yes/no] :").lower()
            time.sleep(1)
            if v == "yes":
                continue
            else:
                time.sleep(1)
                print("ok, no problem. Have a Nice Day!")
                break



        else:
            i+=1

            if i == 3:
                print("ok, no problem. i will see you next time")
                break
            print("further ask you...")
            continue

























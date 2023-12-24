        #write b

                # bbbbbbbbbbbbbbbb



def name ():
    def latter_b ():
        a = 1
        while a < 12:
            a += 1
            if a < 12:
                print ("*", "".ljust(14, "*") if a == 2 or a == 6 or a == 11 else "*".rjust(15))
            else:
                print ("\n\n")

    latter_b()


                      # aaaaaaaaaaaaaaaaaa

    def latter_a():
        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print ("*".rjust(12 - a) , "*".ljust(13, "*") if a == 7 else "*".rjust(2*a - 1))
            else:
                print ("\n\n")


    latter_a()



                        # hhhhhhhhhhhhhhhhhhhh



    def latter_h():
        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print ("*", "".rjust(14, "*") if a == 5 else "*".rjust(15))
            else:
                print ("\n\n")
    latter_h()




                    # oooooooooooooooooooooooo


    def latter_o():
        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print ("*", "".rjust(14, "*")if a == 1 or a == 11 else "", "*".rjust(14) if a in [i for i in range (2, 11)] else "" )
            else:
                print("\n\n")


    latter_o()




                    # dddddddddddddddddddddddddddddddd


    def latter_d():

        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print("*", "".rjust(12, "*") if a == 1 or a == 11 else "", "*".rjust(13) if a == 2 or a == 10 else "", "*".rjust(14) if a in [i for i in range (3, 10)] else "")
            else:
                print("\n\n")

    latter_d()




                    # iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

    def latter_i():

        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print("*".rjust(8))
            else:
                print("\n\n")


    latter_i()



                    # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    def latter_r():

        a = 0
        while a < 12:
            a += 1
            if a < 12:
                print("*", "".rjust(12, "*") if a == 1 or a == 6 else "", "*".rjust(13) if a == 2 or a == 5 else "", "*".rjust(13) if a == 3 or a == 4 else "", "*".rjust(a) if a > 6 else "")
            else:
                print("\n\n")


    latter_r()





name()

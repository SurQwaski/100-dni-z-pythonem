import sys

print("\033[92m" + r"""
___|____|____|____|____|____|____|____|____|____|____|____|
_|____|____|____|____|____|____|____|____|____|____|____|__
___|____|____|____|____|____|____|____|____|____|____|____|
_|____|____|____|____|____|____|____|____|____|____|____|__
___|____|____|     _______________     |____|____|____|____
_|____|____|    _.' _._._._._._._ '._    _|____|____|____|_
___|____|____| / .-'             '-. \ |____|____|____|____
_|____|____|  | /                   \ |  _|____|____|____|_
___|____|____|:;___[___________]___;:|___|____|____|____|__
_|____|____|__|:|                   |:|__|____|____|____|__
___|____|____||:|    ___     ___    |:||____|____|____|____
_|____|____|__|:|   |_O_|   |_O_|   |:|__|____|____|____|__
___|____|____||:|                   |:||____|____|____|____
_|____|____|__|:|___________________|:|__|____|____|____|__
___|____|____| \_____________________/ |____|____|____|____
_|____|____|____|____|____|____|____|____|____|____|____|__
""" + "\033[0m")
print("Welcome to the Treasure Island. \n " \
"The goal of your journey is to find the treasure hidden on the island.")
crossroad_decision = input("You find yourself at the crossroads, from here you can go either left or right. \n Where do you wish to go? ")
if crossroad_decision == "right":
    print("You decide to go right. The road leads to an active bandit camp.\n" \
    "You are taken hostage and live the rest of your live as a slave. GAME OVER")
    sys.exit()

print("\033[92m" + r"""
                                     |
                                   \ _ /
                                 -= (_) =-
                                   /   \
                                     |

                                 _.-._
                               .'     '.
                             .'  _   _  '.
                           .'   / \ / \   '.
                          '    /   V   \    '
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ~   ~    ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~
    ~    ~   ~    ~   ~   ~    ~   ~   ~   ~    ~   ~    ~   ~
~    ~       ~       |=============|       ~        ~       ~
  ~      ~       ~   |=============|  ~        ~        ~      ~
     ~       ~       |=============|       ~        ~       ~
 ~       ~       ~   |=============|   ~       ~        ~      ~
     ~       ~      /===============\      ~        ~       ~
~      ~        ~  /=================\  ~       ~       ~      ~
   ~       ~      /===================\     ~       ~       ~
""" + "\033[0m")

lake_decision = input("You decide to go left. For a while nothing happens, but eventually you end up at a ferry dock.\n" \
"In the distance a mysterious island can be seen. You can try and swim to the island or wait for a ferry. What is your decision, swim or wait? ")

if lake_decision == "swim":
    print("You begin to swim. The island is further than it first appeared to be. \n" \
    "It doesn't take to long for you to grow tired and eventually drown. GAME OVER")
    sys.exit()

print("\033[92m" + r"""
                      /\
                     /  \
                    /    \
                   /      \
                  /        \
                 /          \
                /            \
               /              \
              /                \
             /                  \
            /                    \
           /                      \
          /                        \
         /                          \
        /                            \
       /                              \
      /                                \
     /                                  \
    /                                    \
   /                                     \
  /                                       \
 /                                         \
/____________________________________________\
|                                            |
|      +--+          +--+          +--+      |
|      |  |          |  |          |  |      |
|      |o |          |o |          |o |      |
|      |  |          |  |          |  |      |
|______|__|__________|__|__________|__|______|
""" + "\033[0m")

house_decision = input("After a while a ferry comes and takes you to the island. \n" \
"Before you stands a home with three wooden doors, each painted in a different colour. \n" \
"Which door would you like to go through? Red, yellow or blue? ")

if house_decision == "red" or house_decision == "blue":
    print("As you approach the door and try to open it, the door swallows you whole. GAME OVER")
    sys.exit()
else:
    print("You enter through the yellow door and find yourself in a square room with a golden chest in the middle. \n" \
    "At last. You found the treasure and your journey has come to an end. YOU WIN!")
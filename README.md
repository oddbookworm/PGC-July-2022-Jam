Pygame Community Jam July 2022

Dimensional Snake!

It's snake, but you can move horizontally between rooms and vertically between rooms! New fun ways to play the game abound! Can you find the easter egg?
Note that the number of rooms is 8 total in a 2x2x2 cube. You start off on the bottom "floor" in the back left of the map. Move in the plane of the screen with WASD. Pressing "E" takes you up a floor and pressing "Q" takes you down a floor. I've helpfully displayed your current floor in the top left corner of the screen and put red boundaries where the death zone is. Don't try to go below floor 0 or above floor 1. You will die.

Press "R" at the Game Over screen to restart.

Credit for the pygame snake image goes to @Sjmarf#1894 on Discord

To run:
Option 1) Run game/main.py through your python interpreter (Probably compatible with python 3.5+)<br>
Option 2) From the root directory, run `python -m game`<br>
Option 3) Run the executable provided or create it yourself<br>(pyinstaller command on windows is `pyinstaller --onefile --add-data "./game/*;." ./game/main.py`)<br>
Option 4) From the root directory, run `pygbag game` and go to localhost:8000

Discord ID: @Andrew Coffey#9386
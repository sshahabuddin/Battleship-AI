# Battleship-AI
How to run battleship game:
1. First install python 3 and pygame package. https://www.pygame.org/wiki/GettingStarted 
2. Run the Battleship.py file.  For windows, open command prompt and enter py scriptpath.
My path:
py C:\Users\rayra\OneDrive\Desktop\final_project_team_5\battleship\Battleship.py

Running the Game:
1. Title screen will display with two algorithm options. Click which algorithm you want to use, Brute-force or heuristic.
2. A new screen will appear asking the user to click the positions to place the ships. For example, if placing ship size 5 click one tile and another one four tiles away. Repeat until all ships are placed.
3. Main game screen will display with two 10 by 10 grids to the left and right of the screen. Left grid records user shots and right grid displays users ships and enemy shots fired. The user will click a tile on the left grid to fire at. After selecting the tile, the user needs to click the fire button to fire.
4. A new screen will appear displaying the results of the user's shot. (a miss or a hit)
5. Another screen will appear displaying the return fire of the AI. (a miss or a hit)
6. The main game screen will reappear with both grids updated to show the result of the user's and AI's fire.
7. Repeat steps 3-6 until the user or the AI has sunk the opposing player's ships.
8. After destroying the opposite player's ships (17 total hits), the game will display a winning screen if the user won or a losing screen if the user lost to the AI.
Note: restart program to choose a different algorithm

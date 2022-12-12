# Import the random module
import random

# Define the grid size
GRID_SIZE = 5

# Create the grid
grid = []
for i in range(GRID_SIZE):
  row = []
  for j in range(GRID_SIZE):
    row.append('-')
  grid.append(row)

# Place the battleships on the grid
# (in this example, we will place two battleships on the grid)
ships = []
for i in range(2):
  placed = False
  while not placed:
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    if grid[x][y] == '-':
      grid[x][y] = 'B'
      ships.append((x, y))
      placed = True

# Main game loop
while True:
  # Print the grid
  for row in grid:
    print(' '.join(row))

  # Prompt the user for their move
  x = int(input('Enter x coordinate: '))
  y = int(input('Enter y coordinate: '))

  # Check if the user hit a battleship
  hit = False
  for ship in ships:
    if x == ship[0] and y == ship[1]:
      grid[x][y] = 'X'
      ships.remove(ship)
      hit = True
      break

  # If the user didn't hit a battleship, mark the space as missed
  if not hit:
    grid[x][y] = 'O'

  # Check if the game is over
  if len(ships) == 0:
    print('You won!')
    break

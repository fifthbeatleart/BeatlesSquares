#  Created on: Nov 1, 2021
#      Author: Fifth Beatle art studio
#      E-mail: fifthbeatleart@gmail.com

# Generate next row that doesn't contradict with existing columns:
def next_row(n : int, columns : list, row = []):
   if len(row) == n:
      yield row
   for i in range(n):
      # If element i is absent in row and column, add it to row:
      if i not in row and i not in columns[len(row)]:
         yield from next_row(n, columns, row+[i])

# Generate next Latin square:
def next_square(n : int, square = []):
  if len(square) == n:
     yield square
  else:
     # If a partial square is empty, its columns is empty:
     if len(square) == 0:
        columns = [[]]*n
     # Otherwise, get columns:
     else:
        columns = list(zip(*square))
     for row in next_row(n, columns):
        yield from next_square(n, square+[row])

# Count Beatles in rows, columns, diagonals, and 2*2 subsquares.
def count_beatles(square : list):
  res = 8 # each square has at least 8 Beatles - in 4 rows and 4 columns
  if is_diagonal(square): # 2 more Beatles in main diagonal and main antidiagonal
    res += 2
  n = len(square)
  # Count Beatles in 2*2 subsquares:
  for i in range(n-1):
    for j in range(n-1):
      subsquare = [square[i][j], square[i][j+1], square[i+1][j], square[i+1][j+1]]
      if len(set(subsquare)) == n:
        res += 1
  return res

# Transpose a square:
def transpose(square : list):
  n = len(square)
  res = [[None]*n for i in range(n)]
  for i in range(n):
    for j in range(n):
      res[j][i] = square[i][j]
  return res

# Check if a square is diagonal, i.e. both main diagonal and antidiagoal are distinct:
def is_diagonal(square : list):
  n = len(square)
  diag = [square[i][i] for i in range(n)]
  antidiag = [square[n-i-1][i] for i in range(n)]
  if len(set(diag)) == n and len(set(antidiag)) == n:
    return True
  return False

# Check if a square is equal-diagonal, i.e. the main diagonal contains only one element,
# and the same for the main antidiagonal:
def is_equal_diagonal(square : list):
  n = len(square)
  diag = [square[i][i] for i in range(n)]
  antidiag = [square[n-i-1][i] for i in range(n)]
  if len(set(diag)) == 1 and len(set(antidiag)) == 1:
    return True
  return False

# Check if a square is parallel, i.e. either each diagonal contains only repeating
# elements or the same holds for all antidiagonals.
def is_parallel(square : list):
  n = len(square)
  one_element_diagonal_num = 0
  for i in range(n):
    diag = [square[j][n-1-i+j] for j in range(i+1)]
    if len(set(diag)) == 1:
      one_element_diagonal_num += 1
  if one_element_diagonal_num == n:
    return True
  one_element_antidiagonal_num = 0
  for i in range(n):
    diag = [square[i-j][j] for j in range(i+1)]
    if len(set(diag)) == 1:
      one_element_antidiagonal_num += 1
  if one_element_antidiagonal_num == n:
    return True
  return False

# Check if a square is alphabetical, i.e. both first row and first column are in
# alphabetical order by Beatles surnames.
def is_alphabetical(square : list):
  n = len(square)
  first_row = square[0]
  first_column = [row[0] for row in square]
  sorted_arr = [i for i in range(n)]
  if first_row==sorted_arr and first_column==sorted_arr:
    return True
  return False

# Check if a square is mirror, i.e. its cells are reflected if the main diagonal is considered
# a mirror and the same for the main antidiagonal.
def is_mirror(square : list):
  # Check if mirror over the main diagonal:
  n = len(square)
  for i in range(n):
    for j in range(n):
      if square[i][j] != square[j][i]:
        return False
  # Check if mirror over the main antidiagonal:
  if square[0][0] != square[3][3] or square[0][1] != square[2][3] or square[0][2] != square[1][3] or\
     square[1][0] != square[3][2] or square[1][1] != square[2][2] or\
     square[2][0] != square[3][1]:
     return False
  return True

# Check if a square is true mirror, i.e. its cells are reflected if the main diagonal is considered
# a true mirror and the same for the main antidiagonal.
def is_truemirror(square : list):
  # Make a mirror-like and check:
  #tmp_square = [row for row in square]
  square[0][1], square[0][2] = square[0][2], square[0][1]
  square[3][1], square[3][2] = square[3][2], square[3][1]
  res = is_mirror(square)
  # Reverse changes:
  square[0][1], square[0][2] = square[0][2], square[0][1]
  square[3][1], square[3][2] = square[3][2], square[3][1]
  return res

# Print a square: row per line:
def print_square(square : list):
  for row in square:
    print(row)

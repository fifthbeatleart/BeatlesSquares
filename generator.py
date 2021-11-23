#  Created on: Nov 1, 2021
#      Author: Fifth Beatle art studio
#      E-mail: fifthbeatleart@gmail.com

import sys
import square as sqr

isPlot = True
try:
  import plotter as plttr
except ModuleNotFoundError as err:
  print("File plotter.py is not found, so plotting of squares is disabled.")
  print("Should you need the full version please contact the developer.")
  isPlot = False

version = "1.0.0"

BEATLES_SQUARES_NUM = 576
ORDINARY_CLASS = "Ordinary"
DIAGONAL_CLASS = "Diagonal"
CROSS_CLASS = "Cross"
PARALLEL_CLASS = "Parallel"
MIRROR_CLASS = "Mirror"
TRUEMIRROR_CLASS = "TrueMirror"
ALPHABETICAL_CLASS = "Alphabetical"
TOTAL_CLASS = "BeatlesSquares"

squares_to_plot = 0
if (len(sys.argv) >= 2):
  if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print("Usage: script [plot_num]")
    print(" Generate all Beatles squares and (optionally) plot them.")
    print(" plot_num : integer, number of Beatles squares to plot, at most 576.")
    sys.exit()
  else:
    squares_to_plot = int(sys.argv[1])
    if not isPlot:
      squares_to_plot = 0
    elif (squares_to_plot > BEATLES_SQUARES_NUM or squares_to_plot < 0):
      squares_to_plot = BEATLES_SQUARES_NUM
      print("Incorrect plot_num, changed to", squares_to_plot)

print("squares to plot : ", squares_to_plot)
squares_num = 0
n = 4
square_class_id = 0
options_dict = {}
# Number of Beatles in a square is at least 8 and at most 19:
#beatles_squares_num = [0 for i in range(20)]

for square in sqr.next_square(n):
  squares_num += 1
  #print_square(square)
  #print("")
  #beatles_num_in_square = sqr.count_beatles(square)
  #beatles_squares_num[beatles_num_in_square] += 1
  square_options = ""
  if sqr.is_alphabetical(square):
    square_options += "alph"
  if sqr.is_diagonal(square):
    if square_options != "":
      square_options += "-"
    square_options += "diag"
  if sqr.is_equal_diagonal(square):
    if square_options != "":
      square_options += "-"
    square_options += "cross"
  if sqr.is_parallel(square):
    if square_options != "":
      square_options += "-"
    square_options += "parall"
  if sqr.is_mirror(square):
    if square_options != "":
      square_options += "-"
    square_options += "mirror"
  if square_options == "":
    square_options = "ordin"
  if square_options not in options_dict:
    options_dict[square_options] = 1
  else:
    options_dict[square_options] += 1
  if squares_num <= squares_to_plot:
    plttr.plot_square(square, squares_num, TOTAL_CLASS, square_options)
    print("Saved", squares_num, "squares")

squares_in_dict = 0
for i in options_dict:
  squares_in_dict += options_dict[i]
if squares_num != squares_in_dict:
  print("Warning: total num is not equal to the sum of dict squares.")

print("Total squares                 : ", squares_num)
print(options_dict)
#print(" of which")
#print("  Ordinary                    : ", ordinary_squares_num)
#print("  Alphabetical                : ", alphabetical_squares_num) 
#print("  Diagonal                    : ", diagonal_squares_num)
#print("  Cross                       : ", cross_squares_num)
#print("  Parallel                    : ", parallel_squares_num)
#print("  Mirror                      : ", mirror_squares_num)
#print("  TrueMirror                  : ", truemirror_squares_num)
#print("Number of Beatles in squares  :")
#print(beatles_squares_num)

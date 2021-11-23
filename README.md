# Beatles squares generator

<p align="center">
<b>This project mixes art, science, and The Beatles by introducing <i>Beatles squares</i></b>.
<br>
All 576 unique Beatles squares are <a href="images/BeatlesSquares/">here</a>.
</p>

## The Beatles

[The legendary Beatles](https://en.wikipedia.org/wiki/The_Beatles) are (in alphabetical order by last name):
- *George Harrison*
- *John Lennon*
- *Paul McCartney*
- *Ringo Starr*

Here they are on portraits painted with great respect and love in our studio:

<img src="images/Beatles/Beatles.png" width="400" height="100">

## Beatles squares

A Beatles square is a 4x4 table filled with members of The Beatles such that each row and each column is The Beatles, i.e. it contains all the four members.

**Example of a Beatles square:**

<img src="images/BeatlesSquares/042_ordin.png" width="400" height="400">

## Properties

Let's enumerate cells of a Beatles square as follows:  
11 12 13 14  
21 22 23 24  
31 32 33 34  
41 42 43 44  

Cells of the first row are: 11 12 13 14, while ones fo the first column are: 11 21 31 41. Cellas of the main diagonal are: 11 22 33 44, the ones of the main antidiagonal are: 41 32 23 14.

A Beatles square may have the following main properties:
- *alphabetiacal* - the first row and first column are in alphabetical order by the last name, i.e. the order is: George Harrison, John Lennon, Paul McCartney, Ringo Starr.
- *cross* - all four elements of the main diagonal are equal to each other, i.e. it contains four instances of one member of the Beatles. The same holds for the main antidiagonal (but the member is different). As a result, a clear (digonal) cross is formed. 
- *diagonal* - the main diagonal is The Beatles, i.e. it contains all the four members, the same holds for the main antidiagonal. In other words, all elements of these two diagonals are distinct just like in all rows and columns, so 10 The Beatles are formed instead of 8.
- *mirror* -  the main diagonal is considered a mirror, i.e. cells from the left-bottom triangle are reflected to the ones from the right-top triangle. The same holds for the main antidiagonl.
- *parallel* - each diagonal (or each antidiagonal) contains instances of only one member of The Beatles. As a result, the square looks like a set of parallel lines.

An example of diagonal Beatles square is:

<img src="images/BeatlesSquares/021_diag.png" width="400" height="400">

And here is an example of parallel one:

<img src="images/BeatlesSquares/018_parall.png" width="400" height="400">

Based on these properties, 576 Beatles squares were divided into 4 classes: *ordinary*, *advanced*, *rare*, and *super rare*.
- *ordinary*: 407 squares with no mentioned properties. The Beatles square from the example above belongs to this class.
- *advanced*: 142 squares with exactly one of the following properties: cross, diagonal, mirror, parallel.
- *rare*: 23 squares with two properties cross and mirror, i.e. cross-mirror squares.
- *super rare* 4 alphabetical squares. In fact, the first of them is pure alphabetical, the second is alphabetical-mirror, the third is alphabetical-parallel, and the fourth is alphabetical-cross-mirror.

The alphabetical-cross-mirror square is:

<img src="images/BeatlesSquares/001_alph-cross-mirror.png" alt="Beatles" width="400" height="400">

## Generator

The script generator.py generates all of them and (optionally) plots images to files.

## Required packages

python3.6+

## Usage

python3 ./generate.py plot_num

where plot_num is the number of Beatles squares to plot, at most 576.

## NFT collection

Beatles squares is an NFT collection comprised of 576 unique items. The items are based on portraits of The Beatles, exclusively made for this collection, and a combinatorial design known as Latin square. There are 407 ordinary, 142 advanced, 23 rare, and 4 super rare squares. The collection is dedicated to a long-awaited release of The Beatles: Get Back documentary series. We are mixing art, science, and The Beatles to promote this series. Come together, right now, over NFT!


# 0 = abcefg    (6)
# 1 = cf        (2)*
# 2 = acdeg     (5)
# 3 = acdfg     (5)
# 4 = bcdf      (4)*
# 5 = abdfg     (5)
# 6 = abdefg    (6)
# 7 = acf       (3)*
# 8 = abcdefg   (7)*
# 9 = abcdfg    (6)

# 1 = cf        (2)*
# 4 = bcdf      (4)*
# 7 = acf       (3)*
# 8 = abcdefg   (7)*

# 2 = acdeg     (5)
# 3 = acdfg     (5)
# 5 = abdfg     (5)

# 0 = abcefg    (6)
# 6 = abdefg    (6)
# 9 = abcdfg    (6)

#       *                     *                  *         * |
#       7     5     5     5   3      6      6    4      6  2 |
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
#         --- * *---  - - -     --  -- --  --      -  ---    |
#       8     5     2     3   7      9      6    4      0  1 |

#  aaaa    dddd
# b    c  f    a
# b    c  f    a
#  dddd    eeee
# e    f  c    b
# e    f  c    b
#  gggg    gggg

# if it has 2 characters then it's 1

# if it has 3 characters then it's 7

# if it has 4 characters then it's 4

# if it has 7 characters then it's 8

# if it has 5 characters then it's either 2, 3, or 5
# and it has all of 1's characters, then it's 3
# and it's missing two of 4's characters, then it's 2
# then the last 5 is 5

# if it has 6 characters then it's either 0, 6, or 9
# and it doesn't have all of 1's characters, then it's 6
# and it has all of 4's characters, then it's 9
# then the last one is 0

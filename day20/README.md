# Day 20

Went with 2D convolution using NumPy. Used NumPy's stride trick to perform 2D convolution on a padded array.

One thing to note is that the image enhancement algorithm is sneaky (at least for my puzzle input) -- the image's background alternates between dark and light for every step, starting with light background. We made use of padding values 0 and 1 to cope with the changing background respectively.

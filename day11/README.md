# Day 11

Initially wanted to do 2D convolution but... updating an energy is not limited to the sliding window.

Because updating an energy might result in updating the neighbouring energies, and in turn the neighbours' neighbouring energies, defining energy updates recursively is simpler to reason about.

```txt
def update(x):
    update_energy(x)
    for neighbour in neighbours(x):
        update(neighbour)
```

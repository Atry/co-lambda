# tablambda

[![CI](https://github.com/Atry/tablambda/actions/workflows/ci.yml/badge.svg)](https://github.com/Atry/tablambda/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/tablambda)](https://pypi.org/project/tablambda/)
[![Python versions](https://img.shields.io/pypi/pyversions/tablambda)](https://pypi.org/project/tablambda/)
![License: MIT](https://img.shields.io/pypi/l/tablambda)

The artifact for the paper *Cyclic Graphs and Memoization in Pure
$\lambda$-Calculus*. It is a pure lambda-calculus interpreter and compiler in
which programs that loop on themselves or repeat work just run: you write ordinary
pure lambda terms and get cyclic and infinite data structures with no added
recursion construct, automatic memoization and dynamic programming with no
hand-written cache, and a meaningless value for a diverging loop such as `Ω`
instead of a hang, all while the calculus stays pure.

This repository is a uv workspace with three packages and the paper:

- [`packages/fixpoints`](packages/fixpoints) provides the least-fixpoint
  cached-property infrastructure that drives mutually recursive computations to a
  fixpoint.
- [`packages/tablambda`](packages/tablambda) is the pure lambda-calculus
  interpreter and compiler (published to PyPI as `tablambda`).
- [`packages/tablambda-examples`](packages/tablambda-examples) holds example
  applications written as pure lambda terms, their committed defunctionalized
  (compiled) modules, and the interpreted versus compiled benchmark.
- [`paper`](paper) is the LaTeX source whose semantics the
  interpreter realizes.

## Install

```sh
pip install tablambda
```

## Development

Run development commands through the Nix dev shell, and build distributable
artifacts as Nix packages:

```sh
# Run the test suite
direnv exec . uv run pytest

# Run the interpreted versus compiled benchmark
nix build -L .#tablambda-benchmark-pypy

# Build the paper's supplementary material bundle
nix build -L .#tablambda-supplementary-material
```

## License

MIT. See [`LICENSE`](LICENSE).

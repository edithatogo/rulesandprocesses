# Provenance and Reproducibility Evidence

The reproducibility evidence snapshot is anchored to reviewed ancestor commit
`e8da58fd94018191da7a5ad3ffde48ecc1cb990d`. Dependency resolution is pinned by
`contracts/tools/uv.lock`, whose SHA-256 is
`3fc7fa479b9e3cc53640dd4b6c408afa22a2c0c27d32c3c2451ea0b889248fa3`.

The reproducibility procedure is:

1. clone the exact commit in two clean environments;
2. install from the lock file with the pinned `uv` version in CI;
3. run `make check`;
4. hash each generated artifact and compare the manifests.

The repository proves deterministic tests and manifests, plus two
byte-identical clean source archives for the evidence commit, as recorded in
`docs/V1_REPRODUCIBILITY.json`. This does not establish byte-identical package
builds for the current tree. Hosted package provenance attestations, final-tree
reproduction, and signing remain release-blocking.

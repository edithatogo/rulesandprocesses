# process-mappings cutover synchronization submission

Status: prepared; not submitted or applied to the destination repository.

## Destination

- Repository: `https://github.com/edithatogo/process-mappings`
- Required base commit: `d0257c1a99068262ea257643f3d6bdb57f2baee6`
- Parent source commit: `cac2d3c6660b2b8c848c13038189f33c26fe0a2c`
- Destination issue: `edithatogo/process-mappings#1`
- Parent issue: `edithatogo/rac-conformance#50`

## Purpose

Synchronize the destination with newer parent artifacts created after staged
extraction. The twelve files under `cutover-sync/` are destination-relative
replacements or additions. Their expected digests and prior destination state
are pinned in `CUTOVER_SYNC_MANIFEST.json`.

This synchronization must land and pass the destination standalone check before
the parent can become a read-only consumer. It does not itself make the
destination canonical.

## Application contract

1. Create a destination branch from the required base commit.
2. Verify every non-null `beforeSha256` in the manifest. Stop on mismatch.
3. Copy each `cutover-sync/<path>` file to `<path>` in the destination.
4. Run `python3 tools/verify_standalone.py` and hosted `Standalone check`.
5. Merge through the protected branch and record the immutable merge commit.
6. Update destination issue #1 with the merge commit and check run.
7. Then prepare the separate parent cutover that repoints consumers and
   replaces `subrepos/process-mappings/` with a read-only provenance reference.

## Boundaries

- No candidate fixture or source assertion is promoted.
- Health-technology assertions remain agent-proposed and non-controlling.
- No legal, clinical, funding, access, or equivalence conclusion is certified.
- The parent remains the canonical writable source until both transactions are
  reviewed and merged.
- Repository rules prohibit this agent from pushing this cross-repository
  submission directly.


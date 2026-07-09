# Spec: foi-o oia_rules process wiring

## Goal
Process pipeline and default CLI clock dispatch through pure oia_rules deadline functions.

## Acceptance
- normalise LegalClock uses oia_rules calculation method
- DeadlineCalculated carries oia_rules_dispatch quality flag
- CLI clock defaults to rules path; custom flags keep dates helper
- Tests green; merged to foi-o main

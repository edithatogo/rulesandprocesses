# FOI-O Candidate Review

This is an `agent-proposed` compatibility candidate, not a certified FOI-O
profile and not a legal interpretation. It is derived from the staged FOI-O
rules design, source notes, PIC artifacts, and the pinned FOI-O integration
evidence under `external/foi-o/`.

| FOI-O / process concept | PIC process-profile representation | Status |
| --- | --- | --- |
| request receipt | observed `RequestReceived` event and initial state | candidate |
| transfer assessment/notification | executed `TransferNotified` event and transition | candidate |
| extension assessment/notification | executed `ExtensionNotified` event and transition | candidate |
| refusal / deemed refusal signal | refusal event and reviewable terminal transition | candidate |
| reviewability | derived `ReviewableOutcome` event | candidate |

`foi-o` remains authoritative for FOI semantics and `foi-process` remains the
execution/evidence source. Candidate promotion needs human review of the
source assertions, event identity choices, and every loss note.

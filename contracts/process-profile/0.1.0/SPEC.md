# PIC Process Profile 0.1.0

Status: draft normative contract  
Conforms to: `pic-process-profile/0.1.0`

## Lifecycle semantics

The profile describes a process instance as a versioned definition, synthetic
or permitted case, states, events, transitions, actors, optional timers,
human tasks, rule invocations, source assertions, and trace links.

- An `observed` event records that an observation occurred; it does not assert
  that the event was lawful, correct, or complete.
- A `derived` state or event records deterministic processing over declared
  inputs. It must remain distinguishable from observation.
- A `proposed` action or state is a candidate and cannot be treated as an
  executed or certified decision.
- A `certified_human` state or event requires an external human certification
  record; repository authors cannot self-certify it by changing JSON.
- An `executed` state or event records a reported execution outcome, not the
  authority for the rule that produced it.
- A transition links declared states and, when present, the event that caused
  the transition. Missing or dangling links are validation failures.
- A human task remains a human task even when a platform renders it as a job,
  form, or service call. The profile never converts a human task into a
  deterministic rule invocation.
- `occurredAt` and `observedAt` are distinct timestamps. A process comparison
  must not substitute one for the other.

Rule invocations link existing PIC decision and parameter identifiers, a
versioned PIC trace shape, and an authority assertion. They do not embed a
new expression language or redefine PIC semantics.

## Projection and loss

Projection into a service, workflow platform, engine trace, or FOI-O export is
non-normative. A projection MUST report:

1. source process-profile version and digest;
2. target format and adapter version;
3. identifiers preserved, renamed, or unavailable;
4. timestamp, human-task, authority, and source-assertion loss;
5. rejected or unsupported elements; and
6. the normalized trace reference produced on return, when available.

Lossless equivalence is never assumed from matching event counts or labels. A
projection that cannot preserve jurisdiction, effective date, authority,
reviewer state, or human/deterministic distinction must emit an explicit loss
or exception rather than silently flattening it.

## Safety and authority boundary

The contract is not a legal, clinical, regulatory, funding, or standards-body
authority. FOI-O remains authoritative for FOI semantics and jurisdiction
profiles. External engines and platforms remain adapters or evidence sources.
Controlling source assertions are subject to `AUTHORITY_MODEL.md`; agent-only
or secondary-only evidence cannot become a certified process decision.

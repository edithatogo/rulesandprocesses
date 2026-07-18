# Independent Implementer Kit

This directory is the sole canonical independent-validation kit. Copy it to a
clean environment; it does not import repository code or require private
services. Install Python and `jsonschema`, then run:

```text
python run_reference.py --output results.json
```

The bundled manifest pins every schema and corpus artifact by SHA-256. The
reference runner verifies those digests before executing all valid and invalid
cases. Its output is a structural rehearsal only and cannot satisfy the v1
independence gate.

An external implementer must use independently controlled code, fixtures,
oracle, repository, and execution infrastructure. Submit evidence against the
schema and policy identified in the parent `independent/` directory.

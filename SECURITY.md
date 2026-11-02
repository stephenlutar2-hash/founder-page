# Security Policy

> Doctrine v11 LOCKED · 749/14/163 · source snapshot `c7c0ba17c2eaec60ad38ea9172b4a0d9ca0b582f`

## Reporting a Vulnerability

Please report security vulnerabilities by email to **security@szlholdings.com**.

- We operate a **90-day coordinated disclosure window** from the date of acknowledgement.
- Please do not open public issues for security reports.
- We will acknowledge receipt within 2 business days.
- For sensitive reports, request the current encryption key in the first message.

## Supported Versions

The latest revision on the default branch is supported. Older revisions are best-effort.

## Verification boundary

This repository publishes a static GitHub Pages site. Reviewers can bind the rendered source to a commit on [`main`](https://github.com/stephenlutar2-hash/founder-page/commits/main) and inspect the corresponding [Pages workflow](https://github.com/stephenlutar2-hash/founder-page/actions/workflows/pages/pages-build-deployment). The current workflows also generate an SPDX SBOM artifact and maintain an `attestations` branch.

No signed release bundle is asserted for this repository. An SBOM describes the scanned files; by itself it does not prove build provenance, deployment identity, or runtime behavior.

## Organization policy

See the [SZL Holdings security policy](https://github.com/szl-holdings/.github/security/policy).

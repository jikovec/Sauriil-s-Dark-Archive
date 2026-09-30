# Security Policy

This repository contains asset-processing tools plus opt-in Windows and Linux apply/rollback scripts. Treat live OS modification paths as security-sensitive.

## Reporting a vulnerability

Do not post secrets, exploit details, private machine data, or other sensitive reproduction material in a public Issue.

This repository currently publishes no dedicated private security-reporting contact. Owner decision [#11](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/11) tracks establishment of a private reporting route. Until that route exists, use public Issues only for non-sensitive hardening reports that can be discussed safely in public.

A useful report should identify the affected path/version or revision, prerequisites, minimal reproduction steps, observed impact, and any evidence needed to reproduce the issue without exposing credentials or private data.

## Current security boundary

- Normal asset conversion, documentation, and proof work must not require live OS changes.
- Windows and Linux apply/rollback commands require explicit user authorization for each live-changing task.
- The presence of an `-Apply` or `--apply` gate is not proof that the operation is safe. Current implementation gaps are tracked in [#1](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/1) and its child issues.
- Release archives under `VERSIONS/` are protected distribution/history artifacts. Do not rewrite them as part of routine security or maintenance work.
- Never commit credentials, private keys, tokens, `.env` contents, private URLs, account identifiers, or private machine state.

## Supported versions

No security-support matrix or response-time commitment is currently published. Do not infer support for historical archives from their presence in `VERSIONS/`.

## Disclosure and bounty expectations

No vulnerability bounty, response-time SLA, or coordinated-disclosure timetable is promised by this repository. Owner-approved policy changes belong in this file once established.

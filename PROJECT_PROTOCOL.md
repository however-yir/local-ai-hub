# Local AI Hub Project Protocol

## 1. Scope

This protocol applies to the customized fork named **Local AI Hub** and defines collaboration, deployment, and branding rules for this repository.

## 2. Intended Usage

- Internal productivity and private deployment.
- Team knowledge management and local model orchestration.
- Education, experimentation, and workflow automation.

## 3. Security Baseline

- Do not commit real API keys, database passwords, or tokens.
- Production deployment must use `.env.production` with strong secrets.
- Public exposure requires strict `CORS_ALLOW_ORIGIN` and HTTPS reverse proxy.

## 4. Data Responsibility

- Users are responsible for model output review and compliance checks.
- Sensitive data should be processed in isolated runtime and encrypted storage.
- Regular database and file backups are mandatory for production.

## 5. Branding Rules

- Project display name: **Local AI Hub**.
- Repository metadata should follow `.github/settings.yml`.
- New UI assets should use the `brand-*` naming convention.

## 6. Fork Maintenance

- Upstream sync should happen through reviewed merge commits.
- Breaking configuration changes must update all env example files.
- README and deployment docs must be kept in sync with runtime behavior.

## 7. Compatibility Promise

- Preserve backward compatibility for existing `open-webui` CLI entry where feasible.
- New entrypoint is `local-ai-hub` for project-level identity.

## 8. Contribution Policy

- Major architectural changes require a short design note in PR description.
- New dependencies must include rationale and rollback considerations.
- Keep commit scope small and production-safe.

## 9. License Notice

This protocol is supplemental and does not replace upstream license obligations.
Please review `LICENSE` and `LICENSE_HISTORY` before distribution.

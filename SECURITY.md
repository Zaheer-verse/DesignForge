# Security Policy

DesignForge is an AI skill and documentation repository. It should not contain secrets, credentials, private keys, customer data, or environment-specific authentication files.

## Supported Versions

Security updates apply to the current `main` branch and the latest published release, if releases are used.

## Reporting a Vulnerability

If you find a security issue, open a private security advisory on GitHub if the repository has advisories enabled. If advisories are unavailable, contact the repository maintainers through the repository owner's preferred public contact method.

Please include:

- A clear description of the issue
- Affected files or instructions
- Potential impact
- Suggested remediation, if known

Do not publish working exploit details or real credentials in a public issue.

## Secret Handling

Never commit:

- API keys or access tokens
- OAuth client secrets
- Passwords
- Private keys
- `.env` files
- Local credential stores
- Private customer or project data

Run the repository validator before publishing:

```bash
python scripts/validate_repository.py
```

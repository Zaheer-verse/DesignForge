# Changelog

All notable changes to DesignForge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project uses semantic versioning when releases are published.

## Unreleased

No unreleased changes yet.

## 1.0.0 - 2026-09-02

### Added

- Initial DesignForge skill in `SKILL.md`.
- Professional README with installation, usage, architecture, validation, troubleshooting, roadmap, and contribution guidance.
- Public GitHub repository metadata and README badges for CI and license.
- Documentation hierarchy under `docs/` for quickstart, installation, usage, validation, architecture, skill reference, and troubleshooting.
- Reference guides for design principles, typography, color, layout, animation, 3D, accessibility, responsive design, page patterns, anti-patterns, and quality checks.
- Templates for page specifications and design reviews.
- Realistic examples for landing pages, dashboards, AI app interfaces, and e-commerce product pages.
- Repository validation script at `scripts/validate_repository.py`.
- Unittest wrapper for repository validation.
- GitHub Actions workflow that runs validation and tests.
- Issue templates and pull request template.
- Community files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`.
- MIT License.
- `.gitignore` covering common temporary files, build outputs, and secret-bearing local files.
- `.gitattributes` for consistent text normalization.

### Changed

- Documented DesignForge as a skill corpus rather than an installable package or UI kit.
- Clarified that qualitative AI skill behavior requires scenario-based review in addition to repository checks.

### Fixed

- Removed placeholder GitHub URLs from documentation.
- Removed references to examples and reference files that were not present.
- Avoided fake badges, fake metrics, and invented repository metadata.

### Security

- Added security reporting guidance.
- Added repository checks for secret-like files and high-risk secret patterns.
- Added ignore rules for local environment and credential files.

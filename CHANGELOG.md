# Changelog

جميع التغييرات المهمة في هذا المشروع سيتم توثيقها في هذا الملف.

يتبع هذا المشروع مبادئ [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
ونظام الإصدارات [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- تهيئة الهيكل الكامل لمنصة **Moon** للاستخبارات والتحقيقات الرقمية (OSINT / Intelligence Platform).
- طبقات المنصة الأساسية: `core`, `platform`, `intelligence`, `collectors`, `analyzers`, `graph`, `knowledge`.
- طبقة الحوكمة والمعايير: `governance/`, `standards/`, `architecture/`.
- طبقة الوكلاء والقدرات: `agents/`, `capabilities/`, `workflows/`, `contracts/`.
- طبقة البنية التحتية والأمان: `security/`, `observability/`, `infrastructure/`.
- طبقة التطبيقات: `apps/api`, `apps/web`, `apps/worker`, `apps/cli`, `apps/admin`.
- إعدادات المشروع: `pyproject.toml`, `package.json`, `nx.json`, `docker-compose*.yml`.
- أدوات الجودة: `.pre-commit-config.yaml`, `.importlinter`, `Makefile`.

## [0.1.0] - 2026-07-15

### Added
- الإصدار الأولي لهيكل المستودع (scaffold) بدون منطق تنفيذي فعلي — كل الوحدات
  عبارة عن نقاط بداية (`TODO`) جاهزة للتطوير التدريجي وفق خارطة الطريق في
  `ROADMAP.md`.

[Unreleased]: https://github.com/OWNER/moon/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/OWNER/moon/releases/tag/v0.1.0

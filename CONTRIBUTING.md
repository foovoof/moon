# دليل المساهمة — Contributing to Moon

شكرًا لاهتمامك بالمساهمة في **Moon**، منصة الاستخبارات والتحقيقات الرقمية
مفتوحة الهيكلية. هذا الدليل يوضح كيفية المساهمة بشكل فعّال ومتوافق مع
حوكمة المشروع.

## قبل أن تبدأ

1. اقرأ [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).
2. اقرأ [`ARCHITECTURE.md`](./ARCHITECTURE.md) و [`GOVERNANCE.md`](./GOVERNANCE.md)
   لفهم طبقات النظام وحدود كل طبقة (dependency rules في `architecture/dependency-rules/`).
3. راجع [`STANDARDS.md`](./STANDARDS.md) لمعايير التسمية والبيانات المعتمدة.
4. تحقق من [`ROADMAP.md`](./ROADMAP.md) لمعرفة الأولويات الحالية.

## هيكل الطبقات (لا تُخالف اتجاه الاعتمادية)

```
governance/ standards/  →  core/ normalizers/  →  platform/
        →  collectors/ analyzers/ graph/ knowledge/
        →  intelligence/ agents/ tools/ processors/ connectors/
        →  domain/ contracts/ capabilities/ workflows/
        →  apps/ (api, web, worker, cli, admin)
```

- الطبقات العليا يمكنها الاعتماد على الطبقات الأدنى، والعكس غير مسموح.
- يتم فرض هذه القاعدة عبر `.importlinter` و `tests/architecture/`.

## سير عمل المساهمة

1. **Fork / Branch**: أنشئ فرعًا من `main` باسم واضح: `feat/...`, `fix/...`, `docs/...`.
2. **Install**:
   ```bash
   make setup        # يهيئ بيئة بايثون + Node
   ```
3. **التطوير**: اكتب الكود مع اختبارات مقابلة في `tests/unit/` أو `tests/integration/`.
4. **الجودة محليًا**:
   ```bash
   make lint
   make format
   make test
   pre-commit run --all-files
   ```
5. **Commit**: اتبع [Conventional Commits](https://www.conventionalcommits.org/):
   `feat(collectors): add telegram collector rate limiting`
6. **Pull Request**: استخدم القالب في `.github/PULL_REQUEST_TEMPLATE.md`، واربط
   أي Issue متعلق، واذكر أي تغيير في الـ contracts أو الـ schemas.
7. **المراجعة**: يجب موافقة مراجع واحد على الأقل + نجاح CI (`.github/workflows/`).

## قواعد إضافة الموصلات (Connectors) والمُجمّعات (Collectors)

- كل مصدر بيانات جديد يجب أن يرث من `collectors/base_collector.py` أو
  `connectors/` المناسب، ويُسجَّل في `collectors/collector_factory.py`.
- يجب توثيق أي سياسة استخدام/حدود قانونية للمصدر في `governance/legal/`.
- لا تُضِف مفاتيح API أو أسرارًا في الكود؛ استخدم `security/secrets/` و `.env.example`.

## الإبلاغ عن ثغرات أمنية

لا تفتح Issue علنية للثغرات الأمنية — راجع [`SECURITY.md`](./SECURITY.md).

## الترخيص

بمساهمتك، أنت توافق على ترخيص عملك تحت [`LICENSE`](./LICENSE) (MIT).

# 🌙 Moon — منصة الاستخبارات والتحقيقات الرقمية

**Moon** هي بنية معمارية معيارية (scaffold) كاملة لمنصة استخبارات مفتوحة
المصدر وتحقيقات رقمية (**OSINT / Intelligence & Investigation Platform**)،
مصمّمة على شكل طبقات صريحة الاعتمادية تشمل: الجمع (Collection)، التحليل
(Analysis)، الرسم البياني للمعرفة (Knowledge Graph)، الوكلاء (Agents)،
الحوكمة (Governance)، والأمان (Security).

> ⚠️ هذا مستودع **هيكلي (scaffold)** بالكامل: جميع الوحدات نقاط بداية
> جاهزة للتطوير (`TODO` صريحة) وفق خارطة الطريق في [`ROADMAP.md`](./ROADMAP.md).
> لا يحتوي حاليًا منطقًا تنفيذيًا فعليًا للجمع الآلي للبيانات.

## المحتوى

- [البنية المعمارية](#البنية-المعمارية)
- [الميزات المكتملة حاليًا](#الميزات-المكتملة-حاليًا)
- [نقاط الدخول والروابط](#نقاط-الدخول-والروابط)
- [نموذج البيانات والتخزين](#نموذج-البيانات-والتخزين)
- [دليل الاستخدام السريع](#دليل-الاستخدام-السريع)
- [الميزات غير المكتملة والخطوات القادمة](#الميزات-غير-المكتملة-والخطوات-القادمة)
- [النشر](#النشر)
- [الوثائق الأساسية](#الوثائق-الأساسية)

## البنية المعمارية

راجع [`ARCHITECTURE.md`](./ARCHITECTURE.md) للتفصيل الكامل. ملخص الطبقات:

```
governance/ standards/ security/ policy_engine/   ← حوكمة ومعايير (أفقية)
core/ normalizers/ domain/ models/ utils/          ← نواة مشتركة
platform/ (kernel, orchestration, events)          ← منصة التشغيل
collectors/ analyzers/ graph/ knowledge/            ← الجمع والتحليل والمعرفة
intelligence/ agents/ tools/ processors/ connectors/ ← منطق الاستخبارات
workflows/ capabilities/ contracts/                 ← التنسيق والعقود
apps/ (api, web, worker, cli, admin)                ← نقاط الدخول
```

## الميزات المكتملة حاليًا

- ✅ الهيكل الكامل لجميع الطبقات (~60 مجلدًا رئيسيًا وفرعيًا) مطابق للمخطط
  المعتمد، بما فيه الإضافات: `retention_policy.yaml`, `audit_policy.yaml`,
  دور `auditor`, `identifier_normalizer.py`, موصلات اجتماعية إضافية
  (Instagram, TikTok, Reddit, Discord).
- ✅ وثائق حوكمة كاملة: [`GOVERNANCE.md`](./GOVERNANCE.md),
  [`STANDARDS.md`](./STANDARDS.md), [`ARCHITECTURE.md`](./ARCHITECTURE.md),
  [`ROADMAP.md`](./ROADMAP.md)، وأدوار مفصّلة في `governance/roles/`.
  (Analyst, Investigator, Admin, Auditor).
- ✅ قاموس بيانات مبدئي في `standards/data_dictionary/` لـ 10 كيانات مجال.
- ✅ عقود ونماذج بايثون أولية (placeholders موثّقة) في `core/`, `domain/`,
  `models/`, `normalizers/`, `collectors/`, `analyzers/`, `graph/`,
  `knowledge/`, `connectors/`, `security/secrets/`, `apps/api/`, `utils/`.
- ✅ إعداد أدوات الجودة: `pyproject.toml`, `.pre-commit-config.yaml`,
  `.importlinter` (فرض قواعد الاعتمادية بين الطبقات), `Makefile`.
- ✅ بيئة تشغيل محلية: `docker-compose.yml` / `docker-compose.dev.yml`
  (Postgres, Redis, Neo4j) + `.env.example`.
- ✅ تطبيق حافة (Edge) قائم بذاته يعمل فعليًا: Hono + Cloudflare
  Pages/Workers في `src/index.tsx` (نقطة انطلاق واجهة `apps/web` و
  `apps/api` المستقبلية).

## نقاط الدخول والروابط

| النوع | القيمة |
|-------|--------|
| تطبيق الحافة (Hono) — تطوير محلي | `http://localhost:3000` (عبر `npm run dev:sandbox`) |
| API خلفي (Python/FastAPI مخطط) | `apps/api/` — غير مُفعّل بعد (انظر Roadmap) |
| GitHub | `https://github.com/<OWNER>/moon` |

> لا يوجد رابط نشر إنتاجي عام حتى الآن — هذا مستودع هيكلي أولي.

## نموذج البيانات والتخزين

- **المصدر الرسمي للحقيقة**: `standards/data_dictionary/` (identity,
  entity, relationship, evidence, source, finding, report, investigation,
  workflow, event).
- **نماذج المجال**: `domain/*.py` (Case, Investigation, Evidence, Finding,
  Timeline, Report, ChainOfCustody, ConfidenceScore, ClassificationLevel...).
- **التخزين المخطط**:
  - PostgreSQL — بيانات علائقية للحالات/التحقيقات (`data/database/`).
  - Neo4j / NetworkX — الرسم البياني للكيانات والعلاقات (`graph/connectors/`).
  - Redis — كاش وطوابير المهام (`collectors/infrastructure/cache_manager.py`).
  - Cloudflare D1 / KV / R2 — عند استخدام واجهة الحافة لتخزين بيانات خفيفة
    أو ملفات (أدلة، تقارير) عبر `apps/api`.

## دليل الاستخدام السريع

### تطبيق الحافة (Hono / Cloudflare) — جاهز للتشغيل الآن

```bash
npm install
npm run build
npm run dev:sandbox   # يشغّل على المنفذ 3000
```

### النواة البرمجية (Python) — هيكل جاهز للتطوير

```bash
make setup-py     # تثبيت pyproject.toml[dev] + pre-commit
make test         # تشغيل pytest
make lint          # ruff + import-linter
```

### الخدمات المساعدة (Postgres / Redis / Neo4j)

```bash
cp .env.example .env   # ثم عدّل القيم
make docker-up
```

## الميزات غير المكتملة والخطوات القادمة

راجع [`ROADMAP.md`](./ROADMAP.md) للتفصيل الكامل عبر 7 مراحل. أبرز ما لم
يُنفَّذ بعد:

- ❌ منطق فعلي داخل `collectors/`, `analyzers/`, `graph/`, `knowledge/`
  (حاليًا placeholders موثّقة ترفع `NotImplementedError`).
- ❌ تفعيل `platform/orchestration/` وتشغيل أول وكيل حقيقي.
- ❌ تفعيل `security/authentication/` و `security/authorization/` (RBAC).
- ❌ ربط `apps/api` الفعلي (FastAPI) وتوصيله بواجهة `apps/web`.
- ❌ CI/CD كامل في `.github/workflows/`.

## النشر

- **تطبيق الحافة**: يُنشر عبر Cloudflare Pages (Wrangler) — راجع تعليمات
  النشر في قسم "Deployment" ضمن أدوات المشروع عند تنفيذ `npm run deploy`.
- **الخدمات الخلفية (Python)**: مخطط للنشر عبر `infrastructure/docker/`
  و `infrastructure/kubernetes/` أو `infrastructure/terraform/` (لم تُنفَّذ بعد).

## الوثائق الأساسية

| الملف | المحتوى |
|-------|---------|
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | الطبقات، الاعتماديات، المكدس التقني |
| [`GOVERNANCE.md`](./GOVERNANCE.md) | الأدوار، صناعة القرار، السياسات |
| [`STANDARDS.md`](./STANDARDS.md) | معايير التسمية وقاموس البيانات |
| [`ROADMAP.md`](./ROADMAP.md) | خارطة الطريق التفصيلية على 7 مراحل |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | سير عمل المساهمة الكامل |
| [`SECURITY.md`](./SECURITY.md) | سياسة الأمان والإبلاغ عن الثغرات |
| [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) | ميثاق قواعد السلوك |
| [`CHANGELOG.md`](./CHANGELOG.md) | سجل التغييرات |

---

### ملاحظة تقنية لتطبيق الحافة (Hono)

```bash
npm install
npm run dev
```

```bash
npm run deploy
```

[توليد/مزامنة الأنواع بناءً على تهيئة Worker](https://developers.cloudflare.com/workers/wrangler/commands/#types):

```bash
npm run cf-typegen
```

مرّر `CloudflareBindings` كـ generics عند إنشاء نسخة `Hono`:

```ts
// src/index.tsx
const app = new Hono<{ Bindings: CloudflareBindings }>()
```

## الترخيص

[MIT](./LICENSE) — راجع أيضًا ملاحظة الاستخدام المسؤول في نهاية ملف الترخيص.

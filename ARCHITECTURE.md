# البنية المعمارية — Architecture

## نظرة عامة

**Moon** منصة معيارية (modular) للاستخبارات مفتوحة المصدر والتحقيقات
الرقمية (OSINT / Digital Investigation Intelligence Platform)، مصمّمة
على شكل طبقات صريحة الاعتمادية (layered architecture) مع فرض القواعد
آليًا عبر `.importlinter` و `tests/architecture/`.

## مخطط الطبقات (من الأسفل إلى الأعلى)

```
┌─────────────────────────────────────────────────────────────┐
│  apps/            (api, web, worker, cli, admin)             │  ← نقاط الدخول
├─────────────────────────────────────────────────────────────┤
│  workflows/  capabilities/  contracts/  agents/  tools/      │  ← التنسيق والعقود
├─────────────────────────────────────────────────────────────┤
│  intelligence/  processors/  connectors/                     │  ← منطق الأعمال العالي
├─────────────────────────────────────────────────────────────┤
│  collectors/  analyzers/  graph/  knowledge/                 │  ← الجمع والتحليل والمعرفة
├─────────────────────────────────────────────────────────────┤
│  platform/  (kernel, orchestration, events)                  │  ← منصة التشغيل
├─────────────────────────────────────────────────────────────┤
│  core/  normalizers/  domain/  models/  utils/                │  ← النواة المشتركة
├─────────────────────────────────────────────────────────────┤
│  governance/  standards/  security/  policy_engine/           │  ← الحوكمة والمعايير (شفافة للجميع)
└─────────────────────────────────────────────────────────────┘
```

**القاعدة الذهبية**: أي طبقة يمكنها الاستيراد من الطبقات الأدنى منها فقط،
عدا `governance/`, `standards/`, `security/`, `policy_engine/` التي تُعتبر
طبقة أفقية (cross-cutting) يمكن لأي طبقة الرجوع إليها للقراءة فقط.

## الوحدات الرئيسية

| الطبقة | الغرض |
|--------|-------|
| `core/` | الأنواع الأساسية، البطاقات (Cards)، السجل (Registry)، محلل الهوية |
| `normalizers/` | توحيد صيغ البيانات الخام (هاتف/بريد/اسم/تاريخ/عنوان/معرّف) |
| `platform/` | نواة التشغيل: kernel, orchestration, events (event-driven) |
| `intelligence/` | منطق الاستخبارات العالي: research, osint, correlation, attribution |
| `collectors/` | جمع البيانات من مصادر متعددة (شبكات اجتماعية، دارك ويب، تسريبات...) |
| `analyzers/` | تحليل النصوص/الشبكات/الصور/السلوك/المخاطر |
| `graph/` | نموذج الرسم البياني للكيانات والعلاقات + موصلات Neo4j/NetworkX |
| `knowledge/` | حل الهوية (entity resolution)، الربط، الاستدلال |
| `agents/` | وكلاء مستقلون قابلون للتوصيف عبر `agents/registry/` |
| `tools/` | أدوات قابلة لإعادة الاستخدام يستدعيها الوكلاء |
| `domain/` | نماذج المجال الأساسية (Case, Investigation, Evidence, Report...) |
| `contracts/` | عقود الواجهات بين الوحدات (DTOs, event schemas, service interfaces) |
| `workflows/` + `capabilities/` | تعريف تدفقات العمل والقدرات القابلة للتركيب |
| `security/` + `policy_engine/` | الهوية، التفويض، الأسرار، فرض السياسات برمجيًا |
| `observability/` | السجلات، المقاييس، التتبع، التنبيه، لوحات القيادة |
| `apps/` | نقاط الدخول: REST API (Hono/FastAPI)، واجهة الويب، عامل الخلفية، CLI |

## قرارات معمارية (ADR)

كل قرار معماري مهم (اختيار قاعدة بيانات الرسم البياني، اختيار إطار الـ API،
استراتيجية الأحداث...) يُوثَّق كسجل قرار في `architecture/adr/` باستخدام
قالب موحّد (السياق → القرار → البدائل → العواقب).

## نموذج البيانات المرجعي

راجع `standards/data_dictionary/` للحصول على التعريف الدقيق لكل كيان مجال
(identity, entity, relationship, evidence, source, finding, report,
investigation, workflow, event) بما يشمل الحقول والعلاقات ودورة الحياة.

## المكدس التقني المقترح (قابل للتغيير عبر ADR)

- **الخلفية الأساسية (منطق الاستخبارات/الوكلاء)**: Python (`pyproject.toml`).
- **واجهة API خفيفة الوزن للحافة (Edge)**: Hono + TypeScript على Cloudflare
  Workers/Pages، مناسبة لواجهات خفيفة وSSR سريع (`apps/api`, `apps/web`).
- **تنسيق الأحاديث بين المكوّنات (Monorepo)**: Nx (`nx.json`) لتنسيق أوامر
  البناء/الفحص بين حزم Python وNode.
- **التطوير المحلي**: Docker Compose (`docker-compose.yml` / `.dev.yml`)
  لتشغيل قواعد البيانات/الخدمات المساعدة (Neo4j, Redis, Postgres...).

## اختبار البنية

`tests/architecture/` يحتوي اختبارات تتحقق من:
- عدم وجود استيراد عكسي بين الطبقات (مطابقة لـ `.importlinter`).
- توافق كل وحدة جديدة مع اتفاقية التسمية في `STANDARDS.md`.

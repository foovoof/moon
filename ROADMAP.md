# خارطة الطريق — Roadmap

هذا المستند يوضح مراحل تطور منصة **Moon** من هيكل أولي (scaffold) إلى منصة
استخباراتية وتحقيقية جاهزة للإنتاج.

## المرحلة 0 — الأساس (Foundations) ✅ الحالية

- [x] إنشاء الهيكل الكامل للمستودع (جميع الطبقات والمجلدات).
- [x] وثائق الحوكمة الأساسية (`governance/`, `GOVERNANCE.md`, `STANDARDS.md`).
- [x] عقود ونماذج بيانات مبدئية (`domain/`, `contracts/`, `standards/data_dictionary/`).
- [x] إعداد أدوات الجودة (`pre-commit`, `.importlinter`, `Makefile`).
- [ ] CI/CD أساسي يعمل بنجاح على `main` (`.github/workflows/`).

## المرحلة 1 — النواة والمعايير (Core & Standards)

- [ ] تنفيذ `core/types.py`, `core/card.py`, `core/registry.py`, `core/resolver.py`.
- [ ] تنفيذ طبقة `normalizers/` بالكامل (هاتف، بريد، اسم، تاريخ، عنوان، معرّف).
- [ ] تثبيت `standards/ontology/` و `standards/taxonomy/` بمخطط رسمي (JSON Schema/YAML).
- [ ] اختبارات وحدة كاملة لـ `tests/unit/core/` و `tests/unit/normalizers/`.

## المرحلة 2 — الجمع والتحليل (Collection & Analysis)

- [ ] تنفيذ `collectors/base_collector.py` و `collector_factory.py`.
- [ ] تفعيل 3-5 مُجمّعات أولية (phone, email, domain, ip, social_media).
- [ ] طبقة النقل `collectors/transport/` (api/scrape/selenium fetchers) مع
      `rate_limiter`, `retry_handler`, `circuit_breaker`.
- [ ] محلّلات أولية: `analyzers/text/`, `analyzers/network/`.

## المرحلة 3 — المعرفة والرسم البياني (Knowledge & Graph)

- [ ] تنفيذ `graph/graph_manager.py` مع موصل `networkx` (تطوير) و `neo4j` (إنتاج).
- [ ] تنفيذ `knowledge/resolution/entity_resolution.py`.
- [ ] استعلامات الرسم البياني: `shortest_path`, `community_detection`.

## المرحلة 4 — الوكلاء والتنسيق (Agents & Orchestration)

- [ ] تنفيذ `platform/orchestration/` (planner/executor/state).
- [ ] أول وكيل بحث فعلي في `agents/research/` مسجّل في `agents/registry/agents.yaml`.
- [ ] تفعيل `workflows/research.yaml` end-to-end.

## المرحلة 5 — الأمان والامتثال (Security & Compliance)

- [ ] تنفيذ `security/authentication/` و `security/authorization/` (RBAC حسب
      `governance/roles/`).
- [ ] تنفيذ `policy_engine/` لفرض `governance/policies/*.yaml` برمجيًا.
- [ ] تدقيق كامل (`security/audit/`, `observability/audit_telemetry/`).

## المرحلة 6 — التطبيقات والواجهات (Apps)

- [ ] `apps/api` جاهز للإنتاج (FastAPI/Hono حسب القرار النهائي في `ARCHITECTURE.md`).
- [ ] `apps/web` لوحة تحقيقات تفاعلية.
- [ ] `apps/cli` لإدارة الحالات من سطر الأوامر.

## المرحلة 7 — النضج التشغيلي (Operational Maturity)

- [ ] `infrastructure/kubernetes/` و `infrastructure/terraform/` جاهزة للنشر.
- [ ] `observability/dashboards/` + `runbooks/` كاملة.
- [ ] `benchmarks/` مع تقارير دورية في `benchmarks/reports/`.
- [ ] SDKs منشورة (`sdk/python`, `sdk/javascript`).

> ملاحظة: هذه خارطة طريق مبدئية قابلة للتعديل حسب أولويات الفريق. أي تغيير
> جوهري في الأولويات يجب أن يُوثَّق في `architecture/adr/` كسجل قرار (ADR).

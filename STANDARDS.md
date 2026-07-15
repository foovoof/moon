# المعايير — Standards

يشير هذا الملف إلى مجلد `standards/` الذي يحتوي المصدر الرسمي (source of
truth) لكل تعريفات البيانات والمصطلحات في **Moon**. راجع
[`standards/README.md`](./standards/README.md) للتفصيل الكامل.

## نظرة سريعة على المحتوى

| المجلد | الغرض |
|--------|-------|
| `standards/ontology/` | الأنطولوجيا المفاهيمية للكيانات والعلاقات |
| `standards/taxonomy/` | التصنيفات الهرمية (تصنيف مصادر، تصنيف مخاطر...) |
| `standards/concepts/` | تعريفات المفاهيم المجردة المشتركة |
| `standards/entities/` | أنواع الكيانات المعتمدة (شخص، منظمة، جهاز، حساب...) |
| `standards/relationships/` | أنواع العلاقات المعتمدة بين الكيانات |
| `standards/confidence/` | نموذج درجات الثقة (Confidence Scoring) الموحّد |
| `standards/evidence/` | معايير توثيق الأدلة وسلسلة الحفظ |
| `standards/lifecycle/` | دورة حياة الحالة/التحقيق/الدليل |
| `standards/classifications/` | مستويات التصنيف الأمني للمعلومات |
| `standards/metadata/` | حقول البيانات الوصفية الموحّدة عبر كل الوحدات |
| `standards/events/` | كتالوج الأحداث، قواعد التسمية، إصدار الأحداث |
| `standards/data_dictionary/` | قاموس البيانات التفصيلي لكل كيان مجال |

## قواعد التسمية العامة (Naming Conventions)

- **ملفات بايثون**: `snake_case.py`.
- **الفئات (Classes)**: `PascalCase`.
- **الدوال والمتغيرات**: `snake_case`.
- **ملفات YAML/JSON للتهيئة**: `snake_case.yaml` / `snake_case.json`.
- **الأحداث** (`standards/events/catalog.yaml`): `domain.entity.action`
  مثال: `investigation.case.created`, `collector.source.fetched`.
- **الإصدارات (Versioning)**: [SemVer](https://semver.org/) لكل حزمة
  منشورة، وإصدار مستقل للأحداث في `standards/events/event_versioning.yaml`.

## مبدأ المصدر الواحد للحقيقة (Single Source of Truth)

- أي حقل بيانات مُستخدم في أكثر من وحدة **يجب** أن يكون معرَّفًا أولاً في
  `standards/data_dictionary/` قبل استخدامه في `domain/` أو `contracts/`.
- أي تغيير على تعريف موجود يتطلب تحديث كل من: `standards/data_dictionary/`,
  `domain/`, `contracts/dto/`, و اختبارات `tests/contract/`.

## الامتثال للمعايير

يتم فرض هذه المعايير جزئيًا آليًا عبر:
- `tests/contract/` — التحقق من تطابق العقود مع قاموس البيانات.
- `tests/architecture/` — التحقق من قواعد الاعتمادية بين الطبقات.
- `.pre-commit-config.yaml` — فحص التنسيق والتسمية قبل كل commit.

# الدور: المشرف (Admin)

## الملخص

المشرف مسؤول عن إدارة النظام ككل: البنية التحتية (`infrastructure/`)،
الصلاحيات والمستخدمين (`security/authorization/`)، وتسجيل الوكلاء
والقدرات الجديدة (`agents/registry/`, `capabilities/`).

## الصلاحيات

- الإدارة الكاملة لحسابات المستخدمين والأدوار (RBAC وفق
  `security/authorization/` و `governance/roles/`).
- تسجيل/تعطيل الوكلاء (`agents/`) والموصلات (`connectors/`) والمُجمّعات
  (`collectors/`) الجديدة عبر السجل المركزي (`agents/registry/agents.yaml`).
- إدارة الأسرار ومفاتيح API عبر `security/secrets/manager.py`.
- الوصول الكامل لسجلات المراقبة (`observability/`) ولوحات القيادة.
- تنفيذ عمليات الاسترجاع/النشر عبر `infrastructure/deployment/`.

## المسؤوليات

- تطبيق `governance/policies/*.yaml` تقنيًا عبر `policy_engine/`.
- مراقبة صحة النظام (`platform/kernel/health/`) والاستجابة للحوادث وفق
  `observability/runbooks/`.
- ضمان تدوير الأسرار وعدم تسريبها (`SECURITY.md`).
- الموافقة على أي طلب توسيع صلاحيات لدور آخر.

## القيود

- **لا يجوز** للمشرف الوصول لمحتوى الحالات/التحقيقات دون سبب تشغيلي
  موثّق (يُسجَّل الوصول في `security/audit/`).
- لا يجوز تعديل سياسات الحوكمة (`governance/policies/`) من جانب واحد —
  يتطلب مراجعة فريق الحوكمة (`GOVERNANCE.md`).
- كل عملية إدارية حساسة (حذف حالة، تعديل صلاحيات) تُسجَّل بشكل غير قابل
  للتلاعب في سجل التدقيق.

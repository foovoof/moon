## الوصف

<!-- اشرح بإيجاز ما يفعله هذا الـ PR ولماذا -->

## نوع التغيير

- [ ] إصلاح خلل (fix)
- [ ] ميزة جديدة (feat)
- [ ] تغيير كاسر (breaking change)
- [ ] توثيق فقط (docs)
- [ ] إعادة هيكلة بدون تغيير سلوك (refactor)
- [ ] تحديث بنية تحتية/أدوات (chore/ci)

## الطبقات المتأثرة

<!-- ضع علامة على كل الطبقات التي عدّلتها -->
- [ ] `core` / `normalizers` / `domain` / `models`
- [ ] `platform`
- [ ] `collectors` / `analyzers` / `graph` / `knowledge`
- [ ] `intelligence` / `agents` / `tools` / `processors` / `connectors`
- [ ] `workflows` / `contracts` / `capabilities`
- [ ] `security` / `policy_engine`
- [ ] `apps` (api / web / worker / cli / admin)
- [ ] `governance` / `standards` (يتطلب مراجعة إضافية)

## قائمة التحقق

- [ ] قرأت [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- [ ] الكود يتبع قواعد الاعتمادية بين الطبقات (`.importlinter`).
- [ ] أضفت/حدّثت الاختبارات المناسبة (`tests/unit` أو `tests/integration`).
- [ ] `make lint` و `make test` ينجحان محليًا.
- [ ] حدّثت الوثائق ذات الصلة (`README.md`, `docs/`, `standards/` عند الحاجة).
- [ ] لم أُضِف أي سر/مفتاح API في الكود.

## Issues مرتبطة

Closes #

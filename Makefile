.PHONY: setup setup-py setup-node dev build test lint format \
        migrate seed db-reset docker-up docker-down clean help

PYTHON ?= python3
PIP ?= pip3
NPM ?= npm

help: ## عرض هذه القائمة
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

setup: setup-py setup-node ## تهيئة بيئة بايثون و Node معًا
	@echo "✅ Moon setup complete."

setup-py: ## تثبيت اعتماديات بايثون + pre-commit hooks
	$(PIP) install -e ".[dev]"
	pre-commit install

setup-node: ## تثبيت اعتماديات Node (apps/api, apps/web على Cloudflare)
	$(NPM) install

dev: ## تشغيل خادم التطوير (Cloudflare Pages/Workers عبر Wrangler)
	fuser -k 3000/tcp 2>/dev/null || true
	$(NPM) run build
	$(NPM) run dev:sandbox

build: ## بناء تطبيق الحافة (apps/api, apps/web)
	$(NPM) run build

test: ## تشغيل كل الاختبارات (بايثون)
	pytest -q

test-cov: ## تشغيل الاختبارات مع تقرير التغطية
	pytest --cov --cov-report=term-missing

lint: ## فحص الجودة (ruff + import-linter)
	ruff check .
	lint-imports

format: ## إعادة تنسيق الكود (black + ruff --fix)
	black .
	ruff check --fix .

migrate: ## تطبيق ترحيلات قاعدة البيانات (D1/Postgres حسب البيئة)
	bash scripts/migrate.sh

seed: ## زرع بيانات تجريبية
	bash scripts/seed.sh

db-reset: ## إعادة تهيئة قاعدة البيانات المحلية بالكامل
	bash scripts/setup_db.py 2>/dev/null || $(PYTHON) scripts/setup_db.py

docker-up: ## تشغيل الخدمات المساعدة (Postgres/Redis/Neo4j) محليًا
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

docker-down: ## إيقاف الخدمات المساعدة
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down

clean: ## تنظيف ملفات البناء والكاش
	rm -rf dist .wrangler .pytest_cache .mypy_cache .ruff_cache
	find . -name "__pycache__" -not -path "./node_modules/*" -exec rm -rf {} +

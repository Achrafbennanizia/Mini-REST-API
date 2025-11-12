.PHONY: run test fmt

run:
	uvicorn app.main:app --reload

test:
	pytest -q

fmt:
	python -m pip install ruff
	ruff check --select I --fix .

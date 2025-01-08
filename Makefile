.DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8065

run:
	uvicorn main:app --host $(HOST) --port $(PORT) --reload

help:
	@echo "Usage: make [command]"

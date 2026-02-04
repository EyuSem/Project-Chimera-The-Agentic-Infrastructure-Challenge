setup:
	pip install pytest

test:
	pytest

docker-test:
	docker build -t chimera .
	docker run chimera

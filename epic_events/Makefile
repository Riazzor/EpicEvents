docker_psql:
	docker run --rm -p 5432:5432 -d \
		-e POSTGRES_PASSWORD=postgres \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_DB=epic_event_db \
		-v pgdata:/var/lib/postgresql/data \
		--name epic_event_db \
		postgres

shell:
	python3 manage.py shell_plus

run:
	python3 manage.py runserver

migrations :
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

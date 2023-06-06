docker_psql:
	docker run -p 5432:5432 -d \
		-e POSTGRES_PASSWORD=postgres \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_DB=epic_event_db \
		-v pgdata:/var/lib/postgresql/data \
		--name epic_event_db \
		postgres

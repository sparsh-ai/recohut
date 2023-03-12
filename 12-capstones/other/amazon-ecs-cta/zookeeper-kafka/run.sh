ecs-cli compose \
--project-name kafkazookeeper \
--file docker-compose.yml \
--debug service up \
--deployment-max-percent 100 \
--deployment-min-healthy-percent 0 \
--launch-type FARGATE
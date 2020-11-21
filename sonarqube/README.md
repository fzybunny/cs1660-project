# SonarQube and SonarScanner

This can be done with prexisting Docker containers, so we don't actually need
to create our own. The only thing to do here is to find a way to manage the
containers from the main application.

The containers are:
 * `sonarqube:latest`
 * `sonarsource/sonar-scanner-cli`

They should be run with these commands:
```
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```
```
docker run --rm -e SONAR_HOST_URL=http://sonarqube:9000 --link sonarqube -v ${project_dir}:/usr/src sonarsource/sonar-scanner-cli -Dsonar.projectKey=${project_key}
```

`${project_key}` is obtained from the web interface of the first command.
`${project_dir}` is the directory where the code is stored on the local machine.
**It should not be necessary to run these in the same container, as long as the
main application can pass these information between them.**

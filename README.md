This Repo helps beginners to connect to Oracle database using Python FastAPI.

Run: "python -m src.main"

Install Oracle database on MacOS:
1. Download "Oracle Database 19c for LINUX ARM (aarch64)" from Oracle website.
2. Clone "https://github.com/oracle/docker-images"
3. Goto docker-images -> Oracle Database -> SingleInstance -> docker files -> 19.3.0 -> Paste the zip file from step 1.
4. Install Docker.
5. Open Terminal and goto that docker files directory.
6. run "./buildContainerImage.sh -v 19.3.0 -e"
7. Once the build is complete check "docker images" and verify the container image is created or not.
8. Run "docker run -d --name <"replace-oracle-img-name"> -e ORACLE_PWD=<"replace-password"> -p 1521:1521 oracle/database:19.3.0-ee"
9. Run "docker ps" for checking the health of the image. 
10. Once the status is "healthy" or "running".
11. For Database or SID Name use "docker logs <"replace-oracle-img-name">"
12. Create Users, Tables, etc and connect to the database.
for Role: Choose SYSDBA,
    Database: ORCLCDB/ORCLPDB
    Username: <"username">
    password: <"password">
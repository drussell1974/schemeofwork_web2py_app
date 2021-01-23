## start test

start_date=$(date)
echo started... $start_date
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary
echo "yarn.test-ui--verify.sh:\e[1;33m Use virtualenv 'source .venv/django/bin/activate' and run pip install -r requirements \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run task build:test ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run 'fuser -k 3002/tcp' to kill exiting process using port 3002 \e[0m"

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_*.py

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_content__when_vistor.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py

echo $start_date - $(date)
exit $x
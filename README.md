# tdd_basic_TestDrivenDevelopment

Two additional branches were created, namely
coding_without_tdd;
coding_with_tdd

Initial attempt to write the applications was done without reference to Test Driven Development using the branch, "coding_without_tdd", changes were later merged with the master branch and a release version was created.

Switch to the branch, coding_with_tdd
Creating two Python applications by creating two directories, app/ and test/, each with a blank file, __init__.py
Then, Python application and test files.

After every test failure iteration as well as test success iteration, git commit, git push to branch coding_with_tdd, then pull request to the master branch from coding_with_tdd branch, then merge annd a version is created. 

Check for all release versions
https://github.com/imosudi/tdd_basic_TestDrivenDevelopment-Football-League-results_and-Weather-data/releases


Kindly check the two log files(test_log.txt and weather_testlog.txt ) to view  nosetests log after each iterTION

nosetests -v -s test/test_league_performance.py 2>> test_log.txt

nosetests -v -s test/test_port_harcourt_weather.py 2>> weather_testlog.txt





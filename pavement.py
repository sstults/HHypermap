from paver.easy import sh, task


@task
def reset_db():
    """
    Reset the Django db, keeping the admin user
    """
    sh("python hypermap/manage.py sqlclear aggregator | python hypermap/manage.py dbshell")
    sh("python hypermap/manage.py syncdb")
    sh("python hypermap/manage.py loaddata hypermap/aggregator/fixtures/aggregator.json")

@task
def run_tests():
    """
    Executes the entire test suite.
    """
    sh('python hypermap/manage.py test aggregator --settings=settings.default')
    sh('flake8 hypermap')
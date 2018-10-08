node {
	stage('Checkout') {
		checkout scm
	}

	stage('Create Virtual Environment')
	{
		try {		
			bat 'conda create --name python_uptimer python=3 --yes'
		}
		catch (Exception ex)
		{
			
		}
		bat 'activate python_uptimer && conda update python'
	}

	stage('Install requirements') {
	    bat 'activate python_uptimer && pip install -r requirements.txt'
	}

	stage('Test') {
		bat 'activate python_uptimer && nosetests -w tests --with-xunit --with-coverage --cover-package=python_uptimer --verbosity=2'
    }

	stage('Archive') {
		archive 'nosetests.xml'
	}

	stage('Publish') {
	    step([$class: 'JUnitResultArchiver', testResults: 'nosetests.xml'])
	}
}
node {
	stage('Checkout') {
		checkout scm
	}

	stage('Install requirements') {
	    bat 'pip install -r requirements.txt'
	}

	stage('Test') {
		bat 'nosetests -w tests --with-coverage --cover-package=python_uptimer'
    }

	stage('Archive') {
		archive '.coverage'
		archive 'nosetests.xml'
	}

	stage('Publish') {
	    step([$class: 'JUnitResultArchiver', testResults: 'nosetests.xml'])
	}
}
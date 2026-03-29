pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Source code checked out."
            }
        }

        stage('Environment Setup') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt --quiet
                    echo "Dependencies installed."
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    mkdir -p test-results
                    python3 -m pytest test_iot_sensor.py -v \
                        --junitxml=test-results/results.xml
                '''
            }
            post {
                always {
                    junit 'test-results/results.xml'
                }
            }
        }

        stage('IoT Data Collection') {
            steps {
                sh 'python3 iot_sensor.py'
                archiveArtifacts artifacts: 'sensor_output.json',
                                 fingerprint: true
            }
        }

        stage('Data Analysis') {
            steps {
                sh '''
                    python3 - <<EOF
import json, statistics
with open('sensor_output.json') as f:
    data = json.load(f)
for typ in ['temperature','humidity','pressure','light']:
    vals = [r['value'] for r in data if r['type']==typ]
    if vals:
        print(f"{typ}: avg={statistics.mean(vals):.2f} max={max(vals):.2f} min={min(vals):.2f}")
EOF
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline PASSED. IoT data pipeline healthy."
        }
        failure {
            echo "Pipeline FAILED. Check console output."
        }
    }
}

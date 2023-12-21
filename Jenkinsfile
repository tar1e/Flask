pipeline:
  agent:
    label: 'my-dev-server'

  stages:
    - stage: Checkout
      steps:
        - checkout scm

    - stage: Deploy
      steps:
        - sh 'pip install -r /home/matvey/Flask/requirements.txt' 
        - sh 'python /home/matvey/Flask/application.py &'  # 

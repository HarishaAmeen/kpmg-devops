# kpmg-devops

## How to use 

### Challenge1

To build the environment, run the below command from terraform directory
```sh
cd challenge1/terraform
terraform plan -out=build.plan

#After reviewing the plan output, to apply
terraform apply "build.plan"
```

To destroy the env,
```sh
terraform destroy
```

### Challenge 2
Transfer the script to the new ec2 instances and run it by following below commands
```sh
scp -i <PATH TO PRIVATE KEY> challenge2/run.py ubuntu@<IP ADDRESS>:~/ 
python3 run.py
```

### Challenge 3
To run the script,
```sh
cd challenge3/script
python3 run.py
```

To run unit tests
```sh
cd challenge3
python -m pytest .
```


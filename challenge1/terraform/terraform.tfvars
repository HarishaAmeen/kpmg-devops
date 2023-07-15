# VPC where instance will be created
vpc_id = "vpc-00a561cf18b108e4b"

#Common subnet for all the instances in 3-tier
subnet_id = "subnet-07873bc954f170882"

#common ami name for all instances, override in instance hashmap
# ami_name = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"

#Common instance type for all, override in instance hashmap
# instance_type = "t3.nano"

#Common instance type for all, override in instance hashmap
# attach_eip = false

# Instance details
instances = {
    web = {
        ami_name = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"
        instance_type = "t3.nano"
        key_pair = "default-key"
        attach_eip = true
        security_groups = [
          "allow-http-all",
          "allow-ssh-all",
          "allow-app-traffic-all"
        ]
        tags = {
            ans_group = "web"
        }
    }
#     app = {
#         ami_name = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*"
#         instance_type = "t3.nano"
#         key_pair = "default-key"
#         attach_eip = true
#         security_groups = [
#           "allow-ssh-all",
#           "allow-app-traffic-all"
#         ]
#         tags = {
#            ans_group = "app"
#         }
#     }
#     db = {
#         ami_name = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*"
#         instance_type = "t3.nano"
#         key_pair = "default-key"
#         attach_eip = true
#         security_groups = [
#           "allow-ssh-all",
#           "allow-app-traffic-all"
#         ]
#         tags = {
#            ans_group = "db"
#         }
#    }
}

# Ansible specific vars
ansi_user = "ubuntu"
ansi_private_key_path = "/Users/harishaameen/.ssh/default-ec2-key.cer"

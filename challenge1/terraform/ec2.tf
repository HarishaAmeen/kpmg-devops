data "aws_ami" "ami" {
  for_each = {for ec2_name, ec2_data in var.instances:
      ec2_name => try(ec2_data.ami_name, var.ami_name)
    }
  most_recent = true

  filter {
    name   = "name"
    values = [ each.value ]
  }

  owners = ["amazon"]
}


data "aws_security_groups" "selected" {
  for_each = var.instances

  filter {
    name   = "group-name"
    values = each.value.security_groups
  }

  depends_on = [
    aws_security_group.allow-ssh-all,
    aws_security_group.allow-app-traffic-all,
    aws_security_group.allow-http-all
    ]
}

#Instances
resource "aws_instance" "instacnes" {
  for_each = var.instances

  ami             = data.aws_ami.ami[each.key].id
  instance_type   = try(each.value.instance_type, var.instance_type)
  key_name        = try(each.value.key_pair, var.key_pair)
  security_groups = data.aws_security_groups.selected[each.key].ids
  subnet_id       = var.subnet_id

  provisioner "local-exec" {
    command = "sleep 20s; ansible-playbook -i aws_ec2.yml -u ${var.ansi_user} --private-key ${var.ansi_private_key_path} ${each.key}.yml"
    working_dir = "../ansible"
    environment = {
      ANSIBLE_HOST_KEY_CHECKING = "False"
    }
  }

  associate_public_ip_address = try(each.value.attach_eip, var.attach_eip)

  tags = merge(try(each.value.tags, {}), {
    Name = each.key
  })
}
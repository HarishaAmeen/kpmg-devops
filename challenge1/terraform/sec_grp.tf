data "aws_vpc" "vpc" {
  id = var.vpc_id
}

resource "aws_security_group" "allow-ssh-all" {
  name = "allow-ssh-all"
  vpc_id = data.aws_vpc.vpc.id
  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
  from_port = 22
    to_port = 22
    protocol = "tcp"
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow-ssh-all"
  }
}

resource "aws_security_group" "allow-app-traffic-all" {
  name = "allow-app-traffic-all"
  vpc_id = data.aws_vpc.vpc.id
  ingress {
    self = true
    from_port = 0
    to_port = 0
    protocol = "-1"
  }

  egress {
   from_port = 0
   to_port = 0
   protocol = "-1"
   cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow-app-traffic-all"
  }
}

resource "aws_security_group" "allow-http-all" {
  name        = "allow-http-all"
  description = "Allow HTTP inbound traffic"
  vpc_id      = data.aws_vpc.vpc.id

  ingress {
    description = "http"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow-http"
  }
}
variable "vpc_id" {
    type = string
    default = null
}

variable "subnet_id" {
    type = string
    default = null
}

variable "ami_name" {
    type = string
    default = null
}

variable "instances" {
    type = any
    default = {}
}

variable "instance_type" {
    type = string
    default = "t3.nano"
}

variable "key_pair" {
    type = string
    default = null
}

variable "attach_eip" {
    type = bool
    default = false
}

# Ansible specific
variable "ansi_user" {
    type = string
    default = null
}

variable "ansi_private_key_path" {
    type = string
    default = null
}

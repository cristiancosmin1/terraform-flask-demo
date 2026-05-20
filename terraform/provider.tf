terraform {
  backend "s3" {
    bucket = "terraform-state-cristiancosmin1-flask-demo"
    key    = "flask-demo/terraform.tfstate"
    region = "eu-central-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

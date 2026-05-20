resource "aws_instance" "web" {
  ami                         = "ami-0a628e1e89aaedf80"
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.web.id]
  associate_public_ip_address = true

  user_data                   = file("userdata.sh")
  user_data_replace_on_change = true

  tags = {
    Name = "flask-demo-server"
  }
}

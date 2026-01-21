#!/bin/bash

# Function to check for successful installation
check_installation() {
    if command -v "$1" &>/dev/null; then
        echo "$1 installed successfully!"
    else
        echo "Error: $1 installation failed!"
        exit 1
    fi
}

echo "Updating the system..."
sudo yum update -y

echo "Installing required dependencies..."
sudo yum install -y curl unzip python3 jq

echo "Installing AWS CLI version 2.15.30..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.15.30.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

check_installation "aws"

echo "Installing Terraform version 1.14.3..."
sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum install terraform

check_installation "terraform"

echo "Installing AWS CDK version 2.1101.0..."
sudo curl -sL https://rpm.nodesource.com/setup_lts.x | sudo bash
sudo yum install -y nodejs
sudo npm install -g aws-cdk

check_installation "cdk"

echo "Installing Ansible (latest version)..."
sudo yum install -y ansible

check_installation "ansible"

echo "Installing kubectl (latest version)..."
sudo curl -LO "https://dl.k8s.io/release/v1.26.0/bin/linux/arm64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

check_installation "kubectl"

rm -f awscliv2.zip terraform_1.14.3_linux_amd64.zip stable.txt

echo "All tools have been installed successfully!"

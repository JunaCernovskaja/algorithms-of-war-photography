FROM gitpod/workspace-full:latest

# Install Python and other dependencies
RUN sudo apt-get update && sudo apt-get install -y python3-pip python3-dev
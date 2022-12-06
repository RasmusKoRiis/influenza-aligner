# Use the ubuntu image as the base image
FROM ubuntu
 
# Install the necessary dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  git \
  python3 \
  python3-pip
 
# Clone the repository
RUN git clone https://github.com/RasmusKoRiis/influenza-aligner.git
 
# Install the python dependencies
RUN pip3 install -r influenza-aligner/requirements.txt
 
# Set the working directory to the repository
WORKDIR influenza-aligner
 
# Run the aligner script when the container is started
CMD ["python3", "aligner.py"]
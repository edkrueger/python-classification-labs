# Loan-Classifier 
This is a simple analysis of classification models used to predict if a person will default on a loan.

[Read more about this project on Medium](https://medium.com/@edkrueger_16881/using-loan-data-to-train-and-build-a-classification-machine-learning-app-174c2f1058e3)



## Build and Run in Docker Locally
Build: `docker build . -t loan-classifier`
Run: `PORT=8000 &&  docker run -p 80:${PORT} -e PORT=${PORT} loan-classifier`

# Application of Machine Learning on Amazon reviews

source data: https://www.kaggle.com/snap/amazon-fine-food-reviews \
data can also be downloaded from my S3 at: https://data-bootcamp-x399.s3.us-east-2.amazonaws.com/Reviews.csv \
the ipynb template file is set up to grab data from the S3 file already

---
## How to run locally

1. Download .zip or clone repo

2. Open command line in the extracted file

3. Create new virtual env

```
conda create -n newenvname python=3.7 anaconda
```

4. Activate new environtment

```
conda activate newenvname
```

5. Install requirements.txt
```
pip install -r requirements.txt
```
note: we are using pip install instead of 'conda install --file requirements.txt' to avoid PackagesNotFoundError

6. Launch flask app
```
python app.py
```

7. Launch preffered web browser and direct it to the given address

note: Standard address is: 'http://127.0.0.1:5000/'
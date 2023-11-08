# machine-learning-zoomcamp-midterm-project


This project uses data from the [Bay Wheels](https://www.lyft.com/bikes/bay-wheels/system-data) bike-sharing program to create a model to predict whether a rider departing from a certain station is probably a registered member or a casual user. Bay Wheels could leverage this insight to tailor campaigns to users at particular stations during selected times.


## Run  the project locally

To run the project locally, make sure you are using Python 3.10 and do the following:

* Install [virtualenv](https://virtualenv.pypa.io/en/latest/): `pip install virtualenv`    
* Create a virtual environment for the project:  `python3.10 -m venv midterm-project-env`
* Activate the virtual env: `source midterm-project-env/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
* To build a model run `python train.py`
* To run prediction app locally run `flask --app predict run`


## Building the docker image

To build the image:

    docker build -t bike-share-member-prediction .

To run the image locally:

    docker container run -it --rm -p80:80 bike-share-member-prediction

To publish the image to Docker image registry to run the app on render.com for example, do the following:

    docker tag bike-share-member-prediction yourusername/bike-share-member-prediction:v0.0.1
    docker push yourusername/bike-share-member-prediction:v0.0.1

# Cloud deployment

The prediction app has been deployed to https://machine-learning-zoomcamp-midterm-poject.onrender.com. The deployment has been done manually from Render web UI by using a Docker image `hjkero/bike-share-member-prediction:v0.0.1`

You can do a POST request to the above URL with the following kind of body to predict if the user is a member or not:

    {
        "rideable_type": "electric_bike",
        "start_station_name": "3rd_st_at_townsend_st",
        "start_hour_of_day": 9,
        "start_weekday": 9
    }





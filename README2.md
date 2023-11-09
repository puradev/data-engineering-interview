## Random User Loader Instructions
### Pre-Reqs
This repo uses [MAKE]('https://www.gnu.org/software/make/manual/make.html') and [docker-compose]('https://docs.docker.com/compose/) to spin up and tear down the local dev environment. MAKE is not required if you'd prefer to just user docker-compose. You will need to be able to run Docker containers on your local machine. 

## Usage Steps
1. From the home dir run `make build` to build the image locally
2. Run `make up` to start the container
3. Run `make shell` to attach a shell to the running container

- once in the shell run the following

4. Run `python app/random_user_loader.py`
5. To run unit tests enter `pytest`

The script will generate a new line delimited json file in your local directory at `/local_data/user_information.json`

- It should return 200 records for random users, with only the fields :
   - First name
   - Last name
   - Gender
   - Email address
   - Date of birth
   - Phone number (either the phone number or cell if phone is null)
   - Nationality

##  Known Limitations
- The test coverage is not absolutely complete, as a real life example (where I'd take a bit more time) all the functions would have tests, for the purpose of this exercise I wanted to demonstrate proper testing with pytest and some more advanced concepts like unitest.mock

- The api call is pinned to return 200 random users

- The container could have an entrypoint that just runs the script, but I wanted users to be able to run the pytest


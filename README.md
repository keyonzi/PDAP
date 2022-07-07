# PDAP Assessment
# 
# # 
## Test Requirements

Build a RESTful api that services requests for sprocket factory data and sprockets.

An endpoint that returns all sprocket factory data
	- An endpoint that returns factory data for a given factory id
	- An endpoint that returns sprockets for a given id
	- An endpoint that will create new sprocket
	- An endpoint that will update sprocket for a given id


## Endpoints Created

	- Return all Factories
	- Add a Factory
	- Update factory by ID
	- Return a Factory by ID
	- Delete a Factory by ID
	- Return all Sprockets
	- Add a Sprocket
	- Update Sprocket by ID
	- Return a Sprocket by ID
	- Delete a Sprocket by ID

TEST STEPS:

Please note, for testing the API I used a free tool called Postman. Any tool can be used to make the API requests, but I found Postman the simplest and most straightforward.

Run "docker compose up --build pythonapp" from the terminal<br>
	-This should automatically install the requirements and build the image environment needed

Run "docker compose up --build pythonapp" from the terminal AGAIN<br>
	-I did experience some issues setting up the DB via Docker, and it meant on a clean install, it needs to be run twice. This isn't ideal, but for speed I just moved on


For all of the API tests below please use an API testing mechanism like Postman or curl. I will outline the the API call to make, and provide the json formatted body to send to the API in the sections below.

### Homepage Test	
GET http://localhost:80/
	
### Add Factories

We will add 3 factories to the DB.

**POST** http://localhost:80/factories

{
    "sprocket_production_actual":33,
    "sprocket_production_goal":36
}

**POST** http://localhost:80/factories
{
    "sprocket_production_actual":12,
    "sprocket_production_goal":29
}

**POST** http://localhost:80/factories
{
    "sprocket_production_actual":40,
    "sprocket_production_goal":40
}

### Add Sprockets

We will add 3 sprockets to the DB.

**POST** http://localhost:80/sprockets

{
    "teeth":5,
    "pitch_diameter":5,
    "outside_diameter":6,
    "pitch": 1
}

**POST** http://localhost:80/sprockets
{
    "teeth":2,
    "pitch_diameter":2,
    "outside_diameter":2,
    "pitch": 2
}

**POST** http://localhost:80/sprockets
{
    "teeth":8,
    "pitch_diameter":7,
    "outside_diameter":6,
    "pitch": 5
}

### Update Factory by ID
**PUT** http://localhost:80/factories/3
{
    "sprocket_production_actual":30,
    "sprocket_production_goal":30
}

### Get Factory by ID
**GET** http://localhost:80/factories/3

### Delete Factory by ID
**DELETE** http://localhost:80/factories/1

### Get all Factories
**GET** http://localhost:80/factories

### Update Sprocket by ID
**PUT** http://localhost:80/sprockets/1

{
    "teeth":5,
    "pitch_diameter":5,
    "outside_diameter":5,
    "pitch": 5
}

### Get Sprocket by ID
**GET** http://localhost:80/sprockets/1

### Delete Sprocket by ID
**DELETE** http://localhost:80/sprockets/2

### Get all Sprockets
**GET** http://localhost:80/sprockets


With regards to expanding at scale, it would need a proper backend database. Then we could build an API with all of the functions people would need to get what they are looking for.
# simple_bitly  
Simple_bitly is a URL shortener software.  
This project has been developed solely for technical purposes.  
Simple_bitly consists of two modules. the `generator` and the `redirector`.  

## Installation
First you need to clone the project or download it directly.  
Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install simple_bitly.  

```bash
cd [PATH_TO_DOWNLOAD]
pip install .
```

## Deployment
We use [gunicorn](https://gunicorn.org/) to serve our wsgi application. When you install `simple_bitly` gunicorn is
also installed as a dependency library. so you don't need to install it yourself.  
you can deploy the `generator` and the `redirector` using the following commands respectively.  
**Note**: You can bind it to any address of your liking.  
```bash
cd [PATH_TO_DOWNLOAD]
gunicorn simplebitly.generator:generator --bind localhost:8000
gunicorn simplebitly.redirector:redirector --bind localhost:8001
```

## Usage
To use `simple_bitly` use the following command to send a your URL to the `generator`.
```bash
curl localhost:8000 -X POST -d "url=[some long URL]"
```
The answer to the request is an 8-char fixed-length string which is basically your short url.  
Now take the accquired short URL to make a request to the `redirector`.
You can use a web browser for this part as it's a simple *GET* request.
so simply visit `localhost:8001/[short URL]`.  
Now you must be automatically redirected to your original URL.

## Tests
Although this project is not using any 3rd-party library to handle BDD tests, I've done my best to follow the philosophy 
to some extent. Hence, we use the natural language style of `Feature` files in BDD to name our `unittest`s.
So throughout the project, `unittest`s follow the below template.
```python
def test_[Given clause]_[When clause]_[Then clause]()
```
**Note**: The keywords: `given`, `when` and `then` are simply ommited because of redundancy.

## Contributing
Pull requests are welcome.
Please make sure to update tests as appropriate if you decide to make a pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)

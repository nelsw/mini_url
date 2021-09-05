# mini url
An example URL Shortener Application

```shell
# Clones the src, enters the directory, and runs the app. 
git clone https://github.com/nelsw/mini_url.git && cd mini_url && flask run

# Encodes the given "long" URL into a "short" url
curl -X PUT -d encode=http://arepublixchickentendersubsonsale.com http://localhost:5000 -w "\n"

# Decodes the given "short" url into "long"
curl -X GET http://localhost:5000/XWbNWn -w "\n"

# Remove the project from your machine (Mac/Unix)
rm -rf mini_url

# Remove the project from your machine (Windows)
rmdir /Q /S mini_url
```

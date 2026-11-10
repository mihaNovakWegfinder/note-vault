# 1. Go to imob-docker images and build the images
## do not forget to incriment the tag

```sh
docker build --no-cache --pull --platform linux/amd64 \
  --build-arg TAG=v1.15.1-imob7 \
  -t imobregistry.azurecr.io/controller:v1.15.1-imob7 .
```

# 2. Once build you can check if the images have what you need

```sh
docker run --rm --entrypoint apk imobregistry.azurecr.io/controller:v1.15.1-imob7 info -v | grep -E '^(musl|zlib|curl|libcurl|brotli)'
```

# 3. Login into the our docker regestery

```sh
az acr login -n imobregistry
```

# 4. Push the imgages to regestery

```sh
docker push imobregistry.azurecr.io/controller:v1.15.1-imob7
```

# 5. Update the image in the kubectl config
https://github.com/i-mobility/kubernetes-config/commit/0e4d2bc1607dc059bf8b65572e28a3736936f0e1

```sh
    image: imobregistry.azurecr.io/controller:v1.15.1-imob7
```

# 6. Apply the change

```sh
    kubectl apply <your targeted source>
```
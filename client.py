import Algorithmia
# Authenticate with your API key
apiKey = "simM4rTOyKHKXgtMWfBnqJYOsNd1"
input = "ckreager"
client = Algorithmia.client(apiKey)
algo = client.algo('demo/Hello/')
print("Connecting as %s" % input)

# Pass in input required by algorithm
try:
    # Get the summary result of your file's contents
    print(algo.pipe(input).result)
except Exception as error:
    # Algorithm error if, for example, the input is not correctly formatted
    print(error)

# print algo.pipe(input)

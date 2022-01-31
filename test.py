from urllib.request import urlcleanup
import requests


def main():
  url = "http://127.0.0.1:8000/"
  res = requests.get(url)
  print(res.json())


if __name__ == "__name__":
  main()

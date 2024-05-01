import json
import cfscrape

class PyHaveIBeenPwned:
    API_ENDPOINT = "https://haveibeenpwned.com/api/v2/"
    ERROR_STRINGS = {
        400: "400 - Bad request - Invalid account specified",
        403: "403 - Forbidden - Request is forbidden",
        404: "404 - Not found - No account match",
        429: "429 - Rate limit exceeded - The rate limit for the API has been reached. Please try again later",
        "5XX": "5XX - Server error - The server returned an error"
    }

    def makeScrapedRequest(self, urlToFetch):
        requestScraper = cfscrape.create_scraper()
        response = requestScraper.get(url=urlToFetch)
        if response.status_code >= 500:
            return self.ERROR_STRINGS["5XX"]
        elif 400 <= response.status_code < 500:
            return self.ERROR_STRINGS[response.status_code]
        else:
            content = response.content.decode('utf8')
            return json.loads(content)

    def getAccountBreaches(self, email, domain=None):
        urlEndpoint = "breachedaccount/"
        url = f"{self.API_ENDPOINT}{urlEndpoint}{email}"
        if domain:
            url += f"?domain={domain}"
        return self.makeScrapedRequest(url)

    def getDomainBreaches(self, domain):
        urlEndpoint = "breaches/"
        url = f"{self.API_ENDPOINT}{urlEndpoint}?domain={domain}"
        return self.makeScrapedRequest(url)

    def getDomainBreach(self, name):
        urlEndpoint = "breach/"
        url = f"{self.API_ENDPOINT}{urlEndpoint}{name}"
        return self.makeScrapedRequest(url)

    def getDataClasses(self):
        urlEndpoint = "dataclasses/"
        url = f"{self.API_ENDPOINT}{urlEndpoint}"
        return self.makeScrapedRequest(url)

    def getAccountPastes(self, email):
        urlEndpoint = "pasteaccount/"
        url = f"{self.API_ENDPOINT}{urlEndpoint}{email}"
        return self.makeScrapedRequest(url)

    def testMe(self):
        return self.getAccountBreaches("foo@bar.com")

if __name__ == "__main__":
    instance = PyHaveIBeenPwned()
    results = instance.testMe()
    print(results)


import json
import re
import cfscrape

class pyHaveIBeenPwned():
    #End Nodes#
    apiEndpoint = "https://haveibeenpwned.com/api/v2/"
    errorStrings = {400: "400 - Bad request - Invalid account specified",
                    403: "403 - Forbidden - Request is forbidden",
                    404: "404 - Not found - No account match",
                    429: "429 - Rate limit exceeded - The rate limit for the API has been reached. Please try again later",
                    "5XX": "5XX - Server error - The server returned an error"}
                    
    #Constructor
    def __init__(self):
        return

    def makeScrapedRequest(self, urlToFetch):
        requestScraper = cfscrape.create_scraper()
        r = requestScraper.get(url=urlToFetch)
        if r.status_code >= 500:
            return self.errorStrings["5XX"]
        elif r.status_code >= 400 and r.status_code < 500:
            return self.errorStrings[int(r.status_code)]
        else:
            resultContent = r.content
            resultContent = resultContent.decode('utf8')
            resultContent = json.loads(resultContent)
            return resultContent

    def getAccountBreaches(self, email, domain=None):
        urlEndpoint = "breachedaccount/"
        if domain:
            url = "{0}{1}{2}?domain={3}".format(self.apiEndpoint, urlEndpoint, email, domain)
        else:
            url = "{0}{1}{2}".format(self.apiEndpoint, urlEndpoint, email)
        r = self.makeScrapedRequest(url)
        return r

    def getDomainBreaches(self, domain):
        urlEndpoint = "breaches/"
        url = "{0}{1}?domain={2}".format(self.apiEndpoint, urlEndpoint, domain)
        r = self.makeScrapedRequest(url)
        return r

    def getDomainBreach(self, name):
        urlEndpoint = "breach/"
        url = "{0}{1}{2}".format(self.apiEndpoint, urlEndpoint, name)
        r = self.makeScrapedRequest(url)
        return r

    def getDataClasses(self):
        urlEndpoint = "dataclasses/"
        url = "{0}{1}".format(self.apiEndpoint, urlEndpoint)
        r = self.makeScrapedRequest(url)
        return r

    def getAccountPastes(self, email):
        urlEndpoint = "pasteaccount/"
        url = "{0}{1}{2}".format(self.apiEndpoint, urlEndpoint, email)
        r = self.makeScrapedRequest(url)
        return r

    def testMe(self):
        t = self.getAccountBreaches("foo@bar.com")
        return t

if __name__ == "__main__":
    testClassInstance = pyHaveIBeenPwned()
    testResults = testClassInstance.testMe()
    print(testResults)

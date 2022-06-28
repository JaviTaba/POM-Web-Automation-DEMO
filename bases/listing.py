from lxml import etree


class Listing:
    def __init__(self, listing):
        self.name = listing.find().text


class PageWithListings:
    def __init__(self, page_source):
        self.tree = etree.HTML(page_source)

    def get_listings(self, locator):
        elements = self.tree.findall(locator)
        return [Listing(element) for element in elements]

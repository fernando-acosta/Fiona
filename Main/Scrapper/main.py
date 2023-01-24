from power_outage_us_scraper import PowerOutageUSScraper

if __name__ == '__main__':
    scraper = PowerOutageUSScraper()
    scraper.scrape()
    scraper.save_to_database()
    # TODO Generate Statistics 
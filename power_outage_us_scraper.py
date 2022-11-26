from base_scraper import BaseScraper
import datetime 

class PowerOutageUSScraper(BaseScraper):
    _data_source_id = 1
    _customers_out_xpath= '/html/body/div[2]/table/tbody/tr[2]/td/div[3]'
    _customers_tracked_xpath= '/html/body/div[2]/table/tbody/tr[2]/td/div[2]'
    _last_update_xpath= '/html/body/div[2]/div[2]/div[4]/div/div[2]/item'

    def scrape(self):
        with self.driver as driver:
            for region in self.regions:
                row_data = {}
                # Step 1: Access Power Outage page
                driver.get(f"{self.source_url}{region['source_specific_region_id']}")

                # Step 2: Scrape Data
                last_updated_on = driver.find_element('xpath', self._last_update_xpath).get_attribute("value")
                customers_out = driver.find_element('xpath', self._customers_out_xpath).text
                total_clients = driver.find_element('xpath', self._customers_tracked_xpath).text 
                # Step 3: Save Data
                row_data['total_clients'] = int(total_clients.replace(',', ''))
                row_data['clients_without_power_service'] = int(customers_out.replace(',', ''))
                row_data['region_id'] = region['region_id']
                row_data['source_last_updated_on'] = datetime.datetime.today()
                self._data = self._data.append(row_data, ignore_index=True)

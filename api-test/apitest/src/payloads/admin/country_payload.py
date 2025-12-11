from datetime import datetime

class CountryPayload(object):
    def add(self, iso2_alpha=None, iso3_alpha=None, country_name=None, country_name1=None, country_name2=None, country_name3=None, country_short_name=None, short_name1=None, short_name2=None, short_name3=None, currency_code=None, main_language=None, status_of_country=None, order=None, region_of_country=None):
        if not iso2_alpha:
            iso2_alpha = ''
        if not iso3_alpha:
            iso3_alpha = ''
        if not country_name:
            country_name = ''
        if not country_name1:
            country_name1 = ''
        if not country_name2:
            country_name2 = ''
        if not country_name3:
            country_name3 = ''
        if not country_short_name:
            country_short_name = ''
        if not short_name1:
            short_name1 = ''
        if not short_name2:
            short_name2 = ''
        if not short_name3:
            short_name3 = ''
        if not currency_code:
            currency_code = ''
        if not main_language:
            main_language = ''
        if not status_of_country:
            status_of_country = ''
        if not order:
            order = 0
        if not region_of_country:
            region_of_country = ''
        payload = {
            "iso2_alpha": iso2_alpha,
            "iso3_alpha": iso3_alpha,
            "country_name": country_name,
            "multi_lingual_country_name": {
                "country_name1": country_name1,
                "country_name2": country_name2,
                "country_name3": country_name3
            },
            "country_short_name": country_short_name,
            "multi_lingual_country_short_name": {
                "short_name1": short_name1,
                "short_name2": short_name2,
                "short_name3": short_name3
            },
            "currency_code": currency_code,
            "main_language": main_language,
            "status_of_country": status_of_country,
            "order": order,
            "region_of_country": region_of_country
        }
        return payload

    def update(self, id=None, iso2_alpha=None, iso3_alpha=None, country_name=None, country_name1=None, country_name2=None, country_name3=None, country_short_name=None, short_name1=None, short_name2=None, short_name3=None, currency_code=None, main_language=None, status_of_country=None, order=None, region_of_country=None):
        if not id:
            id = 0
        if not iso2_alpha:
            iso2_alpha = ''
        if not iso3_alpha:
            iso3_alpha = ''
        if not country_name:
            country_name = ''
        if not country_name1:
            country_name1 = ''
        if not country_name2:
            country_name2 = ''
        if not country_name3:
            country_name3 = ''
        if not country_short_name:
            country_short_name = ''
        if not short_name1:
            short_name1 = ''
        if not short_name2:
            short_name2 = ''
        if not short_name3:
            short_name3 = ''
        if not currency_code:
            currency_code = ''
        if not main_language:
            main_language = ''
        if not status_of_country:
            status_of_country = ''
        if not order:
            order = 0
        if not region_of_country:
            region_of_country = ''
        payload = {
            "id": id,
            "iso2_alpha": iso2_alpha,
            "iso3_alpha": iso3_alpha,
            "country_name": country_name,
            "multi_lingual_country_name": {
                "country_name1": country_name1,
                "country_name2": country_name2,
                "country_name3": country_name3
            },
            "country_short_name": country_short_name,
            "multi_lingual_country_short_name": {
                "short_name1": short_name1,
                "short_name2": short_name2,
                "short_name3": short_name3
            },
            "currency_code": currency_code,
            "main_language": main_language,
            "status_of_country": status_of_country,
            "order": order,
            "region_of_country": region_of_country
        }
        return payload

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, iso2_alpha=None, iso3_alpha=None, country_name=None, page_index=None, page_size=None):
        if not iso2_alpha:
            iso2_alpha = ''
        if not iso3_alpha:
            iso3_alpha = ''
        if not country_name:
            country_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "iso2_alpha": iso2_alpha,
            "iso3_alpha": iso3_alpha,
            "country_name": country_name,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def simple_search(self, search_text=None, page_size=None, page_index=None):
        if not search_text:
            search_text = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "search_text": search_text,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload
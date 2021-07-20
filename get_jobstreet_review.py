import requests
from bs4 import BeautifulSoup
import pandas as pd

# company jobstreet links
companies = {
    'Payfazz': 'https://www.jobstreet.co.id/en/companies/1010964-pt-payfazz-teknologi-nusantara',
    'HappyFresh': 'https://www.jobstreet.co.id/en/companies/778409-happyfresh',
    'DANA': 'https://www.jobstreet.co.id/en/companies/156860936056163-dana-indonesia',
    'Mekari': 'https://www.jobstreet.co.id/en/companies/832497-pt-mid-solusi-nusantara-mekari',
    'Tiket': 'https://www.jobstreet.co.id/en/companies/739059-pt-global-tiket-network',
    'Alodokter': 'https://www.jobstreet.co.id/en/companies/810792-alodokter',
    'Tokopedia': 'https://www.jobstreet.co.id/en/companies/722539-pt-tokopedia',
    'Moka': 'https://www.jobstreet.co.id/en/companies/779406-pt-moka-teknologi-indonesia',
    'HarukaEdu': 'https://www.jobstreet.co.id/en/companies/749483-pt-haruka-evolusi-digital-utama',
    'GoJek': 'https://www.jobstreet.co.id/en/companies/735646-pt-aplikasi-karya-anak-bangsa-go-jek-indonesia',
    'Quipper': 'https://www.jobstreet.co.id/en/companies/810854-pt-quipper-edukasi-indonesia',
    'Grab': 'https://www.jobstreet.co.id/en/companies/1235646-pt-grab-indonesia',
    'Zalora': 'https://www.jobstreet.co.id/en/companies/741840-pt-fashion-eservices-indonesia-zalora',
    'Bukalapak': 'https://www.jobstreet.co.id/en/companies/772913-pt-bukalapak',
    'Traveloka': 'https://www.jobstreet.co.id/en/companies/740178-pt-trinusa-travelindo',
    'Ruangguru': 'https://www.jobstreet.co.id/en/companies/865007-ruangguru',
    'FinAccel (Kredivo)': 'https://www.jobstreet.co.id/en/companies/818222-pt-finaccel-teknologi-indonesia',
    'Blibli': 'https://www.jobstreet.co.id/en/companies/778275-pt-global-digital-niaga-blibli',
    'PegiPegi': 'https://www.jobstreet.co.id/en/companies/779476-pt-go-online-destinations-pegipegi',
    'Fore Coffee': 'https://www.jobstreet.co.id/en/companies/1272057-pt-fore-kopi-indonesia',
    'Shopee': 'https://www.jobstreet.co.id/en/companies/778744-shopee-internasional-indonesia',
    'OVO': 'https://www.jobstreet.co.id/en/companies/810877-ovo-pt-visionet-internasional',
    'Amartha': 'https://www.jobstreet.co.id/en/companies/998332-pt-amartha-mikro-fintek-jakarta',
    'Lazada': 'https://www.jobstreet.co.id/en/companies/733046-lazadaid',
    'Zenius': 'https://www.jobstreet.co.id/en/companies/739458-zenius-education',
    'Cermati': 'https://www.jobstreet.co.id/en/companies/777739-pt-dwi-cermat-indonesia',
    'Berrybenka': 'https://www.jobstreet.co.id/en/companies/749588-pt-berrybenka',
    'Bizzy': 'https://www.jobstreet.co.id/en/companies/778855-bizzyid',
    'Bhinneka': 'https://www.jobstreet.co.id/en/companies/713003-pt-bhinneka-mentari-dimensi',
    'Halodoc ID': 'https://www.jobstreet.co.id/en/companies/812304-halodoc',
    'JD.ID': 'https://www.jobstreet.co.id/en/companies/779394-jd-id-pt-ritel-bersama-nasional',
    'Warung Pintar': 'https://www.jobstreet.co.id/en/companies/1050237-pt-warung-pintar-sekali',
    'Ralali': 'https://www.jobstreet.co.id/en/companies/775283-ralali',
    'Fabelio': 'https://www.jobstreet.co.id/en/companies/812926-fabelio',
    'Sociolla': 'https://www.jobstreet.co.id/en/companies/777495-pt-social-bella-indonesia',
    'OYO Indonesia': 'https://www.jobstreet.co.id/en/companies/1239253-pt-oyo-rooms-indonesia',
    'Uang Teman': 'https://www.jobstreet.co.id/en/companies/836103-pt-digital-alpha-indonesia-uangteman',
    'Akulaku': 'https://www.jobstreet.co.id/en/companies/860537-pt-akulaku-silvrr-indonesia',
}


def get_reviews(link):
    reviews = {}  # number of reviews in rating 5,4,3,2,1

    page = requests.get(link)  # fetch link
    result = BeautifulSoup(page.text)  # get HTML text of the result

    class_id = '_3eyB2L9D5BjiN6P4xTnSH_'  # class for finding num_review
    result = result.find_all('span', class_=class_id)

    for idx, num_review in enumerate(result):
        reviews[str(5-idx)] = int(num_review.text)

    return reviews


def iterate_company_reviews(companies):
    df = pd.DataFrame()

    for company_name, link in companies.items():
        company_reviews = {}
        company_reviews['company_name'] = company_name
        print('Getting reviews for', company_name)
        reviews = get_reviews(link)
        company_reviews.update(reviews)
        company_reviews_df = pd.DataFrame(company_reviews, index=[0])
        df = df.append(company_reviews_df, ignore_index=True)

    filename = 'jobstreet_review.csv'
    print('Save result to', filename)
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    print('Start iterating companies')
    iterate_company_reviews(companies)
    print('Complete')

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Website Data Models

# from datamodels import *
class CompanyInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    companyName = db.Column(db.String(32))
    companyAddress = db.Column(db.String(64))
    companyAddressLink = db.Column(db.String(64))
    companyMapSource = db.Column(db.String(200))
    companyPhoneText = db.Column(db.String(32))
    companyPhoneLink = db.Column(db.String(32))
    companyEmail = db.Column(db.String(32))

    def __repr__(self):
        return '<CompanyInformation {}>'.format(self.id)

class ProductPrices(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    priceWeddingBouquet = db.Column(db.String(32))
    priceRoses10Pack = db.Column(db.String(32))
    priceTulips10Pack = db.Column(db.String(32))
    priceSummerBouquet = db.Column(db.String(32))
    priceFallBouquet = db.Column(db.String(32))
    priceFuneralWreath = db.Column(db.String(32))
    priceLilies = db.Column(db.String(32))
    priceHydrangea = db.Column(db.String(32))
    priceAloeVera = db.Column(db.String(32))
    priceCactusInPot = db.Column(db.String(32))

    def __repr__(self):
        return '<ProductPrices {}>'.format(self.id)

class Resolution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    max_width = db.Column(db.Integer)
    path = db.Column(db.String)
    
    # Foreign key relationship to Products model
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Products', back_populates='resolutions')

    def __repr__(self):
        return '<Resolution {}>'.format(self.id)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.String, unique=True)
    defaultPath = db.Column(db.String)
    alt = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.String)
    unit = db.Column(db.String)
    resolutions = db.relationship('Resolution', back_populates='product', cascade='all, delete-orphan')

    def __repr__(self):
        return '<Products {}>'.format(self.productId)

class OpeningHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openingHoursMonday = db.Column(db.String)
    openingHoursTuesday = db.Column(db.String)
    openingHoursWednesday = db.Column(db.String)
    openingHoursThursday = db.Column(db.String)
    openingHoursFriday = db.Column(db.String)
    openingHoursSaturday = db.Column(db.String)
    openingHoursSunday = db.Column(db.String)

class SocialMediaLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebookLink = db.Column(db.String)
    instagramLink = db.Column(db.String)
    xLink = db.Column(db.String)

# Website Language Data Model

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Header
    logoAlt = db.Column(db.String)

    # Slideshow
    slideshowSummerBouquetAlt = db.Column(db.String)
    slideshowTulipBouquetAlt = db.Column(db.String)
    slideshowFallBouquetAlt = db.Column(db.String)

    # Flowergram
    flowergramHeaderText = db.Column(db.String)
    flowergramButtonText = db.Column(db.String)
    flowergramQuestionText = db.Column(db.String)
    flowergramVisitOrCall = db.Column(db.String)
    flowergramZipCheckText = db.Column(db.String)
    zipCodePlaceholder = db.Column(db.String)

    # Products section
    productsHeaderText = db.Column(db.String)
    dealOfTheDayText = db.Column(db.String)
    nameWeddingBouquet = db.Column(db.String)
    altWeddingBouquet = db.Column(db.String)
    nameRoses10Pack = db.Column(db.String)
    altRoses10Pack = db.Column(db.String)
    nameTulips10Pack = db.Column(db.String)
    altTulips10Pack = db.Column(db.String)
    nameSummerBouquet = db.Column(db.String)
    altSummerBouquet = db.Column(db.String)
    nameFallBouquet = db.Column(db.String)
    altFallBouquet = db.Column(db.String)
    nameFuneralWreath = db.Column(db.String)
    altFuneralWreath = db.Column(db.String)
    nameLilies = db.Column(db.String)
    altLilies = db.Column(db.String)
    nameHydrangea = db.Column(db.String)
    altHydrangea = db.Column(db.String)
    nameAloeVera = db.Column(db.String)
    altAloeVera = db.Column(db.String)
    nameCactusInPot = db.Column(db.String)
    altCactusInPot = db.Column(db.String)
    sek = db.Column(db.String)
    sekEach = db.Column(db.String)
    
    # Add other product fields with respective translations
    
    # Map section
    mapHeaderText = db.Column(db.String)
    noscriptMapAlt = db.Column(db.String)

    # Employee information section
    employeeInformationHeaderText = db.Column(db.String)
    fredrikOrtqvistTitle = db.Column(db.String)
    fredrikOrtqvistAlt = db.Column(db.String)
    orjanJohanssonTitle = db.Column(db.String)
    orjanJohanssonAlt = db.Column(db.String)
    annaPetterssonTitle = db.Column(db.String)
    annaPetterssonAlt = db.Column(db.String)

    # Employee fields as necessary

    # Contact information
    contactUsHeaderText = db.Column(db.String)

    # Opening hours
    openingHoursHeaderText = db.Column(db.String)
    monday = db.Column(db.String)
    tuesday = db.Column(db.String)
    wednesday = db.Column(db.String)
    thursday = db.Column(db.String)
    friday = db.Column(db.String)
    saturday = db.Column(db.String)
    sunday = db.Column(db.String)

    # Closed days
    closedDaysHeaderText = db.Column(db.String)
    closedDaysDateJan1 = db.Column(db.String)
    closedDaysNameJan1 = db.Column(db.String)
    closedDaysDateJan6 = db.Column(db.String)
    closedDaysNameJan6 = db.Column(db.String)
    closedDaysDateMay1 = db.Column(db.String)
    closedDaysNameMay1 = db.Column(db.String)
    closedDaysDateJun6 = db.Column(db.String)
    closedDaysNameJun6 = db.Column(db.String)
    closedDaysDateDec24 = db.Column(db.String)
    closedDaysNameDec24 = db.Column(db.String)
    closedDaysDateDec25 = db.Column(db.String)
    closedDaysNameDec25 = db.Column(db.String)
    closedDaysDateDec26 = db.Column(db.String)
    closedDaysNameDec26 = db.Column(db.String)
    closedDaysDateDec31 = db.Column(db.String)
    closedDaysNameDec31 = db.Column(db.String)

    # Social media icons
    altFacebookIcon = db.Column(db.String)
    altInstagramIcon = db.Column(db.String)
    altXIcon = db.Column(db.String)

    # JavaScript
    dealOfTheDayTextBanner = db.Column(db.String)
    noZipCode = db.Column(db.String)
    zipCodeNotCorrectLength = db.Column(db.String)
    invalidZipCode = db.Column(db.String)
    validZipCode = db.Column(db.String)
    holidayClosed = db.Column(db.String)
    beforeOpening = db.Column(db.String)
    afterClosing = db.Column(db.String)
    open = db.Column(db.String)

    # Language settings
    language = db.Column(db.String)
    languageKey = db.Column(db.String)

    def __repr__(self):
        return '<LanguageEnglish {}>'.format(self.id)
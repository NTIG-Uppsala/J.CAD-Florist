
const lang = document.querySelector("#data").dataset.lang;
const data = {
  en: {
    data: {
      companyName: "florista",
      companyAddress: "Fjällgatan 32H, 981 39 KIRUNA",
      companyAddressLink: "https://maps.app.goo.gl/pne1zVvPmaNENVQz5",
      companyPhoneText: "0630-555-555",
      companyPhoneLink: "0630555555",
      companyEmail: "info@florista.ntig.dev",
      rootPath: "../../",
      priceWeddingBouquet: "1 200",
      priceRoses10Pack: "150",
      priceTulips10Pack: "100",
      priceSummerBouquet: "200",
      priceFallBouquet: "400",
      priceFuneralWreath: "800",
      priceLilies: "29",
      priceHydrangea: "59",
      priceAloeVera: "99",
      priceCactusInPot: "99",
      openingHoursMonday: "10-18",
      openingHoursTuesday: "10-18",
      openingHoursWednesday: "10-17",
      openingHoursThursday: "10-17",
      openingHoursFriday: "10-18",
      openingHoursSaturday: "12-16",
      openingHoursSunday: "12-15",
      facebookLink: "https://www.facebook.com/ntiuppsala",
      instagramLink: "https://www.instagram.com/ntiuppsala",
      xLink: "https://x.com/ntiuppsala",
      products: [
        {
          id: "product-brollopsbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/brollopsbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/brollopsbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/brollopsbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/brollopsbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/brollopsbukett.jpg",
          alt: "altWeddingBouquet",
          name: "nameWeddingBouquet",
          price: "1 200",
          unit: "sek"
        },
        {
          id: "product-rosor-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/rosor-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/rosor-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/rosor-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/rosor-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/rosor-10-pack.jpg",
          alt: "altRoses10Pack",
          name: "nameRoses10Pack",
          price: "150",
          unit: "sek"
        },
        {
          id: "product-tulpaner-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/tulpaner-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/tulpaner-10-pack.jpg",
          alt: "altTulips10Pack",
          name: "nameTulips10Pack",
          price: "100",
          unit: "sek"
        },
        {
          id: "product-sommarbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/sommarbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/sommarbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/sommarbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/sommarbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/sommarbukett.jpg",
          alt: "altSummerBouquet",
          name: "nameSummerBouquet",
          price: "200",
          unit: "sek"
        },
        {
          id: "product-hostbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hostbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hostbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hostbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hostbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/hostbukett.jpg",
          alt: "altFallBouquet",
          name: "nameFallBouquet",
          price: "400",
          unit: "sek"
        },
        {
          id: "product-begravningskrans",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/begravningskrans.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/begravningskrans.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/begravningskrans.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/begravningskrans.jpg"
            }
          ],
          defaultPath: "images/480x320/begravningskrans.jpg",
          alt: "altFuneralWreath",
          name: "nameFuneralWreath",
          price: "800",
          unit: "sek"
        },
        {
          id: "product-liljor",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/liljor.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/liljor.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/liljor.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/liljor.jpg"
            }
          ],
          defaultPath: "images/480x320/liljor.jpg",
          alt: "altLilies",
          name: "nameLilies",
          price: "29",
          unit: "sekEach"
        },
        {
          id: "product-hortensia",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hortensia.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hortensia.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hortensia.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hortensia.jpg"
            }
          ],
          defaultPath: "images/480x320/hortensia.jpg",
          alt: "altHydrangea",
          name: "nameHydrangea",
          price: "59",
          unit: "sek"
        },
        {
          id: "product-aloe-vera",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/aloe-vera.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/aloe-vera.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/aloe-vera.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/aloe-vera.jpg"
            }
          ],
          defaultPath: "images/480x320/aloe-vera.jpg",
          alt: "altAloeVera",
          name: "nameAloeVera",
          price: "99",
          unit: "sek"
        },
        {
          id: "product-kaktus-i-kruka",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/kaktus.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/kaktus.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/kaktus.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/kaktus.jpg"
            }
          ],
          defaultPath: "images/480x320/kaktus.jpg",
          alt: "altCactusInPot",
          name: "nameCactusInPot",
          price: "99",
          unit: "sek"
        }
      ]
    },
    lang: {
      logoAlt: "Logo of the website",
      chooseLanguage: "Choose language",
      slideshowSummerBouquetAlt: "Picture of a summer bouquet",
      slideshowTulipBouquetAlt: "Picture of a tulip bouquet",
      slideshowFallBouquetAlt: "Picture of a fall bouquet",
      flowergramHeaderText: "Sur&shy;prise some&shy;one with a flower&shy;gram",
      flowergramButtonText: "Send a flower&shy;gram",
      flowergramQuestionText: "Do you want to send a flower&shy;gram?",
      flowergramVisitOrCall: "Visit us in the store or call us on",
      flowergramZipCheckText: "Double check if we deliver to your zip code:",
      zipCodePlaceholder: "Enter zip code",
      productsHeaderText: "Products",
      dealOfTheDayText: "Deal of the day",
      nameWeddingBouquet: "Wedding bouquet",
      altWeddingBouquet: "Wedding bouquet",
      nameRoses10Pack: "Roses 10-pack",
      altRoses10Pack: "Roses 10-pack",
      nameTulips10Pack: "Tulips 10-pack",
      altTulips10Pack: "Tulips 10-pack",
      nameSummerBouquet: "Summer bouquet",
      altSummerBouquet: "Summer bouquet",
      nameFallBouquet: "Fall bouquet",
      altFallBouquet: "Fall bouquet",
      nameFuneralWreath: "Funeral wreath",
      altFuneralWreath: "Funeral wreath",
      nameLilies: "Lilies",
      altLilies: "Lilies",
      nameHydrangea: "Hydrangea",
      altHydrangea: "Hydrangea",
      nameAloeVera: "Aloe vera",
      altAloeVera: "Aloe vera",
      nameCactusInPot: "Cactus in pot",
      altCactusInPot: "Cactus in pot",
      sek: "SEK",
      sekEach: "SEK/unit",
      mapHeaderText: "Map",
      noscriptMapAlt: "Map of the store's location",
      employeeInformationHeaderText: "Staff",
      fredrikOrtqvistTitle: "Owner",
      fredrikOrtqvistAlt: "Picture of Fredrik Örtqvist",
      orjanJohanssonTitle: "Florist",
      orjanJohanssonAlt: "Picture of Örjan Johansson",
      annaPetterssonTitle: "Horticulturist",
      annaPetterssonAlt: "Picture of Anna Pettersson",
      contactUsHeaderText: "Contact us",
      openingHoursHeaderText: "Opening hours",
      monday: "Monday",
      tuesday: "Tuesday",
      wednesday: "Wednesday",
      thursday: "Thursday",
      friday: "Friday",
      saturday: "Saturday",
      sunday: "Sunday",
      closedDaysHeaderText: "Closed days",
      closedDaysDateJan1: "1 Jan",
      closedDaysNameJan1: "New Year's Day",
      closedDaysDateJan6: "6 Jan",
      closedDaysNameJan6: "Epiphany",
      closedDaysDateMay1: "1 May",
      closedDaysNameMay1: "May Day",
      closedDaysDateJun6: "6 Jun",
      closedDaysNameJun6: "National Day",
      closedDaysDateDec24: "24 Dec",
      closedDaysNameDec24: "Julafton",
      closedDaysDateDec25: "25 Dec",
      closedDaysNameDec25: "Christmas Day",
      closedDaysDateDec26: "26 Dec",
      closedDaysNameDec26: "Boxing Day",
      closedDaysDateDec31: "31 Dec",
      closedDaysNameDec31: "New Year's Eve",
      altFacebookIcon: "Facebook-icon",
      altInstagramIcon: "Instagram-icon",
      altXIcon: "X-icon",
      dealOfTheDayTextBanner: "Today { productName } costs only { productPrice } instead of { productOldPrice }",
      noZipCode: "You must enter a zip code!",
      zipCodeNotCorrectLength: "The zip code must be 5 digits!",
      invalidZipCode: "We unfortunately do not deliver to this zip code!",
      validZipCode: "We deliver to this zip code!",
      holidayClosed: "Today we are closed due to a public holiday. We open at { openingTime } on { openingDay }",
      beforeOpening: "We are closed. We open at { openingTime } today",
      afterClosing: "We are closed. We open at { openingTime } on { openingDay }",
      open: "We are open. We close at { closingTime } today",
      language: "en",
      languageKey: "en"
    }
  },
  no: {
    data: {
      companyName: "florista",
      companyAddress: "Fjällgatan 32H, 981 39 KIRUNA",
      companyAddressLink: "https://maps.app.goo.gl/pne1zVvPmaNENVQz5",
      companyPhoneText: "0630-555-555",
      companyPhoneLink: "0630555555",
      companyEmail: "info@florista.ntig.dev",
      rootPath: "../../",
      priceWeddingBouquet: "1 200",
      priceRoses10Pack: "150",
      priceTulips10Pack: "100",
      priceSummerBouquet: "200",
      priceFallBouquet: "400",
      priceFuneralWreath: "800",
      priceLilies: "29",
      priceHydrangea: "59",
      priceAloeVera: "99",
      priceCactusInPot: "99",
      openingHoursMonday: "10-18",
      openingHoursTuesday: "10-18",
      openingHoursWednesday: "10-17",
      openingHoursThursday: "10-17",
      openingHoursFriday: "10-18",
      openingHoursSaturday: "12-16",
      openingHoursSunday: "12-15",
      facebookLink: "https://www.facebook.com/ntiuppsala",
      instagramLink: "https://www.instagram.com/ntiuppsala",
      xLink: "https://x.com/ntiuppsala",
      products: [
        {
          id: "product-brollopsbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/brollopsbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/brollopsbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/brollopsbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/brollopsbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/brollopsbukett.jpg",
          alt: "altWeddingBouquet",
          name: "nameWeddingBouquet",
          price: "1 200",
          unit: "sek"
        },
        {
          id: "product-rosor-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/rosor-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/rosor-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/rosor-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/rosor-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/rosor-10-pack.jpg",
          alt: "altRoses10Pack",
          name: "nameRoses10Pack",
          price: "150",
          unit: "sek"
        },
        {
          id: "product-tulpaner-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/tulpaner-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/tulpaner-10-pack.jpg",
          alt: "altTulips10Pack",
          name: "nameTulips10Pack",
          price: "100",
          unit: "sek"
        },
        {
          id: "product-sommarbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/sommarbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/sommarbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/sommarbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/sommarbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/sommarbukett.jpg",
          alt: "altSummerBouquet",
          name: "nameSummerBouquet",
          price: "200",
          unit: "sek"
        },
        {
          id: "product-hostbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hostbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hostbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hostbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hostbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/hostbukett.jpg",
          alt: "altFallBouquet",
          name: "nameFallBouquet",
          price: "400",
          unit: "sek"
        },
        {
          id: "product-begravningskrans",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/begravningskrans.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/begravningskrans.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/begravningskrans.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/begravningskrans.jpg"
            }
          ],
          defaultPath: "images/480x320/begravningskrans.jpg",
          alt: "altFuneralWreath",
          name: "nameFuneralWreath",
          price: "800",
          unit: "sek"
        },
        {
          id: "product-liljor",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/liljor.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/liljor.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/liljor.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/liljor.jpg"
            }
          ],
          defaultPath: "images/480x320/liljor.jpg",
          alt: "altLilies",
          name: "nameLilies",
          price: "29",
          unit: "sekEach"
        },
        {
          id: "product-hortensia",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hortensia.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hortensia.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hortensia.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hortensia.jpg"
            }
          ],
          defaultPath: "images/480x320/hortensia.jpg",
          alt: "altHydrangea",
          name: "nameHydrangea",
          price: "59",
          unit: "sek"
        },
        {
          id: "product-aloe-vera",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/aloe-vera.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/aloe-vera.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/aloe-vera.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/aloe-vera.jpg"
            }
          ],
          defaultPath: "images/480x320/aloe-vera.jpg",
          alt: "altAloeVera",
          name: "nameAloeVera",
          price: "99",
          unit: "sek"
        },
        {
          id: "product-kaktus-i-kruka",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/kaktus.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/kaktus.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/kaktus.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/kaktus.jpg"
            }
          ],
          defaultPath: "images/480x320/kaktus.jpg",
          alt: "altCactusInPot",
          name: "nameCactusInPot",
          price: "99",
          unit: "sek"
        }
      ]
    },
    lang: {
      logoAlt: "Logoen til nettstedet",
      chooseLanguage: "Velg språk",
      slideshowSummerBouquetAlt: "Bilde av en sommerbukett",
      slideshowTulipBouquetAlt: "Bilde av en tulipanbukett",
      slideshowFallBouquetAlt: "Bilde av en høstbukett",
      flowergramHeaderText: "Over&shy;rask noen med et blomster&shy;gram",
      flowergramButtonText: "Send et blomster&shy;gram",
      flowergramQuestionText: "Vil du sende et blomster&shy;gram?",
      flowergramVisitOrCall: "Besøk oss i butikken eller ring oss på ",
      flowergramZipCheckText: "Dobbelt&shy;sjekk om vi leverer til ditt post&shy;nummer:",
      zipCodePlaceholder: "Angi postnummer",
      productsHeaderText: "Produkter",
      dealOfTheDayText: "Dagens tilbud",
      nameWeddingBouquet: "Bryllupsbukett",
      altWeddingBouquet: "Bryllupsbukett",
      nameRoses10Pack: "Roser 10-pakke",
      altRoses10Pack: "Roser 10-pakke",
      nameTulips10Pack: "Tulipaner 10-pakke",
      altTulips10Pack: "Tulipaner 10-pakke",
      nameSummerBouquet: "Sommerbukett",
      altSummerBouquet: "Sommerbukett",
      nameFallBouquet: "Høstbukett",
      altFallBouquet: "Høstbukett",
      nameFuneralWreath: "Begravelseskrans",
      altFuneralWreath: "Begravelseskrans",
      nameLilies: "Liljer",
      altLilies: "Liljer",
      nameHydrangea: "Hortensia",
      altHydrangea: "Hortensia",
      nameAloeVera: "Aloe vera",
      altAloeVera: "Aloe vera",
      nameCactusInPot: "Kaktus i krukke",
      altCactusInPot: "Kaktus i krukke",
      sek: "SEK",
      sekEach: "SEK/stk",
      mapHeaderText: "Kart",
      noscriptMapAlt: "Kart over butikkens beliggenhet",
      employeeInformationHeaderText: "Butikkpersonale",
      fredrikOrtqvistTitle: "Eier",
      fredrikOrtqvistAlt: "Bilde av Fredrik Örtqvist",
      orjanJohanssonTitle: "Florist",
      orjanJohanssonAlt: "Bilde av Örjan Johansson",
      annaPetterssonTitle: "Horticulturist",
      annaPetterssonAlt: "Bilde av Anna Pettersson",
      contactUsHeaderText: "Kontakt oss",
      openingHoursHeaderText: "Åpningstider",
      monday: "Mandag",
      tuesday: "Tirsdag",
      wednesday: "Onsdag",
      thursday: "Torsdag",
      friday: "Fredag",
      saturday: "Lørdag",
      sunday: "Søndag",
      closedDaysHeaderText: "Stengte dager",
      closedDaysDateJan1: "1 Jan",
      closedDaysNameJan1: "Nyttårsdagen",
      closedDaysDateJan6: "6 Jan",
      closedDaysNameJan6: "Helligtrekongersdag",
      closedDaysDateMay1: "1 mai",
      closedDaysNameMay1: "Arbeidernes internasjonale kampdag",
      closedDaysDateJun6: "6 jun",
      closedDaysNameJun6: "Sveriges nasjonaldag",
      closedDaysDateDec24: "24 des",
      closedDaysNameDec24: "Julaften",
      closedDaysDateDec25: "25 des",
      closedDaysNameDec25: "Første juledag",
      closedDaysDateDec26: "26 des",
      closedDaysNameDec26: "Andre juledag",
      closedDaysDateDec31: "31 des",
      closedDaysNameDec31: "Nyttårsaften",
      altFacebookIcon: "Facebook-ikon",
      altInstagramIcon: "Instagram-ikon",
      altXIcon: "X-ikon",
      dealOfTheDayTextBanner: "I dag koster { productName } bare { productPrice } i stedet for { productOldPrice }",
      noZipCode: "Du må angi et postnummer!",
      zipCodeNotCorrectLength: "Postnummeret må være femsifret!",
      invalidZipCode: "Vi leverer dessverre ikke til dette postnummeret!",
      validZipCode: "Vi leverer til dette postnummeret!",
      holidayClosed: "I dag er vi stengt på grunn av helligdag. Vi åpner klokka { openingTime } på { openingDay }",
      beforeOpening: "Vi er stengt. Vi åpner klokka { openingTime } i dag",
      afterClosing: "Vi er stengt. Vi åpner klokka { openingTime } på { openingDay }",
      open: "Vi er åpent. Vi stenger klokka { closingTime } i dag",
      language: "nb",
      languageKey: "no"
    }
  },
  se: {
    data: {
      companyName: "florista",
      companyAddress: "Fjällgatan 32H, 981 39 KIRUNA",
      companyAddressLink: "https://maps.app.goo.gl/pne1zVvPmaNENVQz5",
      companyPhoneText: "0630-555-555",
      companyPhoneLink: "0630555555",
      companyEmail: "info@florista.ntig.dev",
      rootPath: "../../",
      priceWeddingBouquet: "1 200",
      priceRoses10Pack: "150",
      priceTulips10Pack: "100",
      priceSummerBouquet: "200",
      priceFallBouquet: "400",
      priceFuneralWreath: "800",
      priceLilies: "29",
      priceHydrangea: "59",
      priceAloeVera: "99",
      priceCactusInPot: "99",
      openingHoursMonday: "10-18",
      openingHoursTuesday: "10-18",
      openingHoursWednesday: "10-17",
      openingHoursThursday: "10-17",
      openingHoursFriday: "10-18",
      openingHoursSaturday: "12-16",
      openingHoursSunday: "12-15",
      facebookLink: "https://www.facebook.com/ntiuppsala",
      instagramLink: "https://www.instagram.com/ntiuppsala",
      xLink: "https://x.com/ntiuppsala",
      products: [
        {
          id: "product-brollopsbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/brollopsbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/brollopsbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/brollopsbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/brollopsbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/brollopsbukett.jpg",
          alt: "altWeddingBouquet",
          name: "nameWeddingBouquet",
          price: "1 200",
          unit: "sek"
        },
        {
          id: "product-rosor-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/rosor-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/rosor-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/rosor-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/rosor-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/rosor-10-pack.jpg",
          alt: "altRoses10Pack",
          name: "nameRoses10Pack",
          price: "150",
          unit: "sek"
        },
        {
          id: "product-tulpaner-10-pack",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/tulpaner-10-pack.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/tulpaner-10-pack.jpg"
            }
          ],
          defaultPath: "images/480x320/tulpaner-10-pack.jpg",
          alt: "altTulips10Pack",
          name: "nameTulips10Pack",
          price: "100",
          unit: "sek"
        },
        {
          id: "product-sommarbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/sommarbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/sommarbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/sommarbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/sommarbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/sommarbukett.jpg",
          alt: "altSummerBouquet",
          name: "nameSummerBouquet",
          price: "200",
          unit: "sek"
        },
        {
          id: "product-hostbukett",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hostbukett.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hostbukett.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hostbukett.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hostbukett.jpg"
            }
          ],
          defaultPath: "images/480x320/hostbukett.jpg",
          alt: "altFallBouquet",
          name: "nameFallBouquet",
          price: "400",
          unit: "sek"
        },
        {
          id: "product-begravningskrans",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/begravningskrans.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/begravningskrans.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/begravningskrans.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/begravningskrans.jpg"
            }
          ],
          defaultPath: "images/480x320/begravningskrans.jpg",
          alt: "altFuneralWreath",
          name: "nameFuneralWreath",
          price: "800",
          unit: "sek"
        },
        {
          id: "product-liljor",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/liljor.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/liljor.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/liljor.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/liljor.jpg"
            }
          ],
          defaultPath: "images/480x320/liljor.jpg",
          alt: "altLilies",
          name: "nameLilies",
          price: "29",
          unit: "sekEach"
        },
        {
          id: "product-hortensia",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/hortensia.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/hortensia.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/hortensia.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/hortensia.jpg"
            }
          ],
          defaultPath: "images/480x320/hortensia.jpg",
          alt: "altHydrangea",
          name: "nameHydrangea",
          price: "59",
          unit: "sek"
        },
        {
          id: "product-aloe-vera",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/aloe-vera.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/aloe-vera.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/aloe-vera.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/aloe-vera.jpg"
            }
          ],
          defaultPath: "images/480x320/aloe-vera.jpg",
          alt: "altAloeVera",
          name: "nameAloeVera",
          price: "99",
          unit: "sek"
        },
        {
          id: "product-kaktus-i-kruka",
          resolutions: [
            {
              maxWidth: 320,
              path: "images/224x149/kaktus.jpg"
            },
            {
              maxWidth: 360,
              path: "images/256x170/kaktus.jpg"
            },
            {
              maxWidth: 440,
              path: "images/320x213/kaktus.jpg"
            },
            {
              maxWidth: 520,
              path: "images/384x256/kaktus.jpg"
            }
          ],
          defaultPath: "images/480x320/kaktus.jpg",
          alt: "altCactusInPot",
          name: "nameCactusInPot",
          price: "99",
          unit: "sek"
        }
      ]
    },
    lang: {
      logoAlt: "Logotyp för webbplatsen",
      chooseLanguage: "Välj språk",
      slideshowSummerBouquetAlt: "Bild av en sommarbukett",
      slideshowTulipBouquetAlt: "Bild av en tulpanbukett",
      slideshowFallBouquetAlt: "Bild av en höstbukett",
      flowergramHeaderText: "Över&shy;raska med ett blommo&shy;gram",
      flowergramButtonText: "Skicka blommo&shy;gram",
      flowergramQuestionText: "Vill du skicka ett blommo&shy;gram?",
      flowergramVisitOrCall: "Besök oss i butiken eller ring oss på",
      flowergramZipCheckText: "Kontrollera här om vi levererar till ditt önskade postnummer:",
      zipCodePlaceholder: "Ange postnummer",
      productsHeaderText: "Produkter",
      dealOfTheDayText: "Dagens klipp",
      nameWeddingBouquet: "Bröllopsbukett",
      altWeddingBouquet: "Bröllopsbukett",
      nameRoses10Pack: "Rosor 10-pack",
      altRoses10Pack: "Rosor 10-pack",
      nameTulips10Pack: "Tulpaner 10-pack",
      altTulips10Pack: "Tulpaner 10-pack",
      nameSummerBouquet: "Sommarbukett",
      altSummerBouquet: "Sommarbukett",
      nameFallBouquet: "Höstbukett",
      altFallBouquet: "Höstbukett",
      nameFuneralWreath: "Begravningskrans",
      altFuneralWreath: "Begravningskrans",
      nameLilies: "Liljor",
      altLilies: "Liljor",
      nameHydrangea: "Hortensia",
      altHydrangea: "Hortensia",
      nameAloeVera: "Aloe vera",
      altAloeVera: "Aloe vera",
      nameCactusInPot: "Kaktus i kruka",
      altCactusInPot: "Kaktus i kruka",
      sek: "kr",
      sekEach: "kr/st",
      mapHeaderText: "Karta",
      noscriptMapAlt: "Karta över butikens läge",
      employeeInformationHeaderText: "Personal",
      fredrikOrtqvistTitle: "Ägare",
      fredrikOrtqvistAlt: "Bild på Fredrik Örtqvist",
      orjanJohanssonTitle: "Florist",
      orjanJohanssonAlt: "Bild på Örjan Johansson",
      annaPetterssonTitle: "Hortonom",
      annaPetterssonAlt: "Bild på Anna Pettersson",
      contactUsHeaderText: "Kontakta oss",
      openingHoursHeaderText: "Öppettider",
      monday: "Måndag",
      tuesday: "Tisdag",
      wednesday: "Onsdag",
      thursday: "Torsdag",
      friday: "Fredag",
      saturday: "Lördag",
      sunday: "Söndag",
      closedDaysHeaderText: "Stängda dagar",
      closedDaysDateJan1: "1 jan",
      closedDaysNameJan1: "Nyårsdagen",
      closedDaysDateJan6: "6 jan",
      closedDaysNameJan6: "Trettondedag jul",
      closedDaysDateMay1: "1 maj",
      closedDaysNameMay1: "Första maj",
      closedDaysDateJun6: "6 jun",
      closedDaysNameJun6: "Nationaldagen",
      closedDaysDateDec24: "24 dec",
      closedDaysNameDec24: "Julafton",
      closedDaysDateDec25: "25 dec",
      closedDaysNameDec25: "Juldagen",
      closedDaysDateDec26: "26 dec",
      closedDaysNameDec26: "Annandag jul",
      closedDaysDateDec31: "31 dec",
      closedDaysNameDec31: "Nyårsafton",
      altFacebookIcon: "Facebook-ikon",
      altInstagramIcon: "Instagram-ikon",
      altXIcon: "X-ikon",
      dealOfTheDayTextBanner: "Idag kostar { productName } endast { productPrice } istället för { productOldPrice }",
      noZipCode: "Du måste skriva in ett postnummer!",
      zipCodeNotCorrectLength: "Postnumret måste vara 5 siffror!",
      invalidZipCode: "Vi levererar tyvärr inte till detta postnummer!",
      validZipCode: "Vi levererar till detta postnummer!",
      holidayClosed: "Idag har vi stängt p.g.a helgdag. Vi öppnar kl. { openingTime } på { openingDay }",
      beforeOpening: "Vi har stängt. Vi öppnar kl. { openingTime } idag",
      afterClosing: "Vi har stängt. Vi öppnar kl. { openingTime } på { openingDay }",
      open: "Vi har öppet. Vi stänger kl. { closingTime } idag",
      language: "sv",
      languageKey: "se"
    }
  }
}[lang];

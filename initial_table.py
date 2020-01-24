table = """
|AffCd              |430                                                |
|AffCdNum           |<AffCd>                                            |
|accountSubTypeCd   |BusinessOwner                                      |
|accountTypeCd      |AmwayBusiness                                      |
|addrLineTwo        |Triveni Apartments                                 |
|addrStreet         |144 Lodhi Road                                     |
|addressVar         |#{generate(Address.streetAddress)}                 |
|address2Var        |#{generate(Address.streetAddress)}                 |
|busEntityNum       |430                                                |
|birthCountryCd     |IN                                                 |
|birthDateVar       |#{generateDate(-P50Y, yyyy-MM-dd'T'HH:mm:ss)}-05:00|
|balanceAmount      |100                                                |
|cntryCd            |IN                                                 |
|languageCd         |en                                                 |
|countryPersonalId  |IN                                                 |
|cityName           |NEW DELHI                                          |
|cityNameUpd        |Kerala                                             |
|currencyCd         |INR                                                |
|czshpCntryCd       |IN                                                 |
|genderCd           |Male                                               |
|genderCdL          |#{replaceFirstByRegExp((.).*, $1, <genderCd>)}     |
|natlCntryCd        |IN                                                 |
|isoCntryCd         |IN                                                 |
|postalBoxNum       |12                                                 |
|postalCd           |110001                                             |
|postalCdUpd        |673575                                             |
|stateCd            |HAR                                                |
|stateCdUpd         |                                                   |
|sponsorABONo       |561455                                             |
|taxId              |25BMSPR1264G1AS                                  |
|taxIdUpd           |25BMSPR3336G1AS                                  |
|taxTypeCd          |GSTIN                                              |
|partyFirstNameVar  |#{generateLocalized(Name.firstName,fi)}<AffCd>     |
|partyLastNameVar   |${locale}#{generateLocalized(Name.lastName, fi)}   |
|partyEcommAddrVar  |#{generate(Internet.emailAddress)}                 |
|partyGenderCd      |Female                                             |
|partyGenderCdL     |#{replaceFirstByRegExp((.).*, $1, <partyGenderCd>)}|
|phoneCntryCd       |91                                                 |
|phoneAreaCd        |011                                                |
|phoneExtNum        |123                                                |
|personalIdTypeCd   |PP                                                 |
|personalIdTypeCd2  |StateRegistration                                  |
|preferenceId       |Confidentiality                                    |
|preferenceListId   |Shared                                             |
|phoneNum1Var       |#{generate(Number.digits '7')}                     |
|phoneNum2Var       |#{generate(Number.digits '7')}                     |
|phoneNum3Var       |#{generate(Number.digits '7')}                     |
|personalIdefDateVar|#{generateDate(P, yyyy-MM-dd'T'HH:mm:ss)}+05:30    |
|personalIdexDateVar|#{generateDate(P1Y, yyyy-MM-dd'T'HH:mm:ss)}+05:30  |
|personalIdValueVar |#{generate(Number.digits '7')}                     |
|subscriptionName   |Auto-Renewal                                       |
|deliveryTypeCd     |EM                                                 |
|subscriptionId     |50                                                 |
|countryPersonalId  |Passport                                           |
|accounts_url       |full-accounts                                      |
|subscriptionNumber |5                                                  |
|ecommAddr1Var      |#{generate(regexify '[a-z]{5}[A-Z]{2}')}@test.com  |
|taxExDateVar       |#{generateDate(P3Y, yyyy-MM-dd'T'HH:mm:ss)}-05:00  |
|firstNameVar       |#{generate(Name.firstName)}<AffCd>                 |
|lastNameVar        |${locale}#{generate(Name.lastName)}                |
|accountNameVar     |<lastNameVar>, <firstNameVar>                      |
|userIdVar          |#{generate(regexify '[a-z]{5}[A-Z]{2}')}@test.com  |
|newUserGETPath     |${affiliate}                                       |
|subscriptionGETPath|${affiliate}                                       |
|searchGETPath      |${affiliate}                                       |
|partyPOSTPath      |generic                                            |
"""

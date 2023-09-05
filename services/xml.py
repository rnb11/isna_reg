from datetime import date
import uuid

CURRENT_DATE = date.today()
SERVICE_NAME = 'BT_ISNA_REG_SYNC'
REQUEST_DATA = """{"requestInfo":{"messageId":"aaaaa-bbbb-cccc-dddddd","dataType":"JUR","offset":141}}"""

REQUEST = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header/>
    <soap:Body>
        <ns3:SendMessage xmlns:ns2="http://bip.bee.kz/SyncChannel/v10/Interfaces" xmlns:ns3="http://bip.bee.kz/SyncChannel/v10/Types">
            <request>
                <requestInfo>
                    <messageId>92000r1a-825d-477f-87eb-c7ff00100766</messageId>
                    <serviceId>ISNA_FL_actualization</serviceId>
                    <messageDate>2009-11-06T22:58:33.058Z</messageDate>
                    <sender>
                        <senderId>GBDFL</senderId>
                        <password>Qwerty!2</password>
                    </sender>
                </requestInfo>
                <requestData>
                    <data xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                        <messageId>e4275682-bf8b-4d6c-b072-5e24fad4db74</messageId>
                        <messageDate>2009-06-15T12:55:24.077+06:00</messageDate>
                        <requestId>4654654654</requestId>
                        <sender>
                            <code>GBDFL</code>
                            <nameRu>ГБД ФЛ</nameRu>
                            <nameKz>ЖТ МДБ</nameKz>
                            <changeDate xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
                        </sender>
                        <receiver>
                            <code>ISNA</code>
                            <nameRu>Исна</nameRu>
                            <nameKz>Исна</nameKz>
                            <changeDate xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
                        </receiver>
                        <messageResult>
                            <code>00000</code>
                            <nameRu>Сообщение успешно обработано</nameRu>
                            <nameKz>Хабарлама сәтті өңделді</nameKz>
                            <changeDate xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
                        </messageResult>
                        <persons>
                            <person>
                                <iin>911212333888</iin>
                                <surname>Test</surname>
                                <name>Test</name>
                                <patronymic></patronymic>
                                <birthDate>2023-09-09</birthDate>
                                <deathDate></deathDate>
                                <gender>
                                    <code>1</code>
                                    <nameRu>Мужской</nameRu>
                                    <nameKz>Ер</nameKz>
                                    <changeDate>2013-09-19T09:44:33+06:00</changeDate>
                                </gender>
                                <nationality>
                                    <code>005</code>
                                    <nameRu>КАЗАХ</nameRu>
                                    <nameKz>ҚАЗАҚ</nameKz>
                                    <changeDate>2013-09-19T09:45:38+06:00</changeDate>
                                </nationality>
                                <citizenship>
                                    <code>398</code>
                                    <nameRu>КАЗАХСТАН</nameRu>
                                    <nameKz>ҚАЗАҚСТАН</nameKz>
                                    <changeDate>2013-09-19T09:45:48+06:00</changeDate>
                                </citizenship>
                                <lifeStatus>
                                    <code>0</code>
                                    <nameRu>Нормальный</nameRu>
                                    <nameKz>Қалыпты</nameKz>
                                    <changeDate>2013-09-19T09:45:30+06:00</changeDate>
                                </lifeStatus>
                                <birthCertificate>
                                    <number>956432</number>
                                    <beginDate>2023-09-09</beginDate>
                                    <issueOrganisation>ЗАГС Аксуского района</issueOrganisation>
                                </birthCertificate>
                                <birthPlace>
                                    <country>
                                        <code>398</code>
                                        <nameRu>КАЗАХСТАН</nameRu>
                                        <nameKz></nameKz>
                                        <changeDate>2013-09-19T09:45:48+06:00</changeDate>
                                    </country>
                                    <region>
                                        <code>1913</code>
                                        <nameRu></nameRu>
                                        <nameKz></nameKz>
                                        <changeDate>2013-09-19T09:45:30+06:00</changeDate>
                                    </region>
                                    <district>
                                        <code>1913000</code>
                                        <nameRu></nameRu>
                                        <nameKz></nameKz>
                                        <changeDate>2013-09-19T09:45:41+06:00</changeDate>
                                    </district>
                                    <city>-</city>
                                </birthPlace>
                                <regAddress>
                                    <country>
                                        <code>398</code>
                                        <nameRu>КАЗАХСТАН</nameRu>
                                        <nameKz>ҚАЗАҚСТАН</nameKz>
                                        <changeDate>2013-09-19T09:45:48+06:00</changeDate>
                                    </country>
                                    <region>
                                        <code>1913</code>
                                        <nameRu>НУР-СУЛТАН</nameRu>
                                        <nameKz>НҰР-СҰЛТАН</nameKz>
                                        <changeDate>2013-09-19T09:45:41+06:00</changeDate>
                                    </region>
                                    <district>
                                        <code>1913000</code>
                                        <nameRu>РАЙОН САРЫАРКА</nameRu>
                                        <nameKz>САРЫАРҚА ауданы</nameKz>
                                        <changeDate>2013-09-19T09:45:28+06:00</changeDate>
                                    </district>
                                    <city></city>
                                    <street></street>
                                    <building></building>
                                    <flat></flat>
                                    <beginDate>2009-04-18</beginDate>
                                    <arCode>1201800092845244</arCode>
                                        <status>
                                            <code>0</code>
                                            <nameRu>Зарегистрирован</nameRu>
                                            <nameKz>Тіркелді</nameKz>
                                        </status>
                                    </regAddress>
<documents>
    <document>
        <type>
            <code>002</code>
            <nameRu>УДОСТОВЕРЕНИЕ РК</nameRu>
            <nameKz>ҚР ЖЕКЕ КУӘЛІГІ</nameKz>
            <changeDate>2013-09-19T09:45:40+06:00</changeDate>
        </type>
        <number>015647</number>
        <beginDate>2039-09-09</beginDate>
        <endDate>2049-08-26</endDate>
        <issueOrganization>
            <code>002</code>
            <nameRu>МИНИСТЕРСТВО ВНУТРЕННИХ ДЕЛ РК</nameRu>
            <nameKz>ҚР ІШКІ ІСТЕР МИНИСТРЛІГІ</nameKz>
            <changeDate>2013-09-19T09:45:40+06:00</changeDate>
        </issueOrganization>
        <status>
            <code>00</code>
            <nameRu>ДОКУМЕНТ ДЕЙСТВИТЕЛЕН</nameRu>
            <nameKz>ҚҰЖАТ ЖАРАМДЫ</nameKz>
            <changeDate>2013-09-19T09:45:40+06:00</changeDate>
        </status>
        <surname>Тестовая</surname>
        <name>Ирина</name>
        <patronymic>КНП</patronymic>
        <birthDate>1990-12-15</birthDate>
    </document>  
</documents>
<removed>false</removed>
</person>
</persons>
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gost34310-gost34311"/>
        <ds:Reference URI="">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gost34311"/>
            <ds:DigestValue>vbJh69TDTlNtoUEb6GoxwgF+qZnwAAsjbu23et5k7eY=</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>MlzZ7wC6BEOwDqyRxoQbSifzucbDuMAEU1JOg04s71s3jCtkymEln9lpypiDIEzPwbOrhW7E8fT/ iRLh+RSgLw==</ds:SignatureValue>
    <ds:KeyInfo>
        <ds:X509Data>
            <ds:X509Certificate>MIIGXDCCBgWgAwIBAgIgd3ZR8AE++lIZY5jGEBxbH/FvgJ/HUhlRFvY0k3VD67AwDgYKKwYBBAG1 EQECAgUAMIIBFDEfMB0GA1UEAwwW0J3Qo9CmINCg0JogKNCT0J7QodCiKTFDMEEGA1UECww60JjQ vdGE0YDQsNGB0YLRgNGD0LrRgtGD0YDQsCDQvtGC0LrRgNGL0YLRi9GFINC60LvRjtGH0LXQuTFx MG8GA1UECgxo0J3QsNGG0LjQvtC90LDQu9GM0L3Ri9C5INGD0LTQvtGB0YLQvtCy0LXRgNGP0Y7R idC40Lkg0YbQtdC90YLRgCDQoNC10YHQv9GD0LHQu9C40LrQuCDQmtCw0LfQsNGF0YHRgtCw0L0x FTATBgNVBAcMDNCQ0YHRgtCw0L3QsDEVMBMGA1UECAwM0JDRgdGC0LDQvdCwMQswCQYDVQQGEwJL WjAeFw0xNTAxMDYwNTQxNTZaFw0xNjAxMDYwNTQxNTZaMIIBhjEYMBYGA1UEBRMPSUlONzIwNzI1 NDAyMDg0MRgwFgYDVQQLDA9CSU45NDAzNDAwMDA0MjExgZAwgY0GA1UECgyBhdCT0J7QodCj0JTQ kNCg0KHQotCS0JXQndCd0J7QlSDQo9Cn0KDQldCW0JTQldCd0JjQlSAi0JzQmNCd0JjQodCi0JXQ oNCh0KLQktCeINCu0KHQotCY0KbQmNCYINCg0JXQodCf0KPQkdCb0JjQmtCYINCa0JDQl9CQ0KXQ odCi0JDQnSIxJjAkBgNVBAMMHdCa0JDQm9CY0JzQntCS0JAg0JLQldCd0JXQoNCQMRkwFwYDVQQE DBDQmtCQ0JvQmNCc0J7QktCQMR8wHQYDVQQqDBbQmtCQ0JzQq9Ch0JHQkNCV0JLQndCQMR4wHAYJ KoZIhvcNAQkBFg9ERFQxOTg3QE1BSUwuUlUxCzAJBgNVBAYTAktaMRUwEwYDVQQIDAzQkNCh0KLQ kNCd0JAxFTATBgNVBAcMDNCQ0KHQotCQ0J3QkDBjMA4GCisGAQQBtREBBQgFAANRAAYCAAA6qgAA AEVDMQACAAB8a9LMqZN1v9dPafum2xZWeCiU3VvBxKstKggawBE2+U8emRt57LRKKrMIMxyJ9dKP vJXmQKoQvwhRSa+NpRWqo4ICozCCAp8wHQYDVR0OBBYEFJF2kl5b/Erm9pcsi/esJzzrRyt3MEIG CCsGAQUFBwEBBDYwNDAyBggrBgEFBQcwAoYmaHR0cDovL3BraS5nb3Yua3ovaW5mby9jYWNlcnRf Z29zdC5jZXIwDAYDVR0jBAUwA4ABMDALBgNVHQ8EBAMCAMAwZAYDVR0uBF0wWzAroCmgJ4YlaHR0 cDovL2NybC5wa2kua3ovY3JsL0dvc3QwX2RlbHRhLmNybDAsoCqgKIYmaHR0cDovL2NybDEucGtp Lmt6L2NybC9Hb3N0MF9kZWx0YS5jcmwwggFIBgNVHSAEggE/MIIBOzCBuwYHKoMOAwMCATCBrzA2 BggrBgEFBQcCARYqaHR0cDovL3BraS5nb3Yua3ovaW5mby9wb2xpY3lfc2lnbl9sZWcucGRmMHUG CCsGAQUFBwICMGkaZ8Tr/yDv7uTv6PHoIP3r5ery8O7t7fv1IOTu6vPs5e3y7uIg/vDo5Oj35fHq 6Owg6+j27uwuIM/w5eTt4Oft4Pfl7ejlIC0g8fTl8OAg3evl6vLw7u3t7uPuIM/w4OLo8uXr/PHy 4uAwewYHKoMOAwMBATBwMDAGCCsGAQUFBwIBFiRodHRwOi8vcGtpLmdvdi5rei9pbmZvL2NhX3Bv bGljeS5wZGYwPAYIKwYBBQUHAgIwMBou0OXj6+Ds5e3yIM3g9uju7eDr/O3u4+4g0+Tu8fLu4uXw //755ePuINbl7fLw4DATBgNVHSUEDDAKBggrBgEFBQcDBDBYBgNVHR8EUTBPMCWgI6Ahhh9odHRw Oi8vY3JsLnBraS5rei9jcmwvR29zdDAuY3JsMCagJKAihiBodHRwOi8vY3JsMS5wa2kua3ovY3Js L0dvc3QwLmNybDAOBgorBgEEAbURAQICBQADQQCYWOPTqk2UoWX6W8KoBMaDE0Rd+SssWX4KCAFp 5QLYPcXqgGIAj1XX6+jnZP1x2yfGZnZecByNye09oDLLY3wi</ds:X509Certificate>
        </ds:X509Data>
    </ds:KeyInfo>
</ds:Signature>
</data>
</requestData>
</request>
</ns3:SendMessage>
</soap:Body>
</soap:Envelope>"""


from googletrans import Translator
translator = Translator(service_urls=['translate.google.com','translate.google.co.kr',])

print(translator.translate('Top'))

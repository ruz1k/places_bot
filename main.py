import telebot
from telebot import types
import pyowm

bot = telebot.TeleBot('957663727:AAHG74tk-jvXVMinhWJSs4TOuOpi_Y88p2g')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_we = types.KeyboardButton(text="/Погода")
    button_hk = types.KeyboardButton(text="/Кальянные")
    button_pu = types.KeyboardButton(text="/Пабы")
    keyboard.add(button_we, button_hk, button_pu)
    bot.send_message(message.chat.id, "Привет, я бот, который покажет тебе кальянные и пабы Казни! Также я могу сказать погоду в Казани!", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, 'В данном боте имеется 3 кнопки. При нажатие у вас появляется выбранный вами перечень.\n' + 
		'Также вы можете посмотреть местоположение на карте паба или кальянной, нажав на /название места в списке!')

@bot.message_handler(commands=['Пабы'])
def kazan_pub(message):
	#Информация про Пабы
	image = open("pub/kznpub.jpg", 'rb')
	bot.send_photo(message.chat.id, image)
	bot.send_message(message.chat.id, text=
		'Ирландский Паб "Тринити" /trinity - сердце Ирландии в Казани.' + 
		' Место, где можно хорошо провести время за парой пинт свежего ирландского пива и ' +
		'насладиться общением с приятными людьми.\n\n' +
		'Top - Hop /tophop - Уникальный крафтовый бар. 39 сортов на кране. Еженедельная ротация на копнах.' +
		' 250 видов охлаждённых бутылок. Компетентные бармены. Очень вкусные блюда, а в особенности бургеры. ул. Баумана, 36\n\n' +
		'Ирландский паб Дублин /dublinpub - один из первых пабов в городе Казани. Здесь собраны лучшие идеи и традиции Ирландских пабов.' +
		' Паб представляет достаточно широкую гамму блюд европейской кухни,' +
		' а в карте бара собраны почти все известные группы крепко алкогольных напитков, аперитивов, коктейлей, разливного пива.'
		' Пиво в пабе является основной гордостью и сможет удовлетворить вкусы самых взыскательных гостей.\n\n' +
		'BEERHOUSE /beerhouse - находится в самом центре Казани, и не зарастает к нему народная тропа.' +
		' Так уж положено в пивном ресторане, чтобы хлебосольно было: пиво - рекой, песни – во весь голос, музыка - хорошая и обязательно живая! ' +
		' Чтобы после доброй пирушки с непременной чекушкой доброта в душе разливалась, душевность и потребность славный подвиг совершить!'
		' А для душевной атмосферы у нас в BEERHOUSE есть все: красивый интерьер, живая музыка, бильярд,'
		'трансляция спортивных матчей, отличное пиво и обильное меню на все вкусы.\n\n' +
		'Brown Bear Grill /bbg - Гриль-бар Brown Bear Grill . Основная идея кухни - это гриль . Все блюда готовятся на древесном гриле , из - за чего мясо' +
        'получается особенно вкусным . Широкий ассортимент крепких напитков, разливного пива, крафтового пива и карта классических коктейлей для вас в нашем баре.' + 
		' Бонусом являются ослепительные улыбки наших бартендеров.\n\n'
		'Что делать?! /what2do - Паб - это идеальное место для проведения деловых встреч за вкусным и домашним обедом, а вечером это угарный и безудержный паб,' +
		'где можно по-настоящему весело провести время, послушать приятную музыку и освежиться вкуснейшим пивом и улетными коктейлями.\n\n'
		'Drink craft /drinkcraft - У нас экранирование от предрассудков, шаблонов и стереотипов!' +
		' За баром вас ждет веселая и дружелюбная команда, а на кранах и в холодильниках бутылочки со всего света!' +
		' Здесь ВСЁ для любителей кислого, горького, сладкого, соленого и просто странного.'
		' А в теплое время года на задворках Баумана у нас припрятана летняя терраса, обустроенная в лучших традициях европейских руинных баров,' +
		' где вы сможете полюбоваться звездами, насладиться живой музыкой и потанцевать под DJ сеты!\n\n'
		'Brew Barrel /brewbarrel - одноименное название ресторана и завода.'+
		' В пивоварении это понятие значимо, потому что пиво проходит второе брожение в дубовых бочках (дословно «вареная бочка»), обычно сделанных из американского дуба,'+
		' в которых до того, как попасть к нам, выдерживались крепкие спиртные напитки. В бочках придаем продукту неповторимость, терпкость, нотки дуба, кофе.'
	    ' Появляются исключительная ароматика и послевкусие, делая наши сорта похожими на вино. \n\n'
	    'BeerPoint Brisket BBQ /beerpoint_bbq - Основа меню бара, американская кухня, а именно мраморная говядина, свинина и птица из собственной коптильни.' +
	    ' Все продукты приготовлены по уникальным рецептам, большая часть которых подразумевает длительное маринование и копчение. ' + 
	    ' В баре Beerpoint BBQ 43 крана, на которых имеются импортные сорта классического бочкового пива.' + 
	    ' Есть также уникальные сорта традиционных стилей, фильтрованное и нефильтрованное пиво, лагеры, стауты и другие сорта.' +
	    ' Меню напитков — это большая, интересная и специально подобранная линейка, тщательно подготовленная и изученная руководством заведения. \n\n'
	    'Декабрист /dekabrist - паб где можно купить отличное пиво от лучших российских и западных пивоварен. Без преувеличения, мы знаем о пиве очень много.' +
        ' Мы сами его варим и дружим с ведущими пивоварами.'
        ' Мы - идеалисты. Мы искренне верим, что пиво не просто может, но и должно отличаться по вкусу, цвету, запаху, плотности.'
        ' Мы - селекционеры. Мы заботливо собираем для Вас лучшие сорта по всему миру. \n\n'
        )

@bot.message_handler(commands=['Кальянные'])
def kazan_hookah(message):
	#Информация про Кальянные
	image = open('hookah/hookah.jpg', 'rb')
	bot.send_photo(message.chat.id, image)
	bot.send_message(message.chat.id, 
		'Hookah Place /hookahplace -  самая большая сеть кальянных в мире. Первый Хукаплейс открылся в москве в 2013 году,' 
		' а уже в 2015 был открыт hookahplace в сша (лос анджелес),' +
		' тем самым доказав работоспособность концепции в мировом масштабе. сейчас семья хукаплейс насчитывает более 160 заведений.' +
		' Вторая хука в самом сердце Казани. Кальяны и табаки со всего мира. Бар с широким ассортиментом алкогольных и безалкогольных напитков.\n\n'
        'Hookah Time /hookahtime - Кальнная Hookah Time, вкусные кальяны, множество разных табаков разной крепости, хорошая атмосфера.' +
        ' Имеется очень много настольных игр. Также большой ассортиментов алкогольных и безалкогольных напитков и в дополнение ко всему, вкусные закуски! \n\n'
        'Example Lounge /examplelounge - цивильное курительное заведение, просторное, чтобы люди не сидели спинами друг к другу, светлое и с хорошей вытяжкой, максимально комфортное, с большой парковкой для автомобилей.' +
        ' Ну а летняя терраса на крыше заведения, с панорамным видом на историческую часть города – не оставила никого равнодушным. Огромный выбор табака и вкусов, китайские чаи и лимонады из натуральных ингредиентов!' +
        ' Миссия компании – это поддержание высокого уровня обслуживания клиентов нашей сети. Организация быстрого и качественного сервиса по оказанию услуг кальянной\n\n'
        'Наше Место /ourplace - Классное место для тех, кто хочет покурить хороший кальян в приятной атмосфере в центре города!' +
        ' Помимо клевой атмосферы, вкуснейших кальянов, авторской кухни/а также доставки еды) большая парковка,  быстро и надежно работающие сотовая связь и вай фай,' +
        ' мощная вытяжка, чтоб не болела голова и не было душно и много чего еще\n\n'
        'Масштаб /masshtab - Уютное заведение, прекрасно подходящее для времяпрепровождения в кругу друзей! Тут каждый найдёт своё!'
        ' В общем зале 5 посадочных мест на 3-4 человека.'
        ' 3 закрытые комнаты вместимостью от 7 до 12 человек.\n\n'
        'Loft Club /loft - Дорогие друзья, мы находимся в центре города. Для Вас создана приятная, неповторимая атмосфера заведения, в которое хочется возвращаться.' +
        ' Мы с пониманием и чуткостью относимся к каждому гостю. \n\n'
        'ДУТЬ /dut - это место в котором вы можете расслабиться, провести время с друзьями, поиграть в консоль,' +
        ' и просто насладиться вкусным чаем и самым ароматным и дымным кальяном!\n\n'
        'Хочу и Буду /hb - сочетает в себе все необходимое для комфортного отдыха. Это не совсем чистая кальянная, это гастро-бар, но я ее включил в данный список так как кальяны у них хорошие! Вход 350 рублей' +
        ' Вход 350 рублей, но цены на кальяны 300 рублей. Очень вкусная еда и также дымные, и вкусны кальяны!\n\n'
        'Luna Lounge /luna — место для тех, кто ценит расслабленный отдых, вкусную еду и клубную атмосферу.Интерьер в светлых тонах смотрится свежо и современно.'
        ' Все пространство поделено на зоны, в каждой из которых чувствуешь себя в уединении, а от общения с близкими ничего не отвлекает.' +
        ' Массивные мягкие кресла, просторные диваны, большие круглые столы — все для того, чтобы отдых был максимально комфортным.' +
        ' По вечерам яркая неоновая подсветка на потолке и диско-шар превращают зал в ночной клуб, где принято танцевать под диджей-сеты и веселиться на полную. \n\n'
        'Unity Hall /unity -  уникальное место, в котором собрано всё лучшее от кальянных, баров и кафе. Это своеобразный микс и здесь каждый найдет что-то, что будет по душе!'
        )

#Описание места и их геолокация
@bot.message_handler(commands=['kzncafe'])
def kazan_pub(message):
	bot.send_message(message.chat.id, 'Такие пабы имеются')

@bot.message_handler(commands=['trinity'])
def handle_trinity(message):
	name = 'Trinity'
	addres = 'Баумана 44/8'
	instagram = 'https://www.instagram.com/trinity_pub_kazan/'
	image = open('pub/caption.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.791368, longitude=49.111634)

@bot.message_handler(commands=['tophop'])
def handle_tph(message):
	name = 'Top Hop'
	addres = 'Баумана, 36'
	instagram = 'https://www.instagram.com/tophopbar/'
	image = open('pub/top hop.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.793151, longitude=49.109533)

@bot.message_handler(commands=['dublinpub'])
def handle_dip(message):
	name = 'Dublin Irish Pub'
	addres = 'Островского, 39/6'
	instagram = 'https://www.instagram.com/dublinpub_kzn/'
	image = open('pub/dublin.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.786919, longitude=49.119247)

@bot.message_handler(commands=['beerhouse'])
def handle_bh(message):
	name = 'Beer House'
	addres = 'Астрономическая, 10'
	instagram = 'https://www.instagram.com/beerhouse_kazan/'
	image = open('pub/beer.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.789298, longitude=49.115996)

@bot.message_handler(commands=['bbg'])
def handle_bbg(message):
	name = 'Brown Bear Grill'
	addres = 'Пушкина, 54/1'
	instagram = 'https://www.instagram.com/brownbeargrill/'
	image = open('pub/bbg.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.794797, longitude=49.125261)

@bot.message_handler(commands=['what2do'])
def handle_wdo(message):
	name = 'Что делать?!'
	addres = 'Чернышевского, 3'
	instagram = 'https://www.instagram.com/what2dobar/'
	image = open('pub/w2do.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.795232, longitude=49.113199)

@bot.message_handler(commands=['drinkcraft'])
def handle_dcraft(message):
	name = 'Drink craft'
	addres = 'Баумана, 25'
	instagram = 'https://www.instagram.com/drinkcraft/'
	image = open('pub/drinkcraft.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.79024, longitude=49.115896)

@bot.message_handler(commands=['brewbarrel'])
def handle_bb(message):
	name = 'Brew Barrel'
	addres = 'Островского, 12'
	instagram = 'https://www.instagram.com/p/BzdAEJSAkh9/'
	image = open('pub/brewb.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.789063, longitude=49.114361)

@bot.message_handler(commands=['beerpoint_bbq'])
def handle_bbq(message):
	name = 'BeerPoint Brisket BBQ'
	addres = 'Чернышевского, 16'
	instagram = 'https://www.instagram.com/beerpoint_brisket_bbq/'
	image = open('pub/bbq.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.792474, longitude=49.109636)

@bot.message_handler(commands=['dekabrist'])
def handle_dekabrist(message):
	name = 'Dekabrist Pub'
	addres = 'Лево-Булачная, 52'
	instagram = 'https://www.instagram.com/dekabristkzn/'
	image = open('pub/dek.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес: {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.786061, longitude=49.115277)

@bot.message_handler(commands=['hookahplace'])
def handle_hp(message):
	name = "Hookah Place"
	addres = "Пушкина, 29А"
	addres2 = "Волкова, 70"
	addres3 = "Фатыха Амирхана, 9"
	instagram = 'https://www.instagram.com/hpvolkova/'
	image = open('hookah/hookah_place.jpg', 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {}; {}; {}; \nInstagram: {}'.format(name, addres, addres2, addres3, instagram))
	bot.send_location(message.chat.id, latitude=55.79269309999999, longitude=49.12417049999999)
	bot.send_location(message.chat.id, latitude=55.787726, longitude=49.14402949999999)
	bot.send_location(message.chat.id, latitude=55.820225, longitude=49.13283810000007)

@bot.message_handler(commands=['hookahtime'])
def handle_ht(message):
	name = "Hookah Time"
	addres = "Островского, 9/3"
	instagram = 'https://www.instagram.com/hookahtimekzn/'
	image = open("hookah/hookah_time.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.78990289999999, longitude=49.11311479999995)

@bot.message_handler(commands=['examplelounge'])
def handle_el(message):
	name = "Example Lounge"
	addres = "Галиаскара Камала, 4а"
	instagram = 'https://www.instagram.com/examplekzn/'
	image = open("hookah/example.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.7871804, longitude=49.11273840000001)

@bot.message_handler(commands=['ourplace'])
def handle_our(message):
	name = "Наше Место"
	addres = "Чистопольская 46"
	addres2 = "Кави Наджми 5"
	addres3 = "Иннополис, Спортивная 116"
	instagram = 'https://www.instagram.com/nashemestokzn/'
	image = open("hookah/our_place.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {}; {}; {}; \nInstagram: {}'.format(name, addres, addres2, addres3, instagram))
	bot.send_location(message.chat.id, latitude=55.818352, longitude=49.12625700000001)
	bot.send_location(message.chat.id, latitude=55.79045559999999, longitude=49.113651300000015)
	bot.send_location(message.chat.id, latitude=55.7489666, longitude=48.74261290000004)

@bot.message_handler(commands=['masshtab'])
def handle_mastab(message):
	name = "Масштаб"
	addres = "Петербургская, 74"
	instagram = 'https://www.instagram.com/masshtab_kzn/'
	image = open("hookah/mastab.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.7783265, longitude=49.139051600000016)

@bot.message_handler(commands=['loft'])
def handle_loft(message):
	name = "Loft Club"
	addres = "Бурхана Шахиди, 9а"
	instagram = 'https://www.instagram.com/loftclub_kzn/'
	image = open("hookah/loft.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.787619, longitude=49.10478790000002)

@bot.message_handler(commands=['dut'])
def handle_dut(message):
	name = "ДУТЬ"
	addres = "Баумана, 58А"
	instagram = 'https://www.instagram.com/dut_club_kzn/'
	image = open("hookah/dut.jpeg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram:'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.79006529999999, longitude=49.11551129999998)

@bot.message_handler(commands=['hb'])
def handle_hr(message):
	name = "Хочу и Буду"
	addres = "Баумана, 25"
	instagram = 'https://www.instagram.com/hochubudu_kzn/'
	image = open("hookah/hb.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.7903819, longitude=49.11615589999997)

@bot.message_handler(commands=['luna'])
def handle_luna(message):
	name = "Luna Lounge"
	addres = "Чистопольская, 3б"
	instagram = 'https://www.instagram.com/luna_lounge_kazan/'
	image = open("hookah/luna.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, instagram))
	bot.send_location(message.chat.id, latitude=55.8189127, longitude=49.09949489999997)

@bot.message_handler(commands=['unity'])
def handle_unity(message):
	name = "Unity Hall"
	addres = "Чистопольская, 3"
	addres2 = "Бутлерова, 21"
	instagram = 'https://www.instagram.com/unityhall/'
	image = open("hookah/unity_hall.jpg", 'rb')
	bot.send_photo(message.chat.id, image, caption='{} \nАдрес : {} \nInstagram: {}'.format(name, addres, addres2, instagram))
	bot.send_location(message.chat.id, latitude=55.81905219999999, longitude=49.099207999999976)
	bot.send_location(message.chat.id, latitude=55.7879605, longitude=49.13016429999993)

@bot.message_handler(commands=["Погода"])
def handle_weather(message):
	#Погода
	owm = pyowm.OWM('9d65f4d82febb9ecf669d223518e69d0')
	observation = owm.weather_at_place("Kazan")
	w = observation.get_weather()
	humidity = w.get_humidity()
	wind = w.get_wind()
	temp = w.get_temperature('celsius')
	convert_temp = temp.get('temp')
	convert_wind = wind.get('speed')
	convert_humidity = humidity
	text_temp = str(convert_temp)
	text_wind = str(convert_wind)
	text_humidity = str(convert_humidity)
	bot.send_message(message.chat.id, text="На сегодняшний день температура в Казани такова: \n\n Температура: {} ℃ \n Скорость ветра: {} м/с \n Влажность: {}%".format(text_temp, text_wind, text_humidity))

bot.polling()


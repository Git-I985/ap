CREATE DATABASE IF NOT EXISTS `alinaproj`;

INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (6, 'АО «Тандер»', '132814, Ивановская область, город Сергиев Посад, пр. Чехова, 29', '+7 984 957-51-35',
        'dprice@aol.com');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (7, 'X5 Group', '617743, Оренбургская область, город Пушкино, проезд Будапештсткая, 11', '+7 958 024-04-01',
        'peoplesr@icloud.com');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (8, 'Евроспар', '588008, Тверская область, город Наро-Фоминск, проезд Будапештсткая, 29', '+7 925 515-81-35',
        'jmorris@att.net');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (9, 'ООО Вкусный выбор', '300343, Архангельская область, город Лотошино, пл. Домодедовская, 77',
        '+7 982 745-86-14', 'valdez@yahoo.ca');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (10, 'ИП Продуктовый мир', '492896, Тульская область, город Павловский Посад, проезд Сталина, 78',
        '+7 923 970-12-20', 'balchen@att.net');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (11, 'АО Свежий урожай', '014898, Ульяновская область, город Подольск, пр. Ломоносова, 61', '+7 980 105-20-50',
        'chance@yahoo.ca');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (12, 'ИП Зеленый рынок', '276325, Челябинская область, город Наро-Фоминск, пр. Сталина, 35', '+7 962 183-30-81',
        'philen@att.net');
INSERT INTO alinaproj.client (id, company, adress, phone, mail)
VALUES (13, 'ООО Премиум Продукты', '172229, Свердловская область, город Ступино, въезд Ленина, 34', '+7 987 533-01-87',
        'onestab@att.net');
INSERT INTO alinaproj.delivery (id, supplier_id, date, status_id)
VALUES (6, 4, '2000-01-01 00:00:00', 7);

INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (7, 'Ожидание');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (8, 'В пути');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (9, 'Получено на склад');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (10, 'Проверка качества');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (11, 'Отменено');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (12, 'Возврат');
INSERT INTO alinaproj.deliverystatus (id, name)
VALUES (13, 'Завершено');
INSERT INTO alinaproj.deliverytoproduct (id, delivery_id, product_id, amount)
VALUES (1, 6, 20, 2400.00000);
INSERT INTO alinaproj.deliverytoproduct (id, delivery_id, product_id, amount)
VALUES (2, 6, 27, 580.00000);
INSERT INTO alinaproj.deliverytoproduct (id, delivery_id, product_id, amount)
VALUES (3, 6, 29, 920.00000);
INSERT INTO alinaproj.`order` (id, client_id, delivery_date, adress, status_id)
VALUES (17, 6, '2023-03-12 00:00:00', '251422, Самарская область, город Волоколамск, наб. Косиора, 47', 6);
INSERT INTO alinaproj.`order` (id, client_id, delivery_date, adress, status_id)
VALUES (18, 8, '2023-03-12 00:00:00', '457962, Тамбовская область, город Видное, пл. Домодедовская, 95', 6);
INSERT INTO alinaproj.`order` (id, client_id, delivery_date, adress, status_id)
VALUES (19, 13, '2023-03-15 00:00:00', '309575, Волгоградская область, город Москва, пер. Гагарина, 26', 6);

INSERT INTO alinaproj.orderstatus (id, name)
VALUES (6, 'В обработке');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (7, 'Отправлено');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (8, 'В пути');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (9, 'Доставлено');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (10, 'Отменено');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (11, 'Возврат');
INSERT INTO alinaproj.orderstatus (id, name)
VALUES (12, 'Завершено');

INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (1, 17, 20, 12.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (2, 17, 23, 32.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (3, 17, 28, 23.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (4, 17, 25, 23.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (5, 18, 30, 12.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (6, 18, 24, 50.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (7, 19, 21, 120.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (8, 19, 22, 230.00000);
INSERT INTO alinaproj.ordertoproduct (id, order_id, product_id, amount)
VALUES (9, 19, 29, 180.00000);

INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (20, 'Яйцо куриное Волжанин С', 15, 177.00000, 169.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (21, 'Сыр мягкий Natura Сливочный 45% БЗМЖ', 15, 303.00000, 289.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (22, 'Молоко 2,5% пастеризованное 930 мл Домик в деревне', 15, 58.00000, 55.00000, 7, 2.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (23, 'Авокадо Хасс Artfruit', 16, 177.00000, 169.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (24, 'Томаты черри Рост премиум, красные', 16, 91.00000, 87.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (25, 'Салат Айсберг', 16, 75.00000, 71.00000, 7, 2.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (26, 'Креветки Королевские замороженные', 21, 236.00000, 225.00000, 7, 8.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (27, 'Корейка свиная Слово Мясника', 22, 261.00000, 249.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (28, 'Фарш Слово мясника по-домашнему охлажденный', 22, 167.00000, 159.00000, 7, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (29, 'Вода минеральная Donat Mg газированная лечебная пластик', 26, 167.00000, 159.00000, 10, 5.00000);
INSERT INTO alinaproj.product (id, name, category_id, sale_price, buy_price, unit_id, margin)
VALUES (30, 'Сок с мякотью Сады Придонья мультифрукт', 26, 52.00000, 50.00000, 10, 3.00000);

INSERT INTO alinaproj.productcategory (id, name)
VALUES (15, 'Молочные продукты, сыр и яйца');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (16, 'Фрукты, ягоды и овощи');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (17, 'Хлеб и хлебобулочные изделия');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (18, 'Рыба и морепродукты');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (21, 'Замороженные продукты');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (22, 'Мясо и птица ');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (23, 'Алкоголь');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (24, 'Чай, кофе, какао');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (25, 'Детское питание');
INSERT INTO alinaproj.productcategory (id, name)
VALUES (26, 'Напитки');

INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (3, 'ООО "Ореховый Алтай"', '189493, Псковская область, город Дмитров, проезд Бухарестская, 40',
        '+7 984 957-51-35', 'dprice@aol.com');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (4, 'SMART FMCG', '797101, Оренбургская область, город Можайск, спуск Косиора, 12', '+7 958 024-04-01',
        'peoplesr@icloud.com');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (5, 'ООО "ЭЛЛАДА"(ПРОДУКТЫ ИЗ ГРЕЦИИ)', '177987, Московская область, город Балашиха, наб. Домодедовская, 71',
        '+7 925 515-81-35', 'jmorris@att.net');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (6, 'ООО «ССК Ритейл»', '858481, Томская область, город Москва, пер. Славы, 17', '+7 982 745-86-14',
        'valdez@yahoo.ca');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (7, 'Чайно-кофейная фабрика AROMA TEA COFFEE',
        '046296, Костромская область, город Солнечногорск, шоссе Сталина, 21', '+7 923 970-12-20', 'balchen@att.net');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (8, 'Продукты из Беларуси ОПТ', '891250, Московская область, город Ступино, пер. Бухарестская, 50',
        '+7 980 105-20-50', 'chance@yahoo.ca');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (9, 'Производство и оптовая продажа морепродуктов премиум-класса.',
        '501104, Нижегородская область, город Наро-Фоминск, ул. Космонавтов, 44', '+7 962 183-30-81', 'philen@att.net');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (10, 'Кондитерская фабрика "ФинТур"', '413980, Пензенская область, город Сергиев Посад, наб. Будапештсткая, 52',
        '+7 987 533-01-87', 'onestab@att.net');
INSERT INTO alinaproj.supplier (id, company, adress, phone, mail)
VALUES (11, 'ООО "ГРАНД-МИТ"', '494713, Тульская область, город Одинцово, бульвар Балканская, 20', '+7 936 918-45-43',
        'scottzed@aol.com');

INSERT INTO alinaproj.units (id, name)
VALUES (7, 'г');
INSERT INTO alinaproj.units (id, name)
VALUES (8, 'шт');
INSERT INTO alinaproj.units (id, name)
VALUES (9, 'кг');
INSERT INTO alinaproj.units (id, name)
VALUES (10, 'л');
INSERT INTO alinaproj.units (id, name)
VALUES (11, 'мл');

INSERT INTO alinaproj.user (id, name, login, password, role_id)
VALUES (18, '', 'a', '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8', 5);
INSERT INTO alinaproj.user (id, name, login, password, role_id)
VALUES (19, '', 'm', '6b0d31c0d563223024da45691584643ac78c96e8', 6);
INSERT INTO alinaproj.user (id, name, login, password, role_id)
VALUES (20, '', 'r', '4dc7c9ec434ed06502767136789763ec11d2c4b7', 7);
INSERT INTO alinaproj.user (id, name, login, password, role_id)
VALUES (21, '', 'b', 'e9d71f5ee7c92d6dc9e92ffdad17b8bd49418f98', 8);

INSERT INTO alinaproj.userrole (id, name)
VALUES (5, 'Администратор');
INSERT INTO alinaproj.userrole (id, name)
VALUES (6, 'Менеджер');
INSERT INTO alinaproj.userrole (id, name)
VALUES (7, 'Работник склада');
INSERT INTO alinaproj.userrole (id, name)
VALUES (8, 'Бухгалтер');

INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (5, 20, 8000.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (6, 27, 420.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (7, 28, 8320.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (8, 28, 320.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (9, 30, 321.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (10, 22, 3202.00000);
INSERT INTO alinaproj.warehouse (id, product_id, amount)
VALUES (11, 25, 230.50000);


DROP PROCEDURE IF EXISTS alinaproj.calculate_sale_price;
delimiter //
CREATE PROCEDURE alinaproj.calculate_sale_price(buy_price int, margin int, out sale_price int)
begin
    SET sale_price = buy_price + (margin * (buy_price / 100));
end//
delimiter ;

DROP TRIGGER IF EXISTS alinaproj.on_products_insert;
delimiter //
CREATE TRIGGER alinaproj.on_products_insert
    BEFORE INSERT
    ON alinaproj.product
    FOR EACH ROW
BEGIN
    set @sale_price = 0;
    call alinaproj.calculate_sale_price(NEW.buy_price, NEW.margin, @sale_price);
    SET NEW.sale_price = @sale_price;
END//
delimiter ;
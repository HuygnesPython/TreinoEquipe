create database eventos_db;

use eventos_db;

create table show_db(
id int primary key auto_increment,
nome varchar (255) not null,
data_show date not null,
descricao text,
create_at datetime default current_timestamp
);

insert into show_db(nome, data_show, descricao) values
("matue fortal2025","2025-07-09","Uma das melhores atraçao da cidade"),
("sao joao maracanau2025","2025-06-12","dias dos namorados de uma forma diferente"),
("marinaparck eletronica ediçao 2","2025-12-08","melhore sua vibe"),
("bruna carla beira mar","2025-07-10","traga sua familia pra cultuar"),
("show golpel fortaleza","2025-06-29","Casa de deus")
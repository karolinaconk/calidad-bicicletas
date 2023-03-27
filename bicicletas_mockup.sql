-- Crear la base de datos
DROP DATABASE IF EXISTS centro_comercial_renta_bicicletas;
CREATE DATABASE centro_comercial_renta_bicicletas;

-- Usar la base de datos
USE centro_comercial_renta_bicicletas;

-- Crear la tabla de usuarios

DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  correo_electronico VARCHAR(50) NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  identificacion VARCHAR(20) NOT NULL
);

-- Crear la tabla de bicicletas
DROP TABLE IF EXISTS bicicletas;
CREATE TABLE bicicletas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  marca VARCHAR(50) NOT NULL,
  modelo VARCHAR(50) NOT NULL,
  tamano VARCHAR(20) NOT NULL,
  imagen VARCHAR(200) NOT NULL
);

INSERT INTO bicicletas (marca, modelo, tamano, imagen) VALUES
  ('Specialized', 'Rockhopper', 'M', 'https://www.rei.com/media/product/1599240012'),
  ('Trek', 'FX Sport 4', 'L', 'https://www.rei.com/media/product/136074'),
  ('Giant', 'TCR Advanced Pro 1', 'S', 'https://www.rei.com/media/product/163215'),
  ('Cannondale', 'Synapse Carbon Disc 105', 'L', 'https://www.rei.com/media/product/1510530016'),
  ('Raleigh', 'Cadent 3', 'M', 'https://www.rei.com/media/product/1313380015'),
  ('Fuji', 'Gran Fondo 2.1 Disc', 'S', 'https://www.rei.com/media/product/156645'),
  ('Diamondback', 'Trace ST', 'L', 'https://www.rei.com/media/product/152485'),
  ('Salsa', 'Warbird Carbon 105 700', 'M', 'https://www.rei.com/media/product/155300');


-- Crear la tabla de transacciones
DROP TABLE IF EXISTS transacciones;
CREATE TABLE transacciones (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  id_bicicleta INT NOT NULL,
  fecha_alquiler DATETIME NOT NULL,
  fecha_devolucion DATETIME NOT NULL,
  duracion_alquiler INT NOT NULL,
  costo_alquiler FLOAT NOT NULL,
  estado_pago VARCHAR(20) NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
  FOREIGN KEY (id_bicicleta) REFERENCES bicicletas(id)
);
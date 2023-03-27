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
  ('Specialized', 'Rockhopper', 'M', 'https://images.immediate.co.uk/production/volatile/sites/21/2021/04/Specialized-Rockhopper-Comp-hardtail-mountain-bike-01-300dff1.jpg?quality=90&resize=620%2C413'),
  ('Trek', 'FX Sport 4', 'L', 'https://i.ytimg.com/vi/MCj0g59upz8/maxresdefault.jpg'),
  ('Giant', 'TCR Advanced Pro 1', 'S', 'https://bikestore.com.mx/blog/wp-content/uploads/2021/02/P1012949-1d.jpg'),
  ('Cannondale', 'Synapse Carbon Disc 105', 'L', 'https://images.immediate.co.uk/production/volatile/sites/21/2023/01/C23SynapseAlloy-hero-a8e8b68.jpg?quality=45&resize=768,574'),
  ('Raleigh', 'Cadent 3', 'M', 'https://www.sefiles.net/images/library/large/raleigh-cadent-3-361393-18.png'),
  ('Fuji', 'Gran Fondo 2.1 Disc', 'S', 'https://cdn.road.cc/sites/default/files/fuji-gran-fondo-1.1-glamour-shot.jpg'),
  ('Diamondback', 'Trace ST', 'L', 'https://m.media-amazon.com/images/I/5179j7XygkL._AC_.jpg'),
  ('Salsa', 'Warbird Carbon 105 700', 'M', 'https://s3.amazonaws.com/www.bikerumor.com/wp-content/uploads/2018/09/02155216/2019-Salsa-Warbird-v4_lightweight-650B-700C-carbon-gravel-road-race-bike_105-complete.jpg');


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
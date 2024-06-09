from PIL import Image

# Definindo as dimensões da imagem
largura = 800
altura = 600

# Criando uma imagem em branco com o tamanho especificado
image = Image.new("RGB", (largura, altura))

# Definindo cores para o céu, grama e sol
cor_ceu = (135, 206, 250)  # Azul celeste
cor_grama = (34, 139, 34)  # Verde escuro
cor_sol = (255, 255, 0)  # Amarelo

# Preenchendo o céu
for x in range(largura):
    for y in range(altura // 2):
        image.putpixel((x, y), cor_ceu)

# Preenchendo a grama
for x in range(largura):
    for y in range(altura // 2, altura):
        image.putpixel((x, y), cor_grama)

# Desenhar o sol
center_x = largura // 2
center_y = altura // 4
raio = 50
for x in range(center_x - raio, center_x + raio):
    for y in range(center_y - raio, center_y + raio):
        if (x - center_x)**2 + (y - center_y)**2 <= raio**2:
            image.putpixel((x, y), cor_sol)

# Salvar a imagem gerada
image.save("imagem_natural.png")

# Mostrar a imagem
image.show()
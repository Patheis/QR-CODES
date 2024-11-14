from PIL import Image
import os

# Caminho da pasta com as imagens de QR Codes
input_folder = r'C:\QRCodes'
# Caminho para salvar as imagens sem fundo
output_folder = r'C:\QRCodes_Transparent'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

       
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        
        new_data = []
        for item in datas:
            
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0)) 
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")

        print(f"Fundo removido da imagem: {filename}")

print("Processamento concluído. Imagens sem fundo salvas na pasta:", output_folder)

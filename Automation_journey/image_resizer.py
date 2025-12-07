from PIL import Image
image_path = input("Enter the image path:").strip()
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))

try:
    img = Image.open(image_path)
    resized_img = img.resize((new_width, new_height))
    save_path = image_path.replace('.', '_resized.')
    resized_img.save(save_path)
    print(f"Image resized successfully and saved to {save_path}")
except FileNotFoundError:
    print("The specified image file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


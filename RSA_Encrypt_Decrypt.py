"""
This script demonstrates a simple RSA encryption and decryption app using the Gradio library. 
Users can input plain text and choose between encryption and decryption using RSA algorithm. 
The script generates a key pair, encrypts or decrypts the input text accordingly, and displays the result in the interface.

Author: Abdul Qadeer
Email: itsabdulqadeer.55@gmail.com
Project: RSA Encryption/Decryption App
"""

import gradio as gr
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def encrypt_message(plain_text):
    message = plain_text.encode('utf-8')
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def decrypt_message(ciphertext):
    decrypted_message = private_key.decrypt(
        bytes.fromhex(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode('utf-8')

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

    
def encrypt_interface(plain_text_or_cipher_text, operation):
    if operation == "Encrypt":
        try:
            return encrypt_message(plain_text_or_cipher_text).hex()
        except Exception as e:
            return f"Encryption failed: {e}"
    elif operation == "Decrypt":
        try:
            return decrypt_message(plain_text_or_cipher_text)
        except Exception as e:
            return f"Decryption failed: {e}"
    else:
        return "Invalid operation selected. Please choose either 'Encrypt' or 'Decrypt'."


iface = gr.Interface(
    fn=encrypt_interface,
    inputs=[gr.Textbox(lines=5, label="Plain Text or Cipher Text"), 
            gr.Radio(["Encrypt", "Decrypt"], label="Operation")],
    outputs=gr.Textbox(label="Processed Text"),
    title="(Abdul Qadeer)-RSA Encryption/Decryption",
    description="This is a simple RSA encryption and decryption app to securely encrypt and decrypt messages using the RSA algorithm.",
)

iface.launch(debug=True)

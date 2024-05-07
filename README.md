
  <h1>Caesar Cipher Program</h1>

  <h2>Overview</h2>
  <p>This is a Python program that implements the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This program allows users to encrypt and decrypt text messages either through the console or by processing files.</p>

  <h2>Features</h2>
  <ul>
    <li>Encrypt and decrypt text messages using the Caesar Cipher algorithm.</li>
    <li>Supports encryption and decryption via the console or by processing text files.</li>
    <li>User-friendly interface with clear instructions and error handling.</li>
  </ul>

  <h2>Usage</h2>
  <ol>
    <li><strong>Installation</strong>: Ensure you have Python installed on your system. Clone this repository to your local machine.</li>
    <li><strong>Running the Program</strong>:
      <ul>
        <li>Open a terminal or command prompt.</li>
        <li>Navigate to the directory where the program is located.</li>
        <li>Run the program by executing the command:<br><code>python caesar_cipher.py</code></li>
      </ul>
    </li>
    <li><strong>Using the Program</strong>:
      <ul>
        <li>Upon running the program, you'll be presented with a welcome message and instructions.</li>
        <li>Choose whether you want to encrypt or decrypt a message.</li>
        <li>Choose whether to input the message via the console or by processing a text file.</li>
        <li>If encrypting or decrypting via the console, enter the message and the shifting code when prompted.</li>
        <li>If processing a file, enter the file name or path as instructed.</li>
        <li>The encrypted or decrypted message will be displayed, and the result will also be saved to a file named <code>result.txt</code>.</li>
      </ul>
    </li>
    <li><strong>Exiting the Program</strong>:
      <ul>
        <li>After each operation, you'll be asked if you want to continue using the cipher.</li>
        <li>Type 'y' to continue or any other key to exit.</li>
      </ul>
    </li>
  </ol>

  <h2>Example</h2>
  <p>Here's a simple example of encrypting a message via the console:</p>
  <pre>
    <code>
Welcome to the Caesar Cipher Program

Would you like to encrypt (e) or decrypt (d) or exit(x) to exit
Enter Your Choice >>> e

Enter (c) for console or (f) for file
Enter your Choice >>> c

Enter text you wand to input
Enter your Text >>> hello

Enter Shifting code
Enter your Code >>> 3

Result >>> 
    *** WQRRU ***    

Do You Want To Use The Cipher Again y to continue or any keys to exit
Enter your Choice >>> n

*** Thank you ***
    </code>
  </pre>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

  <hr>

  <p>Created by Aryan Neupane</p>



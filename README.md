# playground-virus
Basic virus made to understand the working of virus on systems and how they use various methods like persistence(i.e, being able to run even beyond the session the virus was installed in) or how they shread the virus
        **The program is just for educational purpose to get a rundown how what virus' try to do in our systems. Please run this program on a sandbox or VM(definitely not on your friends system by just disabling the antivirus for a few mins) environment**
```
PlaygroundVirus
├── main.py # The main virus spearhead which runs everything
├── persistence.py # Hides in %APPDATA% and creates a Run key
├── spreader.py # Drops copies into Desktop, Downloads, Documents, and USBs
├── mimic.py # Shows fake message
├── killswitch.py # A easy method to revert everything the virus did which I was able to make because i knew exactly what and how the virus does and works
├── payloads/
│ ├── init.py # to convert the payloads folder into a useable package
│ ├── keylogger.py # Logs keystrokes to %APPDATA%\keylogger.txt
│ ├── fake_msg.py # Shows fake popups when browser or explorer opens(just to mess with people)
│ └── cpu_stress.py # Eats CPU with background threads
```
## Steps to run
1. Clone the repo into a sandbox or VM environment(*wink*)
    ```
    git clone https://github.com/SudhanshuRai-Flme/playground-virus.git
    ```
2. Open the terminal in the cloned repo folder
3. Install the required python modules or just run the below command in your opened terminal
    ```
    pip install -r requirements.txt
    ```
4. Run the program by opening the main.py file in your preferred IDE and then running it or just put the below command in the aforementioned terminal
    ```
    python main.py
    ```
5. (Optional😅) If form some bizzare reason you wanna remove the virus from whichever system you have it installed to just run killswitch.py or run the script in the terminal with the command
    ```
    python killswitch.py
    ```

### Each script in and of itself has comments explaining what it does 
Mandatory disclaimer once again 
**Run only on machines you own (preferably inside a virtual machine). This is just a simulated and not a real virus**
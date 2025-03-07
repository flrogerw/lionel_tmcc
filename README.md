# Lionel Train Controller GUI

This project is a **GUI-based controller** for a **Lionel Train Command Control (TMCC) system**, built using **Python** and **Tkinter**. The application communicates with the train via a **serial connection** (USB-to-serial adapter) and sends TMCC commands to control the train’s direction, throttle, and additional features like the whistle and emergency halt.

## Features  
- **Throttle Control**: Adjust the train speed using a slider (0-40 scale).  
- **Direction Control**: Switch between **Forward, Neutral, and Reverse**.  
- **Whistle**: Activate the train's whistle with a button click.  
- **Emergency Halt**: Instantly stop the train by cutting track power.  

## Requirements  
- **Python 3.x**  
- **Tkinter** (Built into Python)  
- **PySerial** (`pip install pyserial`)  

## Installation  
1. Clone the repository or download the script.  
2. Install dependencies:  
   ```sh
   pip install pyserial
   ```  
3. Connect your **Lionel TMCC controller** via a USB-to-serial adapter.  

## Configuration  
By default, the script connects to the **serial port** `/dev/cu.usbserial-A1081AFL` at **9600 baud rate**. If your setup uses a different port, update this line in the script:  
```python
ser.port = '/dev/cu.usbserial-YOURPORT'
```  

## Usage  
Run the script:  
```sh
python train_controller.py
```  
This will launch the **Lionel Controller GUI**.  

## Controls  
| Button         | Function                                      |  
|---------------|-----------------------------------------------|  
| **Forward**   | Moves the train forward                      |  
| **Neutral**   | Puts the train in neutral                    |  
| **Reverse**   | Moves the train in reverse                   |  
| **Whistle**   | Activates the train whistle                  |  
| **Halt**      | Immediately stops the train                  |  
| **Throttle**  | Adjusts speed using a slider (0-40 range)    |  

## Troubleshooting  
- If the train **doesn't respond**, check the **serial port configuration**.  
- Ensure that the **USB-to-serial adapter** is properly connected.  
- Try restarting the script and reconnecting the controller.  

## License  
This project is for **personal and educational use**. Feel free to modify and improve it!  

🚂 **Happy Railroading!** 🚂  


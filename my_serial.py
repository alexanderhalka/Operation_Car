class my_Serial:
    def initializeSerial():
        """
        Configure serial port (baud rate, data bits, etc.).
        Open the serial port.
        Return success/failure status.
        """
        pass
        
    def sendToSerial(processedData):
        """
        Take processed data.
        Send it through serial port.
        Handle any transmission errors.
        Return success/failure status.
        """
        pass
    
    def cleanup():
        """
        Close serial port.
        """
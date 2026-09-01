"""
16. Wi-Fi Diagnostic Tree     

Figure 3-21 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. 
Use the flowchart to create a program that leads a person through the steps of fixing a bad Wi-Fi connection. 
Here is an example of the program’s output:Notice the program ends as soon as a solution is found to the problem. 
Here is another example of the program’s output:200

"""

def main():
    print("Lets try to fix you Wi-Fi connection!")
    print(" Reboot the computer and try to connect.")
    answer = input("Did that fix the problem? (yes or no): ")
    if answer.lower() == "yes":
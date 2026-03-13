import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage
import mimetypes

def SendMail(Receiver, Attachment) :
    Sender = "shreyapythontesting@gmail.com"
    app_password = "fyxsfdtiadqfmiqy"

    sub = f"System Surveillance Log at {time.ctime()}"
    # Mail object creation 
    msg = EmailMessage()

    # Set mail headers
    msg["From"] = Sender
    msg["To"] = Receiver
    msg["Subject"] = sub   

    # Create mail Body
    Body = f"""
    ---PLATFORM SURVEILLANCE SYSTEM---

    The LOG FILE attached to this mail contains the summary of :
        Top CPU Usage Processes
        Top Memory Usage Processes
        Top Thread Count Processes
        Top Open Files Processes
    
    Do check the file thoroughly!

    Thank you!!!
    """ 
    # Add Mail Body
    msg.set_content(Body)

    # Attachment Handling
    ctype, encoding = mimetypes.guess_type(Attachment)
    if ctype is None or encoding is None :
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/',1)

    if os.path.exists(Attachment) :
        with open(Attachment, 'rb') as f :
            Data = f.read()
            Path = os.path.basename(Attachment)

        msg.add_attachment(Data, maintype = maintype, subtype = subtype, filename = Path)

    # Create secure SMTP connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Login
    smtp.login(Sender,app_password)

    #Send Mail
    smtp.send_message(msg)

    smtp.quit()

    print("Mail send successfully!")

def CreateLog(FolderName, ReciverEmail) :
    Border = "-"*60
    Ret = False

    Ret = os.path.exists(FolderName)
    if (Ret == True) :
        Ret = os.path.isdir(FolderName)
        if(Ret == False) :
            print("Unable to create folder")
            return
    else :
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp)
    print("File gets created with name : ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("----------Marvellous Platform Surveillance System-----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------------System Report-------------------------\n")
    #print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")
    
    mem = psutil.virtual_memory()
    #print("RAM Usage : ",mem.percent)
    fobj.write("RAM Usage : %s %%\n" %mem.percent)

    fobj.write(Border+"\n")

    fobj.write("Disk Usage Report \n")
    for part in psutil.disk_partitions() :
        try : 
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except :
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()            # used to get data sent and received from internet
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))  
    fobj.write("Receive : %.2f MB\n" %(net.bytes_recv / (1024*1024)))

    # Process LOG
    Data = ProcessScan()

    CPUSorted = sorted(Data, key = lambda item : item['cpu_percent'], reverse = True)[:10]
    
    MemSorted = sorted(Data, key = lambda item : item['memory_percent'], reverse = True)[:10]

    ThreadSorted = sorted(Data, key = lambda item : item['num_threads'], reverse = True)[:10]

    OpenFilesSorted = sorted(Data, key = lambda item : (item['open_files']) if str(item['open_files']).isdigit() else 0, reverse = True)[:10]

    fobj.write(Border+"\n")
    fobj.write("------------------Top CPU Usage Processes-------------------\n")
    fobj.write(Border+"\n") 

    for info in CPUSorted :
        fobj.write(f"PID : {info['pid']}\n")
        fobj.write(f"Name : {info['name']}\n" )
        fobj.write(f"Start Time : {info['create_time']}\n" )
        fobj.write(f"CPU %% : {info['cpu_percent']}\n")
        fobj.write(f"Thread Count : {info['num_threads']}\n")
        fobj.write(f"Number of Files Opened : {info['open_files']}\n")
        fobj.write(f"RSS - Resident Set Size : {info['rss']} MB\n")
        fobj.write(f"{Border}\n")

    fobj.write(Border+"\n")
    fobj.write("----------------Top Memory Usage Processes------------------\n")
    fobj.write(Border+"\n") 

    for info in MemSorted :
        fobj.write(f"PID : {info['pid']}\n")
        fobj.write(f"Name : {info['name']}\n" )
        fobj.write(f"Start Time : {info['create_time']}\n" )
        fobj.write(f"CPU %% : {info['cpu_percent']}\n")
        fobj.write(f"Thread Count : {info['num_threads']}\n")
        fobj.write(f"Number of Files Opened : {info['open_files']}\n")
        fobj.write(f"RSS - Resident Set Size : {info['rss']} MB\n")
        fobj.write(f"{Border}\n")

    fobj.write(Border+"\n")
    fobj.write("----------------Top Thread Count Processes------------------\n")
    fobj.write(Border+"\n") 

    for info in ThreadSorted :
        fobj.write(f"PID : {info['pid']}\n")
        fobj.write(f"Name : {info['name']}\n" )
        fobj.write(f"Start Time : {info['create_time']}\n" )
        fobj.write(f"CPU %% : {info['cpu_percent']}\n")
        fobj.write(f"Thread Count : {info['num_threads']}\n")
        fobj.write(f"Number of Files Opened : {info['open_files']}\n")
        fobj.write(f"RSS - Resident Set Size : {info['rss']} MB\n")
        fobj.write(f"{Border}\n")

    
    fobj.write(Border+"\n")
    fobj.write("-----------------Top Open files Processes-------------------\n")
    fobj.write(Border+"\n") 

    for info in OpenFilesSorted :
        fobj.write(f"PID : {info['pid']}\n")
        fobj.write(f"Name : {info['name']}\n" )
        fobj.write(f"Start Time : {info['create_time']}\n" )
        fobj.write(f"CPU %% : {info['cpu_percent']}\n")
        fobj.write(f"Thread Count : {info['num_threads']}\n")
        fobj.write(f"Number of Files Opened : {info['open_files']}\n")
        fobj.write(f"RSS - Resident Set Size : {info['rss']} MB\n")
        fobj.write(f"{Border}\n")

    fobj.write(Border+"\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------------------End of Log File------------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

    SendMail(ReciverEmail, FileName)

def ProcessScan() :
    ListProcess = []

    print("Process Scan Report")

    # Warm up for CPU percent
    for proc in psutil.process_iter() :
        try :
            proc.cpu_percent()
        except :
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter() :
        try : 
            info = proc.as_dict(attrs = ["pid" , "name" , "username", "status", "create_time","num_threads","open_files"])
            # Convert create_time
            try :
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M%:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            file = proc.open_files()

            info["num_threads"] = proc.num_threads()
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["open_files"] = len(file)
            info["rss"] = proc.memory_info().rss / 1024 * 1024      # to convert into mb
            info["vms"] = proc.memory_info().vms / 1024 * 1024

            ListProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            info["open_files"] = "Access Denied"   

    return ListProcess       

def main() :
    Border = "-"*60
    print(Border)
    print("----------Marvellous Platform Surveillance System-----------")
    print(Border)

    if(len(sys.argv) == 2) :
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H") :
            print("This script is used to ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Stores information about the processes")
            print("5 : Stores information about CPU")
            print("6 : Stores information about RAM usgae")
            print("7 : Stores information about secondary storage")
            print("8 : Send this log of info through mail")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
            print("Use the Automation as ")
            print("ScriptName.py DirectoryName ReciverMailID TimeInterval")
            print("DirectoryName : Name of Directory to create auto logs")
            print("Receiver email : Mail id to which you want to send log periodically")
            print("TimeInterval : The time in minutes for periodic scheduling")

        else :
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 4) :

        # Apply the Scheduler
        schedule.every(int(sys.argv[3])).minutes.do(CreateLog, sys.argv[1], sys.argv[2])

        print("Marvellous Platform Surveillance System started successfully")
        print("Directory created with name : ",sys.argv[1])
        print("Receiver email is : ",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[3])
        print("Press Ctrl + C to stop the execution")

        # Wait till Abort
        while(True) :
            schedule.run_pending()
            time.sleep(1)

    else :
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------------Thank you for using our script----------------")
    print(Border)

if __name__ == "__main__" :
    main()